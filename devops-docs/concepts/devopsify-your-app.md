# Application

- First have an application or html file.\

# Docker

- Second Create the Dockerfile. 

  ```
  FROM httpd
  COPY index.html /usr/local/apache2/htdocs
  EXPOSE 80
  ```

- Build an image.

  ```
  docker image build -t mywebsite .
  # verify
  docker image ls
  ```
- Now make the account on the hub.docker and push the docker image.

  ```
  # create the docker hub image for that
  docker image tag <image-name> <account-name>/<image-name>

  # push the docker image
  docker image push <account-name>/<image-name>
  ```

# Kubernetes

- Third, you need to go with kubernetes
  - For kubernetes, you need to install minikub, refer to documentation and install.
    ```
    minikube start --driver=qemu --network socket_vmnet
    ```
  - Create a folder with name KBS and within the folder you need to create a file **manifest**, and within that you need to create a yaml file with name *deployment.yaml* and *service.yaml*, you can get the configuration for both the yaml file from the documentation.

    ```
    # deployment.yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx-deployment
      labels:
        app: nginx
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: myapp
      template:
        metadata:
          labels:
            app: myapp
        spec:
          containers:
          - name: myapp
            image: utkarshpratapsingh/myapp
            ports:
            - containerPort: 80
    ```

  - Now create the service.yaml file.

    ```
    # service.yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: myapp
    spec:
      type: Nodeport # to check ifservice is available outside the cluster
      selector:
        app.kubernetes.io/name: myapp 
      ports:
        - protocol: TCP
          port: 80
          targetPort: 80
    ``` 
  - Use the command for listing all the objects created in the cluster.
      ```
      kubectl get all
      ```
  - Use this command to  `kubctl apply -f KBS/manfest/deployment.yaml` do same for service.yaml and check whether it is created or not.

    ```
    kubctl apply -f KBS/manfest/deployment.yaml

    kubctl apply -f KBS/manfest/service.yaml
    ```

  - Check using `kubctl get all` to confirm whether they got created or not. Though you will find that service/myapp will be created, this is the cluster for your application that has provided you with IP and port number. Use the `<ip-address>:<port-number>` that minikub has provided and look for the result over the browser. 

    ```
    minikub ip
    ```  

# What is `kubectl apply` doing?

- if the object/resource is not created, `kubectl apply` creates one and maintains a live kubernetes defination file as well as a **JSON** format file that is used to track the last applied changes,

- whenever the change is found inside the local defination file, it is being checked along with the last configurtion (the json file), and changes are made into the live kubernetes defination file

- the json file exists on the `metadata.annotations` that stores the json itself.

Refer to [Kubernetes Core Conceptes](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get) for documentation on each command such as `kubectl run`, `kubectl create`, `kubectl get`.

# Labels and Selector

Labels and selectors uniquly identifies the respoective pods and using labels and selectors we are able to group multiple pods within the same deployment and therefore 

```bash 
kubectl get pods --selector app=App1
```

<br>
<div style="border-left: 4px solid #007acc; background-color: #f1f6f9; padding: 10px; border-radius: 5px;">
<strong>Note: </strong> Note that labels and selector while defining the replicaset we tend to provide the labels at two different times, our notion is for replicaset to be able to find the pod using <strong>labels</strong>.
</div>
<br>

# Helm

Now the deployment is done, website is deployed, but this kind of deployment can be difficult as we need a better solution to deploy it. We can have a better solution to deploy it using the helm chart. 

- Create a folder where your application is and create a helm.

```
# create directory
mkdir helm && cd helm

# create a helm
helm create myapp-chart
```

- After you've created the helm you'll observer two folders named **template** (delete all the files from the template folders) and another will be **charts**, and two files one will be values.yaml and Chart.yaml, then copy the deployment.yaml and service.yaml file from the manifest folder and copy them to the templates.

- Now we need to make a change in the deplayment.yaml (pod files) so that every change in the file can be tracked and deployed, because this is where we are going to implement the CI/CD pipeline. Include the **`{{ .Values.image.tag }}`** in the image.

```
 image: utkarshpratapsingh/mypythonapp{{ .Values.image.tag }}
```

- Now delete the minikube deployed pod and service.

```bash
#check 
kubectl get all

# delete the pod file 
kubectl delete deploy mywebsite

# delete the service file
kubectl delete service mywebsite
```

- Now we will deploy using the `helm`, the below command will deploy everything inside the **templates** folder that is storing both the files for the deployment. 

```
> helm install mywebsite ./mywebsite-chart
NAME: mywebsite 
LAST DEPLOYED: Tue Dec 24 15:04:15 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
```
 
- Check using `kubectl get all`.

# GitHub Action: Contineous Integration

We have finally deployed our application using helm, now we need to add the Github actions. Github actions needs to be defined using *.github/workflows* file within the root directory of the project. Inside root directory create a yaml file that will define the actions. 

```
name: CI
permissions:
  contents: write

on:
  push:
    branches:
      - main
    paths-ignore:
      - 'helm/**'
      - README.md
  workflow_dispatch:
  schedule:
    - cron: "*/1 * * * *"



jobs:
  push:
    concurrency:
      group: prevent
      cancel-in-progress: true
    runs-on: ubuntu-latest
    timeout-minutes: 2
    steps:
      - name: checkout repository
        uses: actions/checkout@v4

      - name: Setup docker build
        uses: docker/setup-buildx-action@v1

      - name: Login do DockerHub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Build and push
        uses: docker/build-push-action@v6
        with:
          context: .
          file: ./Dockerfile
          push: true
          tags: ${{ secrets.DOCKERHUB_USERNAME }}/mywebapp:${{ github.run_id }}
          platforms: linux/amd64,linux/arm64

  update-helm-chart:
    concurrency:
      group: prevent
      cancel-in-progress: true
    runs-on: ubuntu-latest
    needs: push
    timeout-minutes: 2
    steps:
      - name: checkout repository
        uses: actions/checkout@v4

      - name: Update tag
        run: |
          sed -i 's/tag: .*/tag: "${{github.run_id}}"/' helm/myapp-chart/values.yaml

      - name: Commit and push changes
        run: |
          git config --global user.email "itsutkarshpratapon@gmail.com"
          git config --global user.name "Utkarsh Pratap Singh"
          git add helm/myapp-chart/values.yaml
          git commit -m "Update tag in Helm chart"
          git push
```

- *There is something called **Jobs***, GitHub Actions works on three different levels, oen is **workflow** level, where we are to define triggers, Environment variables and others that are needed within the Jobs, **Jobs** is the next level of GitHub Actions where we start defining our jobs that will be performed, for example Unit Testing, Pushing Image to Docker Hub Registry and Updating the Helm Chart for the next deployment.

- The last two steps involves in the devops is the continous integration and contineous deplyment, where there is no human intervention and therefore,
  - **GitHub Actions** - For Continous integration.
  - **ArgoCD** - For Continous Deployment and ths removes the human intervention.

# Cut down the Human Intervention

Create ArgoCD namespace using kubectl to make your application available outside the cluster.  

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

Wait until all the pods are running, check whether the pods are running, it might take a minute. 

```bash
$ kubectl get pods -n argocd
NAME                                                    READY   STATUS    RESTARTS   AGE
pod/argocd-application-controller-0                     1/1     Running   0          2m15s
pod/argocd-applicationset-controller-56c798b5d7-s8vlv   1/1     Running   0          2m17s
pod/argocd-dex-server-f564c6b7-p9bzv                    1/1     Running   0          2m17s
pod/argocd-notifications-controller-7f5d664cdb-fpqx5    1/1     Running   0          2m17s
pod/argocd-redis-6dc4df875b-gj8r7                       1/1     Running   0          2m16s
pod/argocd-repo-server-9f785dcc5-fwt2t                  1/1     Running   0          2m16s
pod/argocd-server-758655c49f-jvlcc                      1/1     Running   0          2m16s

NAME                                              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
service/argocd-applicationset-controller          ClusterIP   10.102.69.175    <none>        7000/TCP,8080/TCP            2m18s
service/argocd-dex-server                         ClusterIP   10.106.148.180   <none>        5556/TCP,5557/TCP,5558/TCP   2m18s
service/argocd-metrics                            ClusterIP   10.98.84.101     <none>        8082/TCP                     2m17s
service/argocd-notifications-controller-metrics   ClusterIP   10.102.221.217   <none>        9001/TCP                     2m17s
service/argocd-redis                              ClusterIP   10.106.86.221    <none>        6379/TCP                     2m17s
service/argocd-repo-server                        ClusterIP   10.109.214.40    <none>        8081/TCP,8084/TCP            2m17s
service/argocd-server                             ClusterIP   10.107.79.227    <none>        80/TCP,443/TCP               2m17s
service/argocd-server-metrics                     ClusterIP   10.108.87.109    <none>        8083/TCP                     2m17s

NAME                                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/argocd-applicationset-controller   1/1     1            1           2m17s
deployment.apps/argocd-dex-server                  1/1     1            1           2m17s
deployment.apps/argocd-notifications-controller    1/1     1            1           2m17s
deployment.apps/argocd-redis                       1/1     1            1           2m17s
deployment.apps/argocd-repo-server                 1/1     1            1           2m16s
deployment.apps/argocd-server                      1/1     1            1           2m16s

NAME                                                          DESIRED   CURRENT   READY   AGE
replicaset.apps/argocd-applicationset-controller-56c798b5d7   1         1         1       2m17s
replicaset.apps/argocd-dex-server-f564c6b7                    1         1         1       2m17s
replicaset.apps/argocd-notifications-controller-7f5d664cdb    1         1         1       2m17s
replicaset.apps/argocd-redis-6dc4df875b                       1         1         1       2m16s
replicaset.apps/argocd-repo-server-9f785dcc5                  1         1         1       2m16s
replicaset.apps/argocd-server-758655c49f                      1         1         1       2m16s

NAME                                             READY   AGE
statefulset.apps/argocd-application-controller   1/1     2m16s
```

Once all are running, we need to change argocd-server type from *ClusterIP* to *NodePort*. Check argocd-server from the services and edit the *TYPE*.

```bash
$ kubectl get service -n argocd
NAME                                      TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                         AGE
alertmanager-operated                     ClusterIP   None             <none>        9093/TCP,9094/TCP,9094/UDP      16h
kubernetes                                ClusterIP   10.96.0.1        <none>        443/TCP                         16h
mywebapp                                  NodePort    10.106.241.206   <none>        80:31001/TCP                    16h
prometheus-grafana                        ClusterIP   10.102.90.239    <none>        80/TCP                          16h
prometheus-kube-prometheus-alertmanager   ClusterIP   10.110.85.108    <none>        9093/TCP,8080/TCP               16h
prometheus-kube-prometheus-operator       ClusterIP   10.104.202.254   <none>        443/TCP                         16h
prometheus-kube-prometheus-prometheus     NodePort    10.111.52.21     <none>        9090:30299/TCP,8080:32532/TCP   16h
prometheus-kube-state-metrics             ClusterIP   10.106.174.254   <none>        8080/TCP                        16h
prometheus-operated                       ClusterIP   None             <none>        9090/TCP                        16h
prometheus-prometheus-node-exporter       ClusterIP   10.110.197.221   <none>        9100/TCP                        16h

```

Above you'll find all the running services within the Kubernetes cluster that are running the services which are to expose the pods running the application, *official application of ArgoCD*.  

In order to access ArgoCD service, we need to expose the service using NodePort, so that we can access the service outside of the Cluster.  

```bash
kubectl edit service argocd-server -n argocd
```

Change the *type* to NodePort and check for the change using `kubectl get service -n argocd`. Now the argocd-server is running, use `minikube service argocd-server -n argocd` to see the running service. 

You would require a username *admin* and password will be available inside argocd secrets. 

```bash
$ kubectl get secret -n argocd
NAME                          TYPE     DATA   AGE
argocd-initial-admin-secret   Opaque   1      7m42s
argocd-notifications-secret   Opaque   0      8m34s
argocd-redis                  Opaque   1      7m45s
argocd-secret                 Opaque   5      8m34s
```

We need to *access* the secret for the **argocd-initial-admin-secret**, to access the secret for the administrative login, follow the below command.  

```bash
kubectl edit secret argocd-initial-admin-secret -n argocd
```

Copy from the *password* and decode it in Base64. 

```bash
echo <base64-password> | base64 --decode
```

Now log into the argocd user interface with username *admin* and decoded password. Create a new application, enter *application name*, copy the *github* link and it will automatically detect the new commit that was made while the developer creates any change within the code, or commits the changes to the github repository. 

# Prometheus

***K8s doesn't by default exposes those metrics***. In order to collect the metrics of the kubernetes cluster we need a container **kube-state-metric** to actually get information from the cluster. So remember that in order to get those metrics we need a collector container called **kube-state-metric** that needs to be deployed within the cluster to obtain those metrics.

It is the Helm chart that will do everything for us using the kube-prometheus-stack that will manage all the prometheus related infomation using the helm chart, developed by prometheus community.

### Kube-Prometheus-Stack consists of an operator

Kube-prometheus-Stack consists of an operator that will manage the creation/initiation/management/configuration for the instance of our complex application, in our case it is none other than prometheus. 

*What Operator does is*, it is like a controller for the application (prometheus in our case) that extends the API server to do all management, configurtion, and creation stuff. Refer to [Prometheus Operator](https://github.com/prometheus-operator/prometheus-operator) to learn more about it. 

### This Operator has other Custom Resources

What prometheus operator does is it comes with lots of custome resources to the deployment and management of the prometheus instance, meaning it itself manages the APIs that calls the resources, meaning you don't have to manage the APIs to reach out the application and all, prometheus does it all by itself just by creating a Prometheus Resource and then we can customise the custom resources we want to deal with. 

Though there are standard K8s APIs that manages the resources, but prometheus resources offers more custom resources that add more layer to prometheus installation. There is **Alertmanager**, **PrometheusRule**, **AlertmanagerConfig**, **ServiceMonitor**, **PodMonitor**.

# Now we are Installing Helm and Prometheus Chart

Lets get the helm chart deployed, refer to [helm docs](https://helm.sh/docs/intro/install/) to start with the show. To start with make sure that you have the helm installed. 

- Add the Prometheus Community Repo.

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
```

- Then, helm repo update

```bash
helm repo update
```

- Then install the prometheus using helm

```bash
helm install prometheus prometheus-community/kube-prometheus-stack
```

<br>
<div style="border-left: 4px solid #007acc; background-color: #f1f6f9; padding: 10px; border-radius: 5px;">
<strong>Note: </strong> You can also use the <code>helm show values prometheus-community/kube-prometheus-stack</code> to check all those values that you can alter.
</div>
<br>

- If you want to go for modified deployment you can use the following, the values.yml file will be having all the customised changes.

```bash
helm install prometheus <chart-name> -f values.yaml
```

# What Prometheus has created

Start with `kubectl get all` and you'll find two statefulset deployment that are the prometheus and prometheus-alertmanager. 

```bash
vagrant@master:~$ kubectl get all
NAME                                                      READY   STATUS              RESTARTS   AGE
pod/prometheus-grafana-66b47dbc84-j7zzt                   0/3     ContainerCreating   0          18s
pod/prometheus-kube-prometheus-operator-c97f8448f-2n646   0/1     ContainerCreating   0          18s
pod/prometheus-kube-state-metrics-65f864fd45-62njh        0/1     ContainerCreating   0          18s
pod/prometheus-prometheus-node-exporter-mzjhk             1/1     Running             0          18s
pod/prometheus-prometheus-node-exporter-p5q5x             1/1     Running             0          18s

NAME                                              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)             AGE
service/kubernetes                                ClusterIP   10.96.0.1        <none>        443/TCP             7m9s
service/prometheus-grafana                        ClusterIP   10.104.121.57    <none>        80/TCP              19s
service/prometheus-kube-prometheus-alertmanager   ClusterIP   10.106.74.248    <none>        9093/TCP,8080/TCP   19s
service/prometheus-kube-prometheus-operator       ClusterIP   10.110.72.163    <none>        443/TCP             19s
service/prometheus-kube-prometheus-prometheus     ClusterIP   10.108.169.49    <none>        9090/TCP,8080/TCP   19s
service/prometheus-kube-state-metrics             ClusterIP   10.100.215.106   <none>        8080/TCP            19s
service/prometheus-prometheus-node-exporter       ClusterIP   10.99.72.5       <none>        9100/TCP            19s

NAME                                                 DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
daemonset.apps/prometheus-prometheus-node-exporter   2         2         2       2            2           kubernetes.io/os=linux   18s

NAME                                                  READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/prometheus-grafana                    0/1     1            0           18s
deployment.apps/prometheus-kube-prometheus-operator   0/1     1            0           18s
deployment.apps/prometheus-kube-state-metrics         0/1     1            0           18s

NAME                                                            DESIRED   CURRENT   READY   AGE
replicaset.apps/prometheus-grafana-66b47dbc84                   1         1         0       18s
replicaset.apps/prometheus-kube-prometheus-operator-c97f8448f   1         1         0       18s
replicaset.apps/prometheus-kube-state-metrics-65f864fd45        1         1         0       18s
```

Thus, **prometheus-grafana** is one of the deployment that helm downloads for you before hand so that it becomes easy to connect to the prometheus and display the dashboard. 

The **prometheus-kube-prometheus-operator** which manages/initiates/creates the instances that the application intends to, refer to [Kube-Prometheus-Stack consists of an operator](#kube-prometheus-stack-consists-of-an-operator) to learn more about it.

Remember **kube-state-metrics** which is responsible for exposing the metrics to the prometheus, it is present in one of the dpeloyment of the prometheus. 

Make sure you observer **daemonset.apps/prometheus-prometheus-node-exporter**, which is a pod that is created on all the nodes created within the cluster, it is called daemonSet which gets installed on every node in cluster, the node exporter takes all the host metrics, such as cpu and memory utilisation. 

```bash 
vagrant@master:~$ kubectl get statefulset 
NAME                                                   READY   AGE
alertmanager-prometheus-kube-prometheus-alertmanager   1/1     17m
prometheus-prometheus-kube-prometheus-prometheus       1/1     17m
```

Now we are going to look after the `prometheus-prometheus-kube-prometheus-prometheus` statefulset which we will look in next section. 

# `prometheus-prometheus-kube-prometheus-prometheus` has containers 

We have a `init-config-reloader` container under `Init Container` that is reponsible for initilising the initial config of the prometheus, so like that there are containers running that does one thing or another.

Thus, `/etc/prometheus/rules/prometheus-prometheus-kube-prometheus-prometheus-rulefiles-0 from prometheus-prometheus-kube-prometheus-prometheus-rulefiles-0` this is the location of the file that contains all the rules on which prometheus make decisions and managed the change.

Then we can see the secret file, goes something like below.

```bash
kubectl describe secrets prometheus-prometheus-kube-prometheus-prometheus
```

when you describe the secrets as above you get to know the file **prometheus.yaml.gz** where you can store and write the custom changes but when it comes to prometheus, we really don't need to change the file and we can perform all the changes using the kubernetes manifest files. 

```bash
kubectl describe secrets prometheus-prometheus-kube-prometheus-prometheus
```

Then, there is another called relesfiles which is containing the rules of the prometheus. This is containing all the rules file necessary for the prometheus.

```bash
kubectl describe configmap prometheus-prometheus-kube-prometheus-prometheus-rulefiles-0
``` 

# Prometheus Services

Use the `kubectl get services` cmd in order to get services running under prometheus, all these services are running on ClusterIP, but if we need them on NodePort, we can first create the yaml file with `kuebctl get service` cmd as below and then change the type of **NodePort** to access the service outside the cluster.  

```bash
kubectl get service prometheus-kube-prometheus-prometheus -o yaml > service.yaml
```

Then change the type to **NodePort** and apply the changes using the `kubectl apply -f service.yaml` and the service will be updated. 




