---
date: 2020-06-01
---

---
layout: post
title: "connect to kafka cluster with SASL"
subtitle: ["GUI Tools Kafka setup", "kafka 客户端SASL配置"]
author: "Ray"
header-style: text
tags:
  - Docker

---

I found there are two GUI client that can be used to connect to kafka:


# Conductor
I have been used this tool for a while, it do have a nice UI design and lots of features. But I need a professional
licence to use it to connect to kafka.
![Conductor UI](https://www.conduktor.io/uploads/screenshot-topics.png)

# Kafka Tool
Kafka Tool also support SASL.
Please refer to the document here:
[Kafka Tool SASL setup](https://kafkatool.com/documentation/connecting.html)
JAAS Setup ![JAAS Setup](https://kafkatool.com/documentation/sshots/connecting_jaas_config.png)

The JAAS connection string `sasl.jaas.config: org.apache.kafka.common.security.scram.ScramLoginModule required username="your name" password="you password";`


# AKHQ (previously known as KafkaHQ)
Kafka GUI for Apache Kafka to manage topics, topics data, consumers group, schema registry, connect and more...
[Github](https://github.com/tchiotludo/akhq)

![AKHQ](https://github.com/tchiotludo/akhq/raw/dev/docs/assets/images/video.gif)

The simplest way to install the software is using docker `tchiotludo/akhq`

You need to update the application.yml and  run

```Dockerfile
docker run -d \
    -p 8080:8080 \
    -v /tmp/application.yml:/app/application.yml \
    tchiotludo/akhq

```
Here is a example [application.yml](https://github.com/tchiotludo/akhq/blob/dev/application.example.yml)

To setup SASL
Need to chang bootstrap, security, sasl configure:

```yml
akhq:
  server:
    base-path: "" # if behind a reverse proxy, path to akhq without trailing slash (optional). Example: akhq is
                  # behind a reverse proxy with url http://my-server/akhq, set base-path: "/akhq".
                  # Not needed if you're behind a reverse proxy with subdomain http://akhq.my-server/
    access-log: # Access log configuration (optional)
      enabled: true # true by default
      name: org.akhq.log.access # Logger name
      format: "[Date: {}] [Duration: {} ms] [Url: {} {} {}] [Status: {}] [Ip: {}] [Length: {}] [Port: {}]" # Logger format

  # default kafka properties for each clients, available for admin / producer / consumer (optional)
  clients-defaults:
    consumer:
      properties:
        isolation.level: read_committed

  # list of kafka cluster available for akhq
  connections:
    my-cluster-sasl:
      properties:
        bootstrap.servers: "1.236.23.21:9092,3.15.1.12:9092,3.15.16.69:9092"
        security.protocol: SASL_PLAINTEXT
        sasl.mechanism: PLAIN
        sasl.jaas.config: org.apache.kafka.common.security.scram.ScramLoginModule required username="your username" password="your password";

  pagination:
    page-size: 25 # number of elements per page (default : 25)
    threads: 16 # Number of parallel threads to resolve page



```
