FROM bde2020/spark-base:3.1.2-hadoop3.2

ENV SPARK_HOME /spark
      
WORKDIR /opt/application

COPY ./requirements /opt/requirements

RUN pip3 install -r /opt/requirements/dev.txt