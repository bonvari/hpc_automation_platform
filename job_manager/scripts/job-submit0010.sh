{% autoescape off %}
for ((i=0;i<10;i++))
do
qsub sge_script2.sh {{experiment_name}}0\$i.xml
done
for ((i=10;i<{{experiment_count}};i++))
do
qsub sge_script2.sh {{experiment_name}}\$i.xml
done
{% endautoescape %}