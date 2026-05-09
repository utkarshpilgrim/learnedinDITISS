# Creating pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod1
spec:
  containers:
    - name: container1
      image: httpd
```

# Creating Replica sets

It is used to create the replicas of yor pods, which is used to make the service and application higly available. Understanding structure is important.   

In order to attach multiple pods into a single node, we need to start labeling them, as the label will only tell the pods that they belong to single family. 

# ReplicaSet Behaviour 

Once the replicaset is instructed to create a pod, it first check whether the pod is already creted or not, because in kubernetes, it needs to check if the number of containers created meets the number of replicas running on **type: myapp**, meaning if the pods are already running on the same label, it will only create such that total number of replicas meets the **required** number of pods. 

This is very much in contrast with the containers that are created within the Docker Swarm, meaning you tell the docker swarm to create the container for the image with so and so number of replicas, it will simply create the images, but it won't care about the replicas that are created before with the same image. 

# Difference between ReplicaSet and Deployment

When you are working with replicaset, replicaset is creating all those pods as well as doing load balancing, and thus deleting the replicaset will delete all the pods that replicaset created, but when using deployment, it is the object deployment that itself is the replicaset in order to create the replicas, as well as deployment is directing replicaset in a certain way.

Creating pods using the deployment will tell the replicaset about deploying the pods along with the required replicaset configuration. Once you create the yaml file using the kind deployment, you can only delete the pods by deleting the deployment itself.

```
kubectl delete deploy <deployment-name>
```



# Rollout concept

```
kubectl rollout restart deployment mywebsite
```