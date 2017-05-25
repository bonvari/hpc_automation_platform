{% autoescape off %}
startp=\$(date +%s.%N)

date
#####java -Xmx2048m -Dfile.encoding=UTF-8 -cp NetLogo.jar org.nlogo.headless.Main --model {{ model_file }} --setup-file {{ work_dir }}/\$1 --table {{ output_dir }}/\$2 #--threads {{thread_count}
java -Xmx2048m -XX:MaxPermSize=512m -Xms512m -Dfile.encoding=UTF-8 -Djava.util.prefs.userRoot={{ java_root }} -classpath NetLogo.jar org.nlogo.headless.Main --model {{ model_file }} --setup-file {{ work_dir }}/\$1 --table {{ output_dir }}/\$2 #--threads {{thread_count}
date

endp=\$(date +%s.%N)

runtime=\$(python -c "print(\${endp} - \${startp})")
echo "Partial Runtime \$1: \$runtime" >> {{output_dir}}/\$1.txt

{% endautoescape %}
