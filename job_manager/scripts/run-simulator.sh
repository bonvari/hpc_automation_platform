{% autoescape off %}
date
java -Xmx2048m -Dfile.encoding=UTF-8 -cp NetLogo.jar org.nlogo.headless.Main --model {{ model_file }} --setup-file \$1 --table {{ output_dir }}/\$2 #--threads {{thread_count}
date
{% endautoescape %}
