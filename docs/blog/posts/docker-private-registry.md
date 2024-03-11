---
layout: post
title: "Build private docker registry"
subtitle: "use docker distribution"
author: "Ray"
header-style: text
tags:
  - Docker
date: 2020-05-12
---
If you do not want publish your docker to public registry(e.g. dockerhub, aws, aliyun etc). You can use a local/private registry.
Docker provide docker registry(which is is a docker image)

A good reference by digital ocean [how to set up a private  docker reigstry on ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-private-docker-registry-on-ubuntu-18-04)
And [Deploy a registry server](https://docs.docker.com/registry/deploying/)

## Publish image to private registry
Note: need a https server, or 
add `"insecure-registries":[true]`
in /etc/docker/demon.json

```bash
docker tag mydocker:v0.1-11 private.docker.domain.name.com:5000/mydocker:v0.3-11
docker push private.docker.domain.name.com:5000/mydocker:v0.3-11
```

#
## Harbor
Trusted cloud native repository for Kubernetes
Installation:
[How To Install Harbor Docker Image Registry on CentOS / Debian / Ubuntu] (https://sxi.io/how-to-install-harbor-docker-image-registry-on-centos-debian-ubuntu/)

![Harbor login](https://sxi.io/wp-content/uploads/2019/09/img_5d909b9c725c6.png)

![Harbor projects](https://sxi.io/wp-content/uploads/2019/09/img_5d909b9f87ea4.png)