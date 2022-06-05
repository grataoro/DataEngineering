FROM confluentinc/cp-kafka-connect-base:6.0.0

USER root

# plugins dos conectores 
RUN confluent-hub install --no-prompt debezium/debezium-connector-mysql:1.2.2        
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-elasticsearch:10.0.1
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.0.0

ENV CONNECT_REST_PORT "8083"
ENV CONNECT_GROUP_ID "kafka-connect"
ENV CONNECT_CONFIG_STORAGE_TOPIC "_connect-configs"
ENV CONNECT_OFFSET_STORAGE_TOPIC "_connect-offsets"
ENV CONNECT_STATUS_STORAGE_TOPIC "_connect-status"
ENV CONNECT_KEY_CONVERTER "org.apache.kafka.connect.storage.StringConverter"
ENV CONNECT_VALUE_CONVERTER "org.apache.kafka.connect.json.JsonConverter"
ENV CONNECT_INTERNAL_KEY_CONVERTER "org.apache.kafka.connect.json.JsonConverter"
ENV CONNECT_INTERNAL_VALUE_CONVERTER "org.apache.kafka.connect.json.JsonConverter"
ENV CONNECT_REST_ADVERTISED_HOST_NAME "kafka-connect"
ENV CONNECT_LOG4J_ROOT_LOGLEVEL "INFO"
ENV CONNECT_LOG4J_LOGGERS "org.apache.kafka.connect.runtime.rest=WARN,org.reflections=ERROR"
ENV CONNECT_LOG4J_APPENDER_STDOUT_LAYOUT_CONVERSIONPATTERN: "[%d] %p %X{connector.context}%m (%c:%L)%n"
ENV CONNECT_CONFIG_STORAGE_REPLICATION_FACTOR "1"
ENV CONNECT_OFFSET_STORAGE_REPLICATION_FACTOR "1"
ENV CONNECT_STATUS_STORAGE_REPLICATION_FACTOR "1"
ENV CONNECT_PLUGIN_PATH "/usr/share/java,/usr/share/confluent-hub-components,/data/connect-jars"

#ADD connectors /etc/kafka-connect/connectors

#WORKDIR /etc/kafka-connect/connectors

#RUN chmod +x ./register_connectors.sh

#CMD ["./register_connectors.sh"]