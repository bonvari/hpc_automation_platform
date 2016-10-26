from pexpect import pxssh

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
