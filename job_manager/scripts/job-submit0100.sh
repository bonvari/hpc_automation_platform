{% autoescape off %}
for ((i=0;i<10;i++))
do
qsub sge-script2.sh {{experiment_name}}00\$i.xml
done

for ((i=10;i<100;i++))
do
qsub sge-script2.sh {{experiment_name}}0\$i.xml
done

for ((i=100;i<{{experiment_count}};i++))
do
qsub sge-script2.sh {{experiment_name}}\$i.xml
done
{% endautoescape %}