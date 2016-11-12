{% autoescape off %}
for ((i=1;i<=10;i++))
do
qsub sge-script.sh $1
done
{% endautoescape %}