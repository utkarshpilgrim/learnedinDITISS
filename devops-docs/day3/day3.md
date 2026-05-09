# ISO OSI Modal

Conceptual model that characterizes and standardizes the communication functions of a telecommunication or computing system without regard to its underlying internal structure and technology.


### Data Link Layer

The Data Link Layer is split into two sublayers, the Logical Link Control (LLC) and Media Access Control (MAC), to provide a modular and adaptable approach to networking. This separation allows for greater flexibility and compatibility across different network technologies.

Here's the logic:

**1. Handling Diverse Hardware (MAC):**  The MAC sublayer deals with the specifics of how data is transmitted and received over the physical medium. Different network hardware (Ethernet, Wi-Fi, Token Ring, etc.) have different methods for accessing the shared medium and avoiding collisions.  By encapsulating these hardware-specific details in the MAC sublayer, the LLC sublayer can remain consistent across different network types. This allows higher-level protocols to operate without needing to know the intricacies of the underlying hardware.

**2. Providing Consistent Services (LLC):** The LLC sublayer provides a standardized interface to the Network Layer, regardless of the MAC sublayer implementation.  It handles functions like flow control, error control (through mechanisms like ARQ - Automatic Repeat reQuest), and addressing (using logical link addresses, sometimes called service access points). This standardization simplifies communication between network devices, as the higher layers only need to interact with the consistent LLC interface.

# Virtualisation

Cloud provides you the way to work with the machine that are not there, Cloud and DevOPS both are apart from each other, DevOPS is like a culture of infrastructure that is followed in IT, but the Cloud is a technology that helps us to connect something that is remote.

Creation of Actual Entrity within the Operating system, that can be used in order to Deloyment, thus adding something virtual, meaning that it is not there actually, but logically it can work. You can use two differnet operating system at the same time, multiple operating system running at the same time. 

# Network Virtualisation

This involves dividing a physical network's bandwidth into multiple virtual channels, each acting as a separate network.  This allows administrators to isolate network traffic, enhance security, and dynamically allocate bandwidth as needed.  Think of it like partitioning a hard drive, but for your network connection. This is especially useful for handling unpredictable usage bursts, ensuring certain applications or users always have the necessary bandwidth.

# Storage Virtualisation

This pools physical storage devices from across a network to create a single, unified storage resource.  This simplifies storage management, improves utilization, and enhances reliability through data redundancy. Applications can access storage without needing to know the physical location or underlying technology. This abstraction simplifies application development and deployment.

#  Data Virtualisation

This focuses on abstracting the technical details of accessing data from various sources. It creates a unified view of data, regardless of its format, location, or underlying API.  This enables applications to access and combine data from multiple sources without dealing with the complexities of each individual source.  Imagine having a single interface to access data from databases, cloud services, and local files, all presented in a consistent format.

# Desktop Virtualisation

This separates the desktop operating system and applications from the physical endpoint device. Users can access their virtual desktops from any device with a network connection, providing flexibility and mobility.  This also simplifies IT management, as desktop images can be centrally managed and deployed.  Zoom, AnyDesk, and Microsoft Remote Desktop are examples of technologies used for desktop virtualization.  Shared hosted desktop virtualization allows multiple users to connect to a shared virtual desktop, optimizing resource utilization.

# Application Virtualisation

**Puppet** and **Ansible** are two of the ways of tdoing th ethings in the actiali IT environment. Similar to desktop virtualization, application virtualization isolates applications from the underlying operating system. This allows applications to be deployed and managed centrally, simplifying updates and patching. It also enables running applications on operating systems they weren't originally designed for.

# Hardware  Virtualisation

This creates virtual machines (VMs) that act like real computers, each with its own operating system and resources. This allows running multiple operating systems simultaneously on a single physical server, maximizing resource utilization and reducing hardware costs. For example, a Windows server could host virtual machines running Linux, allowing you to run Linux-based applications without needing dedicated hardware.

The Sharing of resources such that you are able to manipulate the hardware resources Typically there are two types, one is called Hosted and another is called Bare-Metal Virtualisation.

### Hosted Virtualisation

Hypervisors are used at the op of the Device drivers that manges the inputs being recieved from the Outer Hardware, now that there is hypervisor that is uing the resources, the software that are used for the hypervisor, some example are VMware, Virtual Box, and all. Now what it does is that it creates a Virutal NIC, Virtual Memory, Virtual Audia, and virtual Storage. This kind of Virtualisation is called TYPE II hosted Virtualisation. 

There is Virtual Hardware that is maintained by the Hypervisor, such as VMware and VirtualBox. 

### A Practical Scenario: *Cloud Computing*

Cloud computing heavily relies on all these virtualization techniques.  Network virtualization enables the creation of virtual private clouds (VPCs) and provides isolated network environments for users. Storage virtualization provides scalable and on-demand storage services.  Data virtualization facilitates access to data across various cloud services.  Desktop and application virtualization enable cloud-hosted desktops and applications. Hardware virtualization forms the foundation of cloud infrastructure, allowing cloud providers to offer virtual servers and other resources to their customers.

By combining these virtualization technologies, cloud computing platforms offer flexibility, scalability, cost-effectiveness, and increased efficiency for businesses and individuals.  Imagine easily provisioning virtual servers, scaling resources up or down as needed, accessing data from different sources seamlessly, and providing remote access to desktops and applications – all made possible through the power of virtualization.


### Bare-Metal Virtualisation

The whole infrastructure of the Bare-Metal Virtualisation works on the system called *customised Linux*. This ar multiple Hypervisors that are used in order to make this work, such as XEN, VMware, ESXi. The Hypervisor is directly used over the device Drivers and it removes one more layer of Operating system. Then in that case there is no more resource allocation done by the Operating system itself. Thus, that is called TYPE I Virtualisation.  

# Virtualised Deployment

In real world, you are need to host the application over the AWS and acces the applicaiton over the internet, it means that there is are few terminologies and components.

# Before Cloud 

Earlier people were connected to unix operating system, running on server capable of computing, through the telephone line, on the end people were using a **terminal**, this terminal was connected with the telephone, and copmmand were used to pass the instruction and the inputs were send to the server and outputs were recieved on the papers, as the termials were connected with the Keyboard and Printer.  

Later this got changes to something dfferent, instead of using a terminal thre were used **Modem**, a desktop computing 

This got evolved into Desktop Computing, the computation changes everything, it was called **Desktop Computed Era**. Where every started creating their own data, and with time there came a **Client-Server Architecture**, as this changed everything as people started making their own data, and therefore the server started getting all the data, and data became the talk of theh Generation.

# Client-Server Computing

It is basically associated with the server resolving the client requests for the client re

# Cluster Computing

A scenario where you can include bunch of machiens 

# Cloud Computing

It could be a private network that is handling your requests, it is used over the internet to provide you services, such as creating Virtual Machines, creating Server, deploying application and what not. Having a server might make it vulnerable as if you tried buying 10 such server, if the demand within the coorporation decreases, that would mean loss of resorces.

*So what is cloud computing?* Cloud Computing is the an **On-demand delivery** of an **IT resource** over the internet on **pay as you go** basis. Yes IT resources such as server, engines and all these server could be unsettling and businesses doesn't get ahead of the competition after just installing the MySQL server or any server for example, it is the management and organisation of the data that makes them different, so you can use AWS for deploying and all and focus on the real thing.

## Scalability

*Trade upfront expenses with Variable Expenses.* Meaning everytime you don't have to worry about the Scalability, just few clicks and you can start running you servers and instances. Every application is capable enough to exapand and shrunks the number of resources that you have. This scalability can be used in order to increase or decrease the resources.

## Elasticity

It is the capability of adding the resources and decresing the resources, as you can delete the resources as you don't have to take care of how much you can add or reduce.

## Availablity

This means that you can have the resources because the base requirement of the cloud is for redundant and therefore, you change or reduce


# Management Console

Amazon has group of resoureces where there are multiple functionalities, such as services that AWS provides, so think like this, management console is the way through which you are going to take the services and resources. Thus, then there is CLI (Command Line Interface), which is basically used by the operation team to get those resources in  order to manage the reousrces for multiple programatic services.

Architects uses the Management Console, and Developers uses the SDK, Administrators or say Operation team. Lets start creating our first Virtual Machine running in Cloud. 

# Deployments Modals

There are three deployment modals, Cloud-based deployment, On-premise deployment, and then there is Hybrid deployment.

