---
layout: post
title: "Kubernetes introduction"
subtitle: 'introduction to kubernetes'
author: "Ray"
header-style: text
tags:
  - Docker
date: 2020-05-14
---
# What is Kubernetes?
Kubernetes, AkA k8s.Kubernetes, is an Production-Grade Container Orchestration System. It can automating deployment, scaling, and managing containerized applications. 
 
# What Kubernetes can do?
* Service discovery and load balancing
* Storage orchestration (automatically mount a storage system)
* Automated rollouts and rollbacks
* Automatic bin packing
* Self-healing
* Secret and configuration management
* etc
 
# Kubernetes Clusters
![K8S Architecture](https://miro.medium.com/max/1276/1*56l6-yNIXFaNZgofRqPAkA.jpeg)

Master node:

API will access k8s master and k8s will route the request to node.

![Kubernetes cluster with all the components tied together.](https://d33wubrfki0l68.cloudfront.net/7016517375d10c702489167e704dcb99e570df85/7bb53/images/docs/components-of-kubernetes.png))

## API Server
kube-apiserver is a component of the Kubernetes control plane that exposes the Kubernetes API. 

## Scheduler
kube-scheduler control plane component that watches for newly created Pods with no assigned node, and selects a node for them to run on.

## controller and kube-controller-manager
* controller: Control loops that watch the state of your cluster, then make or request changes where needed. Each controller tries to move the current cluster state closer to the desired state.
* Node controller: Monitor nodes. Noticing and responding when nodes go down.
* Endpoints controller: Populates the Endpoints object
* Replication controller: Responsible for maintaining the correct number of pods for every replication controller object in the system.
* Service Account & Token controllers: Create default accounts and API access tokens for new namespaces.

## POD And Nodes
### Pod
Kubernetes created a Pod to host your application instance. A Pod is a Kubernetes abstraction that represents a **group of one or more application containers** (such as Docker or rkt), and some shared resources for those containers. Those resources include:

* Shared storage, as Volumes
* Networking, as a unique cluster IP address
* Information about how to run each container, such as the container image version or specific ports to use
  Pod is a virtual machine to host docker containers/applications
  Pods overview ![Pods overview](https://d33wubrfki0l68.cloudfront.net/fe03f68d8ede9815184852ca2a4fd30325e5d15a/98064/docs/tutorials/kubernetes-basics/public/images/module_03_pods.svg)

Normally, we group containers that logically coupled together in a Pod. But in most case we run a single container in a Pod.

### Node
  A Node is a machine that host Pods.
  ![Node overview](https://d33wubrfki0l68.cloudfront.net/5cb72d407cbe2755e581b6de757e0d81760d5b86/a9df9/docs/tutorials/kubernetes-basics/public/images/module_03_nodes.svg)
  Node can be either virtual machine or physical machine.
  Node is consisted with :
  * kubelet
  * kube-proxy
  * Pods
    * docker(or other container)

### kube-cluster
  A cluster of Nodes

### Labels and Selectors
Labels are key/value pairs that are attached to objects, such as pods.
`key=value`
selector: used to filter pods

### Pod management

#### ReplicationController
Manage and maintain number of Replica of Pod. (Scale up and down )

#### Replica Set
Manage and maintain number of Replica of Pod. (Scale up and down )

#### Deployments
Provides declarative updates for Pods and ReplicaSets.
#### StatefulSets
Workload API object used to manage stateful applications.
#### DeamonSet
ensures that all (or some) Nodes run a copy of a Pod. 
#### Job
A Job creates one or more Pods and ensures that a specified number of them successfully terminate. 
#### Cronjob 
Creates Jobs on a repeating schedule.
#### HPA  (Horizontal Pod Autoscaler)
Horizontal Pod Autoscaler automatically scales the number of pods in a replication controller, deployment, replica set or stateful set based on observed CPU utilization or, metrics. 

#
### Service
An abstract way to expose an application running on a set of Pods as a network service.