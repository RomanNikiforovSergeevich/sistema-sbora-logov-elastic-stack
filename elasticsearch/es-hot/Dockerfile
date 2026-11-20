FROM docker.elastic.co/elasticsearch/elasticsearch:8.13.4
RUN mkdir -p /tmp/es-config && cp -r /usr/share/elasticsearch/config/. /tmp/es-config/
COPY --chown=elasticsearch:elasticsearch elasticsearch.yml /tmp/es-config/elasticsearch.yml
