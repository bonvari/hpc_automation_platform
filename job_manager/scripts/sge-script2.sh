#!/bin/bash
#\$ -N {{ model_name }}
####\$ -pe mpi 2
#\$ -S /bin/bash
#\$ -V
#\$ -cwd
#\$ -notify
#\$ -o {{ output_dir }}
#\$ -e {{ error_dir }}
####\$ -e /home/gtashakor/netlogo-sge2/outtmp/
#\$ -m e
####\$ -q cluster.q@clus1.hpc.local,cluster.q@clus3.hpc.local,cluster.q@clus4.hpc.local,cluster.q@clus5.hpc.local,cluster.q@clus7.hpc.local,cluster.q@clus8.hpc.local,cluster.q@clus9.hpc.local,cluster.q@clus10.hpc.local

#\$ -q cluster.q@clus1.hpc.local,cluster.q@clus3.hpc.local,cluster.q@clus4.hpc.local,cluster.q@clus5.hpc.local,cluster.q@clus8.hpc.local,cluster.q@clus9.hpc.local
####\$ -l excl
#WORK_DIR=/home/gtashakor/netlogo-sge2/

#SIMULATOR_DIR=/home/gtashakor/netlogo-sge2/

#NETLOGO_DIR=/home/gtashakor/netlogo-sge2/netlogo-5.3.1 = old

WORK_DIR={{ work_dir }}
SIMULATOR_DIR={{ simulator_dir }}
NETLOGO_DIR={{ netlogo_dir }}
SIMULATOR_SRC_DIR= {{ simulator_src_dir }}


echo work=\$WORK_DIR
echo netlogo=\$NETLOGO_DIR
echo error= {{ error_dir }}

#SIMULATOR_SRC_DIR=/home/gtashakor/netlogo-sge2/
# try to remove previous log files content
#date > gtashakor.o
#date > gtashakor.e

#execute
cd \$NETLOGO_DIR
#sh \$NETLOGO_DIR/run-simulator.sh \$1
#sh \$WORK_DIR/{{simulator_name}} \$1 \$2
sh ./{{simulator_name}} \$1 \$2
#move output file

exit 0
