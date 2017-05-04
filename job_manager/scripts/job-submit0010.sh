{% autoescape off %}

start=\$(date +%s.%N)

for ((i=0;i<10;i++))
do
qsub sge-script2.sh {{experiment_name}}0\$i.xml {{experiment_name}}0\$i.csv
done
for ((i=10;i<{{experiment_count}};i++))
do
qsub sge-script2.sh {{experiment_name}}\$i.xml {{experiment_name}}\$i.csv
done

end=\$(date +%s.%N)
runtime=\$(python -c "print(\${end} - \${start},\$start,\$end)")
echo "Runtime was \$runtime"
echo {{experiment_name}} \$runtime >>output.txt

{% endautoescape %}