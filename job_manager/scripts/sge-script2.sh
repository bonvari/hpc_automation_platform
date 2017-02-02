#!/bin/bash
#\$ -N {{ model_name }}
####\$ -pe mpi 2
#\$ -S /bin/bash
#\$ -cwd
#\$ -notify
#\$ -o {{ output_dir }}
#\$ -e /home/gtashakor/netlogo-sge2/outtmp/
#\$ -m e
####\$ -q cluster.q@clus1.hpc.local,cluster.q@clus3.hpc.local,cluster.q@clus4.hpc.local,cluster.q@clus5.hpc.local,cluster.q@clus7.hpc.local,cluster.q@clus8.hpc.local,cluster.q@clus9.hpc.local,cluster.q@clus10.hpc.local

#\$ -q cluster.q@clus1.hpc.local,cluster.q@clus3.hpc.local,cluster.q@clus4.hpc.local,cluster.q@clus5.hpc.local,cluster.q@clus8.hpc.local,cluster.q@clus9.hpc.local
####\$ -l excl
#WORK_DIR=/home/gtashakor/netlogo-sge2/

#SIMULATOR_DIR=/home/gtashakor/netlogo-sge2/

#NETLOGO_DIR=/home/gtashakor/netlogo-sge2/netlogo-5.2.1

WORK_DIR={{ work_dir }}
SIMULATOR_DIR={{ simulator_dir }}
NETLOGO_DIR={{ netlogo_dir }}
SIMULATOR_SRC_DIR= {{ simulator_src_dir }}

#SIMULATOR_SRC_DIR=/home/gtashakor/netlogo-sge2/
# try to remove previous log files content
#date > gtashakor.o
#date > gtashakor.e

#execute
cd \$NETLOGO_DIR
#sh \$NETLOGO_DIR/run-simulator.sh \$1
sh ./run-simulator.sh \$1
#move output file

exit 0
