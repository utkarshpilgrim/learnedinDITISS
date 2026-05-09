# Infrastructure as a Code (IaC)

Building the infrastructure as code, using Code, meaning we will create the Virtual machine, networks, and storage, and everything else, so when it comes to provisioning we will be using terraform, and for configuration of the infrastructure we will use Ansible. 

Infrastructure requirement can require many components, such as operating system, storage, database connection. These 

It control costs, meaning if the developer needs the number of virtual machine, only those will be created in order to control the cost, and when it comes to code, you can save the code, and use the infrastructure code again, until and unless the dependencies are changed.

In real world there are two paradigm on which deployment can work. 

- Delcarative approach - Just like YAML file that will contain the replicaset, services, and deployment and all we need to do it run the kubectl command which will automatically create the pods.  

- Inperative approach - Imperative appraoch is one where we specify the parameters and this the process is not recommended and therefore we don't use it. Meaning when it comes to real world no one uses the parameters. 


Terrform is a multi cloud paradigm that will help creating the infrastructure meaning we can create the code for multiple platform, meaning when it comes to the AWS, Google cloud, all these cloud platform will give the same exprience. 

Not only it will help in builing infrastructure, but also it will help in scalability, meanig on code will take care of scaling the infrastructure, then again, you don't have to take care or writing the code again. Not only that, but you can also use it in collaboration. 

# Terraform

It has Multi-cloud Support, the same concept, you write a IaC code and can build the infrastructure on all the cloud paltform. 

Terraform is nothe one sole tool, but there is also AWS Cloud Formation, Ansible, and Pulumi, Chef/Puppet, all the tools are the one used for the Automation of the infrastructure process. 

Hashicorp is the organisation that is used for the for building the code, for provisioning of the infrastructure, not the configuration, for configuration you need to use Ansible. Terraform can be used for the following:

- **Execution Plan** - Even if yo are not sure, yo can plan the execution of the infrastructure, you don't have to execute the code directly, you can check first, or say preview the code for your infrastructure.

- **State Management** - Terraform maintains a state file, where you can provisioning as well as deprovisioning, meaning destroying the entire resources, where it maintains a **terraform.tfstate** file that will maintain the state for the infrastructure. 

- **Modules and Packages** - It is used for the reusability and share the componenets to share the consistency and stability. 

Terraform is required to work with multiple Cloud Providers, where HashiCorp has many providers registry and you can use any providers. 

# Terraform Architecture

Terraform Core and Terraform 

- Terraform will not recreate the architecture, meaning if once the infras is created, you can't create another one using the same code. 

- 

# Structure

The Structure starts with terraform blocks, rsources block, data block, all these blocks make up the terraform, all these blocks are necessary to use in order to create a Infras.

### Terraform Block

In order to write the code, you need terraform block, like an entry point block, where we start writing using HashiCorp Configuration Language (HCL), these are enclose using curly braces `{}`. For example,

```terraform

terraform{
    required_version=">=1.0.0"

    required_providers{
        aws={
            source="hashicorp/aws"
            version=">=3.0.0"
        }
    }
}
```

Purpose of Terraform Block, it is basically used fr management of the 

### Provider Blocks

Providers are responsible for the management of resources, such as virtual machine, networks, and databases, all these resources needs to be mentioned, using teh provider block, for example, 

```
provider "aws"{
    region="us-west-2"
    profile="default"
}


provider "azurerm"{
    feature {}
    subscription_id=""
}

```

### Reosurces Block

Once you are done with the provider block, you ned to move ahead with the reosurce block. In terraform, it is a configuration block, which is used for the management of the resources, the components that are involves in the resources block are as follows:

- **\<PROVIDER_TYPE>**
- **\<RESOURCE_NAME>**
- **Configuration Arguments**

```

resource "aws_instance" "can_be_anything" {
    ami="ami-7584332"
}
```

# Commands

### `terraform init`

You need to put the block fo terraform where you need to provide the provider, whatever the provider is mentioned in the terraform block, the first commmand that you need to fire is.

### `terraform validate`

It will validate all the **`*.tf`** file and will execute the plan. 

### `terraform apply`

It is where the changes will be finally executed with the provider, it will depoy the changes and therefore, it will 

### `terraform export`

Import an existing resource into the Terrafrom state, allowing it to be maanged by the terraform.  

### `terraform console`

### `terraform refresh`
### `terraform fmt`
### `terraform plan`

# Ansible

Ansible is written in python and it uses ssh mechanism that connects to the nodes and it acts as the controller, the one where the actual application is installed and it then controls the node from there. This server/controller will control the node using the **push** framework. 

Ansible is different from the Chef/Puppet, where a controller is setup using the chef/puppet server, and it **pulls** the configurations from the Chef/Puppet client, meaning it uses the client-server framework. Ansible is not like this, only one server needs to be configured, in Ansible you don't have to deal with the client and the client configurations are given using the Ansible setup. 

# Ansible Key Features

It is agentless architecture, ansible does not need any kind of agent to be configured on the client machine or target system. It uses SSH to connect to the client. 

Because of Idempotency. It is made of smart script, meaing if you are executing the same script, it won't affect the way system works, meaning it can control and same the unnecessary computing of the packages/scripts that is already executed. 

Ansible is Cross-Platform, meaning it is available for Linux, Windows, and MacOS. Because of its Extensibility, it can be used for provisioning (terraform is preferred for provisioning)

# Ansible Architecture Component

It has a Control Node, the machine is mangee


It has another component, called **Manged Node**, baiscally the managed systems that are being controlled, can be linux, macOS, or Windows. For linux and macOS, Ansible uses SSH, it is basically the the 

It is composed of the **≥Inventry**, collection of managed nodes, it could be static or dynamic.

Ansible can be managed using **Modules**, using modules and package module, which provides you all functinalities such as package manager, which will do various operations such as file operation, deleting the service, and creating the service. 

Ansible uses the Plugins, meaning we will have action plugins, connection plugins, callback plugins. 

**Playbook** is the most important part of the system. 

Facts are used as variables inside the playbook.

**Vault** is like a data store where we are stroing sensitive data. 

# WorkFlow

- **Prepare Inventory**

- **Write the Playbook**, meaning you need to write the playbook, 

- **Create yaml file**

- **Execute playbook**

- **Connect to the managed node**

- **Task exection**

- **Report results**

# Inventory

- **Static Inventory**  

- **Dynamic Inventory**

# Playbook Structure

```
