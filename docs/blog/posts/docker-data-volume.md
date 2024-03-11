---
layout: post
title: "Docker storage"
subtitle: 'Docker data volume'
author: "Ray"
template: blog_post.html
header-style: text
tags:
  - Docker
date: 2020-05-09
---

Quote from docker.com
"Copy-on-write is a strategy of sharing and copying files for maximum efficiency. If a file or directory exists in a lower layer within the image, and another layer (including the writable layer) needs read access to it, it just uses the existing file. The first time another layer needs to modify the file (when building the image or running the container), the file is copied into that layer and modified. This minimizes I/O and the size of each of the subsequent layers. These advantages are explained in more depth below."

COW is low efficiency and thus I/O intensive application will need to mount data volume from host to docker.

Storage volume will help data persistency after docker image removed. Also split data with binary executable.

## Bind mounts
A volume that points to a user specified location on host file system
![bind mount](https://docs.docker.com/storage/images/types-of-mounts-bind.png)
/my/bind/volume  -> (bind)  to host /user/configured/directory

## Docker managed volume
Docker deamon creates managed volumes in a portion of host's file system that owned by docker
`var/lib/docker/vfs/dir/<volume-id>

## Usage: Use `-v` to use volume
* Dockage-managed volume:
  * docker run -it --name bbox1 -v /data busybox
  * docker inspect -f {{.Mounts}} bbox1
    * Inspect bbox1 container volume, volume id and directory in host ([{volume bb23e94e907dc29f3e62deddd332520d34f489177c5bbd5b03a8a75426430a19 /var/lib/docker/volumes/bb23e94e907dc29f3e62deddd332520d34f489177c5bbd5b03a8a75426430a19/_data /data local  true }]
)
* Bind mount volume
  * docker run -it --name bbox2 -v HOSTDIR:VOLUMEDIR  busybox  e.g. `docker run -it --name bbox2 -v /data/volumes/b2:/data  busybox`
  * docker inspect -f {{.Mounts}} bbox2
    * output: `[{bind  /data/volumes/b2 /data   true rprivate}]`

## Share folder and joint container with `-v` and `--volumes-from`
* User case duplicate setup/data:
  * Container A startup and access file/setup F in host.
  * Container B startup and access F through container A
  * Container C startup and access F through container A
  * Container A could stop/pause
* Network duplication
  * Container A startup and startup network network1 and loopback and filesystem
  * Container Nginx started up and use A to access network1 and loopback and nginx setup
  * container tomcat started up and use A to access loopback and tomcat setup
  * container mysql started up and use A to loopback and data volume
  * Application server started up and use A to access loopback


### Instruction example
Startup a infrastructure container infrcon access host folder /data/infracon/volume
`docker run --name infracon -it -v /data/infracon/volume/:/data/web/html busybox`

Startup httpd
`docker run --name httpd --network container:infracon --volumes-from infracon -it bosybox`
