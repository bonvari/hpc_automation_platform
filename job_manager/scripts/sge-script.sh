{% autoescape off %}
WORK_DIR={{ work_dir }}
SIMULATOR_DIR={{ simulator_dir }}
NETLOGO_DIR={{ netlogo_dir }}
SIMULATOR_SRC_DIR= {{ simulator_src_dir }}
cd \$NETLOGO_DIR
sh \$NETLOGO_DIR/run-simulator.sh $1
exit 0
{% endautoescape %}