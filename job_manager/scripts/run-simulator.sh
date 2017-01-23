{% autoescape off %}
date
java -Xmx1024m -Dfile.encoding=UTF-8 -cp {{ netlogo_dir }}/NetLogo.jar org.nlogo.headless.Main --model {{ model_file }} --setup-file \$1
date
{% endautoescape %}
