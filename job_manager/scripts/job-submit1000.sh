{% autoescape off %}
for ((i=0;i<10;i++))
do
qsub sge-script.sh {{experiment_name}}000\$i.xml
done

for ((i=10;i<100;i++))
do
qsub sge-script.sh {{experiment_name}}00\$i.xml
done

for ((i=100;i<1000;i++))
do
qsub sge-script.sh {{experiment_name}}0\$i.xml
done

for ((i=1000;i<{{experiment_count}};i++))
do
qsub sge-script.sh {{experiment_name}}\$i.xml
done
{% endautoescape %}