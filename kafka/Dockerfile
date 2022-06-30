FROM confluentinc/cp-kafka:5.3.5

ADD create_default_topic.sh .

RUN  apt-get update \
&& apt-get install --force-yes -y net-tools \
&& chmod +x ./create_default_topic.sh

CMD [ "./create_default_topic.sh" ]