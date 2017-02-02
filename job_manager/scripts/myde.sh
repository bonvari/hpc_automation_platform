#!/bin/bash
#$ -N dengue
####$ -pe mpi 2
#$ -S /bin/bash
#$ -cwd
#$ -notify
#$ -o /home/gtashakor/dengue-sge/outtmp/
#$ -e /home/gtashakor/dengue-sge/outtmp/
#$ -m e
####$ -q cluster.q@clus1.hpc.local,cluster.q@clus3.hpc.local,cluster.q@clus4.hpc.local,cluster.q@clus5.hpc.local,cluster.q@clus7.hpc.local,cluster.q@clus8.hpc.local,cluster.q@clus9.hpc.local,cluster.q@clus10.hpc
.local

#$ -q cluster.q@clus1.hpc.local,cluster.q@clus3.hpc.local,cluster.q@clus4.hpc.local,cluster.q@clus5.hpc.local,cluster.q@clus7.hpc.local,cluster.q@clus8.hpc.local,cluster.q@clus9.hpc.local
####$ -l excl
WORK_DIR=/home/gtashakor/dengue-sge/netlogo-sge

SIMULATOR_DIR=/home/gtashakor/dengue-sge/netlogo-sge/

NETLOGO_DIR=/home/gtashakor/dengue-sge/netlogo-5.2.1

SIMULATOR_SRC_DIR=/home/gtashakor/dengue-sge/
# try to remove previous log files content
#date > gtashakor.o
#date > gtashakor.e

#execute
cd $NETLOGO_DIR
sh $NETLOGO_DIR/d.sh
#move output file

exit 0
