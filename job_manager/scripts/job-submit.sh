{% autoescape off %}
export WORK_DIR={{ work_dir }}
export SIMULATOR_DIR={{ simulator_dir }}
export NETLOGO_DIR={{ netlogo_dir }}
export SIMULATOR_SRC_DIR= {{ simulator_src_dir }}

for ((i=0;i<{{experiment_count}};i++))
do
qsub sge-script2.sh {{experiment_name}}\$i.xml {{experiment_name}}\$i.csv
done
{% endautoescape %}