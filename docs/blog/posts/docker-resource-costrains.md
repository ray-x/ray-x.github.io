---
layout: post
title: "Limit container resources"
subtitle: ["Set up resource constrains", "容器资源限制"]
author: "Ray"
header-style: text
tags:
  - Docker
date: 2020-05-13
---
By default, a container has no resource constrains and an use as much of resource as kernel scheduler allows. 

We can restraint CPU, Memory and GPU usage for docker

## Memory and OOM
On Linux hosts, if the kernel detects that there is not enough memory to perform important system functions, it throws an OOME, or Out Of Memory Exception, and starts killing processes to free up memory. (Most likely a Java application :-P)
Docker attempts to mitigate these risks by adjusting the OOM priority on the Docker daemon so that it is less likely to be killed than other processes on the system. 

`-oom-score-adj` to adjust the priority 
`--oom-kill-disable`
* -m or --memory=   e.g. -m 32m
* --memory-swap  The amount of memory this container is allowed to swap to disk.  

||||
|----|----|-----|
|--memroy-swap|-m|explain|
|passive S|passive M|Container total space S, RAM: M, swap S-M, if S==M, no SWAP allocated|
|0|positive|swap unset (same as below)| 
|unset|positive M|if swap enabled in host , total swap 2*M|
|-1|positive M |if Host enabled swap, container can use up all swap space|


## CPU
--cpus   how may cpus can be used 0.5 half of a CPU, 1.5 one and a half CPU

e.g 
```Bash
docker run -it --cpus=".5" ubuntu /bin/bash
```