{% autoescape off %}


start=\$(date +%s.%N)

for ((i=0;i<10;i++))
do
qsub sge-script2.sh {{experiment_name}}000\$i.xml {{experiment_name}}000\$i.csv
done

for ((i=10;i<100;i++))
do
qsub sge-script2.sh {{experiment_name}}00\$i.xml {{experiment_name}}00\$i.csv
done

for ((i=100;i<1000;i++))
do
qsub sge-script2.sh {{experiment_name}}0\$i.xml {{experiment_name}}0\$i.csv
done

for ((i=1000;i<{{experiment_count}};i++))
do
qsub sge-script2.sh {{experiment_name}}\$i.xml {{experiment_name}}\$i.csv
done
{% endautoescape %}