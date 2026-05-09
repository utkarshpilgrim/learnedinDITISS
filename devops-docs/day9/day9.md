# Building Pipeline

Understanding the flow, get to know how things work here.

- First, build the image, run container, then tag the image to the hub.docker.com and then push the image to the docker account. 

- Once done, create the service for the image with replica.

```
docker service create --name backend --replicas 5 -p 4000:4000 utkarshpratapsingh/myflaskapp
```

- Now create the helm chart. Remove the all the default templates file, only two files should be there, charts.yaml and values.yaml. Clean you values.yaml files. 

```
helm create backend-chart
```

- Create the deployment.yaml file inside the template file. Refer to [deployment.yaml](deployment.yaml) and [service.yaml](service.yaml) file to import the file. 

- Once done with the helm folder, go to the root of the directory and execute the helm install command.

```
helm install backend ./backend-chart
```
  
# CI

Setting up the pipeline, it is nothing but where we setup the sequence of starges. Lets get with CI (Contineous Integration), bring all the clubbing all different parts of the application. Everything builds together to make a package, deployable package. 

- It is the practise of making the code commit, merging the branches together to main branch, thus main branch is where all the codes are accumulated, bug-free, crash-free, and well tested. 

CI pipeline involves three stages that make a complete CI pipeline, this is called **artifact**. It basically involves certain steps as below:

### SCM (Source Code Management)

* **Purpose:**  This stage retrieves the source code from a version control system (like Git). It represents the starting point of the CI pipeline.  The trigger for the CI pipeline is typically a change in the source code repository (e.g., a commit, a merge, or a pull request).
* **Actions:** `git clone` or `checkout`, fetching updates, and potentially tagging the commit for traceability.
* **Output:**  A working copy of the source code on the CI server.

### Build
* **Purpose:**  This stage compiles the source code, packages dependencies, and generates the build artifacts. The specific build steps depend on the programming language, framework, and build tools used.
* **Actions:** Compiling code (e.g., `javac`, `gcc`), running build tools (e.g., `make`, `Maven`, `Gradle`), packaging dependencies, and creating executable files, libraries, or other build outputs.
* **Output:**  The compiled code, packaged application, or other build artifacts.  This is often a deployable package (e.g., a JAR file, a WAR file, a Docker image).

### Test

* **Purpose:** This stage runs automated tests to verify the quality and correctness of the build. This can include unit tests, integration tests, end-to-end tests, and other types of tests.
* **Actions:** Executing test suites using testing frameworks (e.g., JUnit, pytest, Selenium), generating test reports, and potentially performing code analysis or static checks.
* **Output:** Test results, code coverage reports, and other quality metrics.  The success or failure of this stage often determines whether the pipeline proceeds to further stages (like deployment).

*What are artifacts?* A compiled executable, a JAR/WAR file, a Docker image, or any other deployable package. The artifact represents a stable and versioned snapshot of your application at a specific point in time. It serves as the input for subsequent stages in the CI/CD pipeline, such as deployment, staging, or release.

# CD: Contineous Delivery

This is where you will create the environment, where configuration of the environment is set, this is one of the aspets of infrastructure provisioning. Infrastructure is configured using multiple tools. 

### Infrastructure Provisioning 

Terraform, Cloud Formation (AWS), and Vagrant. Infrastructure is created, such as creating the virtual machines, containers, nodes, and networks. Infrastructure provisioning is where  

### Infrastructure Configuration 

Thus, infrastructure configuration using tools such as Ansible, Puppet, and SaltSnack. 


# CD: Contineous Deployment

This is automation is driven by series of testing environment and system pushes the software directly to the deployable environment.  

# Jenkins

Jenkins is called Pipelin as a Code, meaning all the actions and steps can be accomplished using the code, the code is written in **Groovy**, the domain specific language that can be used as scripted pipeline in order ot establish the infrastructure. 

Microservices can be built using multiple technologies, there can be Java used in one service and another serivce can be built using python, in that case it could be hard enough to make it work. Jenkins supports cluster architecture that can provide that platform in order to establish one.

Jennkins follows a cluster architecture, that allows the multiple machiens to be viual machine, physical machien, or any dockes container, or say any pod in kubernetes. Though the machines can be either master or worker, but in Jenkins the master will be responsible foe executing the jobs, and similar to workers, agents are used in order to execute job. 

# Installation 

We will install Jenkins on Fedora machine using the following commands. 

```bash
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
sudo dnf upgrade
# Add required dependencies for the jenkins package
sudo dnf install fontconfig java-17-openjdk
sudo dnf install jenkins
sudo systemctl daemon-reload
```

Enable the service of Jenkins using the following commands.

```bash
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
```

Add firewall rule to access the Jenkins dashboard outside of the fedora virtual machine.

```bash
firewall-cmd --add-port=8080/tcp --permanent
firewall-cmd --reload
```

Because Jenkins uses 8080 port by default, we need to open the services on port 8080. 

# Jenkins Dashboard Overview

Start by copying the password form the path `cat /var/lib/jenkins/secrets/initialAdminPassword`, and wait until it gets loaded after selecting the normal installation. 

Create a freestyle job, provide a name and the start with **Execute Shell**, where you are in control of the linux machine, the default directory of the job is saved inside the location `/var/lib/jenkins/workspace/` where you'll find the directory with the job name. 

<br>
<div style="border-left: 4px solid #007acc; background-color: #f1f6f9; padding: 10px; border-radius: 5px;">
<strong>Note: </strong> You might face a problem where you will recieve the error for <strong>built-in Node</strong>, thus the built-in node problem can be solved by changing the settings inside the threshold free space, where you need to specify 0 for all the Gibs, meaning 0 Gibs. 
</div>
<br>

You can execute **bash scripts** using the Execute Shells, where you can run scripts and therefore you can create scripts and run the scripts using Jenkins. 

You can build using the parameters, where you can create parameters, where configure the build using **Build with Parametres**, you can then use the scripts in the execute shell, before running the build, jenkins will ask for the confirmation for given parameters. 

You can also execute the cron jobs using **Build Periodically**, which will execute the shell script periodically. You need to execute the shell periodically. 

# Working with GitHub

You can pull from GitHub in order to execute and clone the repo on the server. Make sure that you've installed github on the server, otherwise Jenkins won't be able to connect with your github repo. Now, once you enter the github repo in the Git, everytime you'll build, it will fetch the githu b repository from the GitHub and you can inspect the result inside **Console Output**. 

# Auto GitHub Pulling

In order to automate the process of pulling changes from the GitHib, use **Poll SCM**. Specify the time period of the scheduler, where with every change the Jenkins will automatically create the build in the specified cron job, and will pull the changes to the server. 

# Email Notification from Jenkins

Go to **System Global Configuration** and scroll to the bottom where you'll find email notification, you need to add smtp server as *smtp.gmail.com*, smtp port *465* and enable SSL, add gmail id in username and for password generate the **app password** from the gmail settings, use this app password as password in jenkins. 

Test the email notification and start with the build and you'll be able to send email notification for the failed builds.  

# Working on Remote Server

Install the **Publish on SSH** plugin if you want to send the files over ssh to the remote server. In order to achieve the result you also need to establish password less login on the remote servers. 

```bash
# on fedora01
> ssh-keygen

# send the private key to remote server
> ssh-copy-id tvisha@172.16.164.161
```

Check whether password-less login is working or not. Now start with Jenkins, check for the installed Publish on SSH plugin in system global configuration, copy private key from main fedora server and paste in private key column on Jenkins, specify the user that you are using for ssh login on remote server, specify IP address and save. 

Now we need to create the Job, create the job, select **Send files or execute commands over SSH** from build setup, and enter the filename that you want to send, say if you are sending a bash script over the ssh, you can execute the bash scripting using the command `bash myremotefile.sh` in Execute Command.  

# Ansible Plugin 


