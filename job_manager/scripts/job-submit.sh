{% autoescape off %}
for ((i=0;i<{{experiment_count}};i++))
do
qsub sge-script2.sh {{experiment_name}}\$i.xml
done
{% endautoescape %}