{% autoescape off %}
for ((i=0;i<{{experiment_count}};i++))
do
qsub sge-script.sh "{{experiment_name}}$i.xml"
done
{% endautoescape %}