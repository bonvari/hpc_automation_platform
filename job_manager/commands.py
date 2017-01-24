import os
import datetime

from django.template.loader import get_template
import pexpect
from pexpect import pxssh

from django.template import Context, Template


def run_command(hostname, username, password):
    try:                                                            
        result = ''
        s = pxssh.pxssh()
        s.login (hostname, username, password)
        s.sendline ('uptime')  # run a command
        s.prompt()             # match the prompt
        print (s.before)         # print everything before the prompt.
        result += s.before.decode('utf-8') + '\r\n'
        s.sendline ('ls -l')
        s.prompt()
        print (s.before)
        result += s.before.decode('utf-8') + '\r\n'
        s.sendline ('qsub -b y -cwd sleep 100')
        s.prompt()
        print (s.before)
        result += s.before.decode('utf-8') + '\r\n'
        s.logout()
        return result
    except pxssh.ExceptionPxssh as e:
        print ("pxssh failed on login.")
        print (str(e))
        return 'pxssh failed \r \n %s' + str(e)


def submit_job(job, hostname, username, password,thread_count):
    try:

        try:
            xml_dir = os.path.join(os.path.dirname(job.file_first.path), 'experiments')
            os.mkdir(xml_dir)
            os.system('split_nlogo_experiment %s %s --output_dir %s' % (job.file_first.path, job.experiment_name, xml_dir))
        except:
            print('Split failed')

        netlogo_dir = '/home/%s/netlogo-sge' % username
        # datetime.datetime.now().strftime('%Y-%m-%d')
        run_dir = os.path.join(netlogo_dir, 'job-%s' % job.id, '%d' % job.latest_run)
        output_dir = os.path.join(run_dir, 'output')
        model_filepath = os.path.join(run_dir, os.path.split(job.file_first.path)[1])
        experiment_filepath = os.path.join(run_dir, os.path.split(job.file_second.path)[1])

        s = pxssh.pxssh()
        # login to master node

        s.login(hostname, username, password)
        # create the job's new run directory
        s.sendline('mkdir -p %s' % run_dir)
        # cd to run directory
        s.sendline('cd %s' % run_dir)

        #copy experiment files to server
        for experiment_filename in os.listdir(xml_dir):
            file_path = os.path.join(xml_dir, experiment_filename)
            destination_path = os.path.join(run_dir, experiment_filename)
            copy_file(file_path, destination_path, hostname, username, password)

        experiments_count = len(os.listdir(xml_dir))

        # create output dir
        s.sendline('mkdir -p %s' % output_dir)

        # copy job submit script
        # copy sge script
        context_dict = {
            'experiment_name': job.experiment_name,
            'experiment_count': experiments_count,
        }

        if experiments_count<10:
            job_submit_script = get_script('job-submit.sh', context_dict)
        elif experiments_count<100:
            job_submit_script = get_script('job-submit0010.sh', context_dict)
        elif experiments_count<1000:
            job_submit_script = get_script('job-submit0100.sh', context_dict)
        else:
            job_submit_script = get_script('job-submit1000.sh', context_dict)

        copy_script(s, job_submit_script, 'job-submit.sh')
        s.sendline('chmod +x job-submit.sh')

        # copy sge script
        context_dict = {
            'work_dir': run_dir,
            'simulator_dir': run_dir,
            'netlogo_dir': os.path.join(netlogo_dir, 'netlogo-5.2.1'),
            'simulator_src_dir': run_dir
        }
        sge_script = get_script('sge-script.sh', context_dict)
        copy_script(s, sge_script, 'sge-script.sh')
        s.sendline('chmod +x sge-script.sh')

        # copy run simulator script
        context_dict = {
            'model_file': model_filepath,
            'experiment_file': experiment_filepath,
            'netlogo_dir': os.path.join(netlogo_dir, 'netlogo-5.2.1'),
            'output_dir': output_dir,
            'thread_count': thread_count,
        }
        run_simulator_script = get_script('run-simulator.sh', context_dict)
        copy_script(s, run_simulator_script, 'run-simulator.sh')
        s.sendline('chmod +x run-simulator.sh')

        copy_file(job.file_first.path, model_filepath, hostname, username, password)

        copy_file(job.file_second.path, experiment_filepath, hostname, username, password)

        # split before running the main script

        #s.sendline('split_nlogo_experiment "%s" %s' % (model_filepath, job.experiment_name))
        #s.sendline('ls|grep %s|wc -l' % job.experiment_name)

        s.sendline('source ./job-submit.sh')
        s.logout()

        job.latest_run += 1
        job.save()

        return 'Successfully ran the job'
    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(str(e))
        return 'pxssh failed \r \n %s' + str(e)


def get_script(script_name, context_dict={}):
    template = get_template(script_name)
    context = Context(context_dict)
    return template.render(context)


def copy_file(local_filepath, remote_filepath, hostname, username, password):
    try:
        command = "scp %(localpath)s %(username)s@%(hostname)s:%(remote_path)s" % {
            'localpath': local_filepath,
            'username':username,
            'hostname': hostname,
            'remote_path': remote_filepath
        }

        child_process = pexpect.spawn(command)
        expection = child_process.expect(["password:", pexpect.EOF])

        if expection==0:
            # send password
            child_process.sendline(password)
            child_process.expect(pexpect.EOF)
        elif expection == 1:
                print("Got the key or connection timeout")
                pass
    except Exception as e:
        print("Faild to compy file [%s] to remote host [%s]" % (local_filepath, hostname) )
        print(e)


def copy_script(connection, script, filename):

    connection.sendline("echo '#!/usr/bin/env bash' >> %s" % filename)
    for line in script.split('\n'):
        # if '$dollar' in line:
        #     parts = line.split()
        connection.sendline('echo "%s" >> %s' % (line, filename))

def stop_job(job, hostname, username, password):
    try:

        s = pxssh.pxssh()
        # login to master node

        s.login(hostname, username, password)
        # send killall command
        s.sendline('/opt/c3-4/cexec :1-19 killall -u %s' % username)
        s.logout()

        return 'Successfully stop the job'
    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(str(e))
        return 'pxssh failed \r \n %s' + str(e)
