{% autoescape off %}
date
java -Xmx768m -Dfile.encoding=UTF-8 -cp NetLogo.jar org.nlogo.headless.Main \\
--model {{ model_file }} \\
--setup-file {{ experiment_file }} \\
--table {{ output_dir }}`date +%N`.csv
##\\
##--threads 1 \\
##--experiment \\$1
date
{% endautoescape %}