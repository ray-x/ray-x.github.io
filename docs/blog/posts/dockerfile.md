---
layout: post
title: "Dockerfile"
subtitle: 'Build your own docker'
author: "Ray"
header-style: text
tags:
  - Docker
date: 2020-05-10
---
We can use 
* storage volume
* `docker exec`, 
* ansible (and similer software) 
* `docker run` with options, 
* container based on container
* etc
 
to build a customized a docker. But with dockerfile it is easy to build a customized docker.


## Share system variable
As discussed early, we can use a infrastructure container to share system variable to other container. (e.g use consul)
and generate configure file based on system variable. e.g. a nginx file in /etc/nginx/conf.d/
```
# server.config

{
  server_name $MY_NGX_SERVER_NAME;
  listen $NGX_IP:$NGX_PORT;
  root $WEB_ROOT;
}
```

## Dockerfile
* Source code for building Docker images. It contains all the comnands to assemble a image
* Use docker build to access dockerfile

#

### Dockerfile format
  * `# Comment`
  * INSTRUCTION arguments
    * Instruction is **NOT** casesensitive, but it is a convention to use UPPERCASE to distinguish them from arguments more easily
  * Docker runs instructions in a Dockerfile in order
  * The first instruction must be `FROM` in order to specify the Base Docker Image from which your are building.

### Docker ignore file  .dockerignore 
Same as .gitignore

### Environment variable and replacement
* env variable (declared with **ENV** statement) can also be used in instructions as variables to be interpreted by Dockerfile
* Env variable are notated in Dockerfile with $variable_name or ${variable_name}
* ${variable_name} support bash modifiers
  * ${var:-word} if var is set, return var value, otherwise return word
  * ${var:+word} if var is set, return word value, otherwise return empty

##
## Dockerfile instructions
### FROM 
  * Need to be first un-comment statement.
  * Base image can be either local image or docker registry (e.g docker hub)
  * Syntax (either)
    * FROM \<repository>[:<tag>] (repository is image name e.g nginx, redis, or ray-x/busybox-httpd)
    * FROM \<repository>@\<digest-hash> 
e.g.
```Dockerfile
FROM busybox:latest
```

#
###  MAINTAINER (depreacted)
  e.g `MAINTAINER "rayxu <rayx@rayx.me>"`

#
### LABELS
  * Usage: `LABEL <key>=<value> [<key>=<value> ...]`
  * The LABEL instruction adds metadata to an image in format of key=value e.g  `MAINTAINER="rayxu <rayx@rayx.me>"`

#
### COPY
  * Syntax:
    *  COPY \<src> [\<src> ...] \<dest>
    *  COPY ["\<src>", ... "\<dest>"]
  * Copies new files or directories from <src> and adds them to the filesystem of the image at the path \<dest>.
  * \<src> may contain wildcards and matching will be done using Go’s filepath.Match rules.
  * \<dest> is an absolute path, or a path relative to WORKDIR.
  * If \<dest> doesn’t exist, it is created along with all missing directories in its path.
  * If space existed in \<src> use "<src>" e.g. "my src folder"

#
### ADD
  ADD is similar to COPY, expects that it can add and unzip compressed file (gz, Z, bz2, zip). It also can fetch files from URL e.g. `ADD http://nginx.org/download/nginx-1.18.0.tar.gz /usr/local/`
  or `nginx-1.18.0.tar.gz /usr/local` (will untar to /usr/local, docker will have /usr/local/nginx-1.18.0)
  * Syntax:
    *  ADD \<src> [\<src> ...] \<dest>
    *  ADD ["\<src>", ... "\<dest>"]
  * Same as COPY 1~5 bullet points
  * to un-compress, \<dest> must not end with **/**
  * If use `ADD ["<src>", ... "<dest>"]` and wildcard existed in src, \<dest> should end with `/` if \<dest> not end with `/` it will be treat as a single file instead of a dir 

#
### WORKDIR
  The WORKDIR instruction sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile. If the WORKDIR doesn’t exist, it will be created even if it’s not used in any subsequent Dockerfile instruction.
  * Syntax:
    *  WORKDIR /path/to/workdir

  * WORKDIR can be used multiple time 
    ```Dockerfile
    WORKDIR /usr
    RUN pwd  #output /usr
    WORKDIR /bin   
    RUN pwd # output /bin
    ```
  * WORKDIR instruction can resolve environment variables 
    ```Dockerfile
    ENV DIRPATH /path
    WORKDIR $DIRPATH/$DIRNAME
    ```

#
### VOLUME
The VOLUME instruction creates a mount point(volume) and marks it as holding externally mounted volumes from native host or other containers. 
* Syntax:
    *  VOLUME \<mountpoint>  e.g. VOLUME /var/log
    *  VOLUME ["\<mountpoint>"]  e.g. VOLUME ["/opt"]
*  VOLUME is used to share folder between Docker and host/other dockers
*  Docker VOLUME is similar to `-v` option in `docker run` command. Difference is that VOLUME does not specify the directory mapping. Normally is uses to gether the logs in container. More specific, VOLUME /var/log will expose the folder to a folder like `/var/lib/docker/volumes/3207....84e4` and docker container will know the mapping. Any logs in /var/log in docker will also appear in `/var/lib/docker/volumes/3207....84e4`

#
### EXPOSE

Specify the port/protocol container listens on at runtime. 
* Syntax:
EXPOSE \<port> [\<port>/\<protocol>...]
* e.g
  
  `EXPOSE 11211/upp 11211/tcp 2 323/tcp`
  `EXPOSE 80` (default tcp)
  Check the port with `docker port image-name`

#
###  ENV
ENV sets the environment variable \<key> to the value \<value>.
Note ENV is set in `docker build` also it will be passed to `docker run`
The ENV setup can be overwrite with `docker run -e <key>=<value>`
* Syntax:
ENV \<key> \<value>
ENV \<key>=\<value> ...

* Refer to the env variable with $variable_name or ${variable_name}
* e.g 
  `ENV myName John Doe` equal to `ENV myName="John Doe"`

  `ENV myName="John Doe" myDog=Rex\ The\ Dog \
    myCat=fluffy`
* To set a value for a single command, use RUN \<key>=\<value> \<command>

#
### RUN
Run the executable in docke durning docker build.
The RUN instruction will execute any commands in a new layer on top of the current image and commit the results. The resulting committed image will be used for the next step in the Dockerfile.

* Syntax
  * RUN \<command> (shell form, /bin/sh -c \<cmd>)
  * RUN  ["executable", "param1", "param2"] (exec form)
* Shell form PID not 1 and can not receive Unix signals
* Usage
  ``` Dockerfile
  ADD http://nginx.org/download/nginx-1.18.0.tar.gz /usr/local/src
  RUN cd /usr/local/src && \
  tar xf nginx-1.18.0.tar.gz
  ```
* exec form does not support shell operator (e.g wildcard, &, >, | etc) to use shell , you need to run `RUN ["/bin/bash", "-c", "<command>", "<argument1>", "<argument2>" ... ]`
* 

#
### nohub, exec
Tp prevent demon stop after shell stops, need to use 
nohub or exec.

Note:
nohub command
exec: replaces the current process image with a new process image. This means it replace 
nohub: no hungup, Run a Command or Shell-Script Even after You Logout


### CMD
The main purpose of a CMD is to provide defaults for an executing container. e.g. buxybox default CMD is /usr/sh, nginx default is nginx 
* Syntax
  * CMD ["executable","param1","param2"] (exec form, this is the preferred form)
  * CMD ["param1","param2"] (as default parameters to ENTRYPOINT)
  * CMD command param1 param2 (shell form)
  * If multipule CMD provided, only the last one is effective
  * To build a busybox httpd, which is correct:
* Pitfull
    * CMD /bin/httpd -f -h ${WEB_ROOT}
    * CMD ["/bin/httpd", "-f", "-h", "${WEB_ROOT}"]
    * CMD ["/bin/sh", "-c", "/bin/httpd", "-f", "-h ${WEB_ROOT}"]
    * CMD ["/bin/sh", "-c", "/bin/httpd", "-f", "-h /opt/data/web"]
  * form 1, you can not enter interative mode with -it, If you need to inspect, need to run `docker exec '/bin/sh'
  * form 2, will not work, ${WEB_ROOT} not found 
  * form 3, will not work, start and then exit(httpd is a backend deamon sh -c httpd will return so PID 1 will exit too, this will stop the container)
  * form 4, will not work, start and then exit(same as above)
#
### ENTRYPOINT
An ENTRYPOINT allows you to configure a container that will run as an executable.
* Syntax
  * ENTRYPOINT ["executable", "param1", "param2"] (exec form)
  * ENTRYPOINT command param1 param2
* Command line arguments to docker run \<image> will be appended after all elements in an exec form ENTRYPOINT, and will override all elements specified using CMD. This allows arguments to be passed to the entry point, i.e., docker run \<image> -d will pass the -d argument to the entry point. You can override the ENTRYPOINT instruction using the docker run --entrypoint flag.
* The shell form prevents any CMD or run command line arguments from being used, but has the disadvantage that your ENTRYPOINT will be started as a subcommand of /bin/sh -c, which does not pass signals. This means that the executable will not be the container’s PID 1 - and will not receive Unix signals - so your executable will not receive a SIGTERM from docker stop \<container>.

* Only the last ENTRYPOINT instruction in the Dockerfile will have an effect.
* `docker run --entrypoint <cmd> <args>` overwrite the ENTRYPOINT in dockerfile
* ENTRYPOINT solve the issue that `CMD ["/bin/sh", "-c", "/bin/httpd", "-f", "-h /opt/data/web"]` has
`ENTRYPOINT /bin/httpd -f =h /opt/data/web` will not exit
* If both CMD and ENTRYPOINT exists, arguments of CMD will be pass to ENTRYPOINT as argument
  ```Dockerfile
  CMD["/bin/httpd", "-f", "-h", "/opt/data/web"]
  ENTRYPOINT /bin/sh -c
  ```
  is eqal to 
  ```Dockerfile
  ENTRYPOINT /bin/sh -c /bin/sh -c /bin/httpd -f -h /opt/data/web
  ```
  ```Dockerfile
  CMD["/bin/httpd", "-f", "-h", "/opt/data/web"]
  ENTRYPOINT ["/bin/sh", "-c"]
  ```
  is eqal to 
  ```Dockerfile
  ENTRYPOINT /bin/sh -c /bin/httpd -f -h /opt/data/web
  ```
if you run `docker run --name bbxhttpd -it -P bbxhttpd:v0.1 "ls /opt"`

"ls /opt" will overwrite `CMD["/bin/httpd", "-f", "-h", "/opt/data/web"]` 

  * Use ENTRYPOINT to set ENV var and start deamon
  
  file: entrypoint.sh
  ``` bash
  #!/bin/sh
  cat >  /etc/nginx/conf.d/www.conf << EOF
  server {
    server_name ${HOSTNAME};
     listen${IP:-0.0.0.0}:${PORT:-80}
    root ${NGX_DOC_ROOT:-/usr/share/nginx/html}
  }
  EOF
  exec "$@"   # PID=1
  ```

  file Dockerfile
  ``` Dockerfile
  FROM nginx:1.18-alpine
  ENV NGX_ROOT="/usr/data/html"
  ADD index.html ${NGX_ROOT}
  ADD entrypoint.sh /bin/
  CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
  ENTRYPOINT ["/bin/entrypoint.sh"]
  ```

  Run:
  ``` bash
  $ docker build -t nginx_demo:v0.1 ./
  $ docker run --name ngx1 --rm -P nginx_demo:v0.1
  ```
  login into docker
  ```bash
  $ docker exec -it ngx1 /bin/sh
  # ps
  PID  USER  TIME  COMMAND
  1    ROOT  0:00  nginx: master proccess /usr/bin/nginx -g daemon off; 
  ```

  You will see nginx started and use ROOT user. That is not good for security reason

  #
  ### USER
  User name for RUN, CMD, ENTRYPOINT
  * Syntax
    * USER \<UID>[:\<GID>]
    * USER \<user>[:\<group>]
  * check /etc/passwd for \<UID> 

#
### HEALTHCHECK
The HEALTHCHECK instruction tells Docker how to test a container to check that it is still working. (e.g. not responding, infinite loop)
Syntax
* HEALTHCHECK [OPTIONS] CMD command  (check container health by running a command inside the container)
  * The options that can appear before CMD are:
    * --interval=DURATION (default: 30s)
    * --timeout=DURATION (default: 30s)
    * --start-period=DURATION (default: 0s)
    * --retries=N (default: 3)
  * Response:
    * 0: success - the container is healthy and ready for use
    * 1: unhealthy - the container is not working correctly
    * 2: reserved - do not use this exit code
* HEALTHCHECK NONE (disable any healthcheck inherited from the base image)
example:
``` Dockerfile
HEALTHCHECK --interval=5m --timeout=5s --start-period = 1m\
  CMD curl -f http://localhost/ || exit 1
```

A more complex example
``` Dockerfile
FROM nginx:1.18-alpine
ENV NGX_ROOT="/usr/data/html"
ADD index.html ${NGX_ROOT}
ADD entrypoint.sh /bin/
EXPOSE 80
HEALTHCHECK --start-period = 3s --interval=10 --timeout=1s CMD wget -O - -q http://{IP:-0.0.0.0}:${PORT:-80}/
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
ENTRYPOINT ["/bin/entrypoint.sh"]
```
The check result will show in console:
``` bash
docker run --name web1 --rm -P -e "PORT=8080" ngx:v0.1
127.0.0.1 - - [10/May/2020:18:11:20 +0000] "GET / HTTP/1.1" 200 32 "-" "Wget" "-"
127.0.0.1 - - [10/May/2020:18:11:23 +0000] "GET / HTTP/1.1" 200 32 "-" "Wget" "-"

```

#
### SHELL
The SHELL instruction allows the default shell used for the shell form of commands to be overridden. The default shell on Linux is ["/bin/sh", "-c"], and on Windows is ["cmd", "/S", "/C"]. The SHELL instruction must be written in JSON form in a Dockerfile.
* Syntax
  * SHELL ["executable", "parameters"]
* Example
  * `SHELL ["powershell", "-command"]`
  * `SHELL ["/usr/bin/zsh", "-c"]`

#
### STOPSIGNAL
sets the system call signal that will be sent to the container to exit.
* Syntex
  * STOPSIGNAL signal

#
### ARG 
The ARG instruction defines a variable that users can pass at build-time to the **builder** with the **docker build** command using the --build-arg <varname>=<value> flag. If a user specifies a build argument that was not defined in the Dockerfile, the build outputs a warning.
This provide a way to use one dockerfile to meet different requirement
* Syntex
  * ARG \<name>[=\<default value>]
  
example:
``` Dockerfile
...

ARG auther="ray-x"
LABEL maintainer="${auther}"
...

```
Use --build-arg to pass the ARG in
`docker build --build-arg auther="ray-x rayx@mail.com"`

#
### ONBUILD
The ONBUILD instruction adds a trigger instruction to be executed at a later time, when the image is used as the base for another build.
The trigger will be executed in the context of the downstream build, as if it had been inserted immediately after the FROM instruction in the downstream Dockerfile.
* Syntax
  * ONBUILD \<INSTRUCTION>
  * ONBUILD can not use in ONBUILD `ONBUILD ONBUILD CMD ["ls"]` is illegal
  * Use onbuild tag for base image has onbuild
  * COPY, ADD may not work....(different context)

e.g. docker nginx1:v0-onbuild
```Dockerfile
...
ONBUILD ADD http://nginx.org/download/nginx-1.18.0.tar.gz /usr/local/src
```

```Dockerfile
FROM nginx1:v0-onbuild

```