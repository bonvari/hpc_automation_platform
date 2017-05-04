{% autoescape off %}
export WORK_DIR={{ work_dir }}
export SIMULATOR_DIR={{ simulator_dir }}
export NETLOGO_DIR={{ netlogo_dir }}
export SIMULATOR_SRC_DIR= {{ simulator_src_dir }}

start=\$(date +%s.%N)

for ((i=0;i<{{experiment_count}};i++))
do
qsub sge-script2.sh {{experiment_name}}\$i.xml {{experiment_name}}\$i.csv
done

end=\$(date +%s.%N)
runtime=\$(python -c "print(\${end} - \${start},\$start,\$end)")
echo "Runtime was \$runtime"
echo {{experiment_name}} \$runtime >>output.txt



{% endautoescape %}