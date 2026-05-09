# Domain Controller and DNS

*You might ask why we are using DNS?* Think of it like this, if any of your DC failed, what as an adminstrator you would be required to make the configuration of the backup on every machine. Infact, if you logon to the machine and want to fetch any service, what and how you can get all those services from the **Domain Controller**. That is why **DNS**, becuase you don't want any one of the DC failing and then making configurations of the new backup of the servers. 

That is why **Primary DNS** and **Seconday DNS**. DNS would never know if the DC failed, therefore there are two DNS which are to be configured on the machine and therefore those two DNS servers are configured within the organisation.

# What are DNS Zones?

Everytime you make a service call, DNS provides you the required information. DNS therefore has three types of Zones.

1. **Primary DNS**
  - When Domain is created for the first time, it is created using the Primary Zone, it is also a database that is kind of service running on the server.
  - Either it is **Forward Lookup** or **Reverse Lookup**, it would be a part of Primary Zone only.
  - All the services and their IPs are handled here. 
  - Think if this fails, *if the server fails, what you would be doing in that case?*
2. **Secondary DNS**
  - It is the backup copy of the primary zone hosted on the seperate server.
3. **Stub DNS**
  - If you don't want the copy of whoe primary zone then in that case you can create a stub zone, it won't take the whole copy of the primary, instead only the one that is required, not whole.
  - *It only know where to point when there is a required information*, then in that case use stub zone.

This is called Data replication, refer to [Active Directory](../concepts/active-directory.md), and data replication works in two styles, one is push style, another is pull style.

### `dns.conf`

DNS records are updated every period of time, when every there is modification within the zone, the modification of the file will be updated, and the serial number within the file changes and this is how Primary server informs the secondary server.

DNS uses TCP and whenever you do DNS lookup it uses UDP. Becuase everytime there is any change made on the Primary, there is same change seen on the Secondary DNS also. You can also go to Secondary and make them Primary if you know Primary is not going up soon. Then you can go on with the changes that you need to make.

# Forest Functional Level

When you add a forest with Window Server 2016, this forest functional implementation of OS dicides what is going to be the minimum version of the Window OS, which can be configured as **DC** or **ADC** within the entire forest.

Remember if there is another forest, you can set any OS, unitl and unless there is only 

# LDAP (Lightweight Directory Access Protocol)

It follows a directory tree.

| C: | D: | / |
|----|----|---|
| Directory | Directory | Directory |
| ⬇︎  | ⬇︎ | ⬇︎ |
| SubDirectory | SubDirectory | SubDirectory |
| ⬇︎  | ⬇︎ | ⬇︎ |
| Files | Files | Files|


It is called **Directory Access Protocol** called as **X.500**. All the data is stored in some files with information related objects, such as printers, isers and computer. These are stored in files called leaf objects. 

When you say there are two domains within a forest, there are only queries that are to be decided by the **ldap**. It decides what objects permissions that are to be hold.

Remember ldap allows you to create objects such as OUs, Users, and Computer etc. Each object will have some properties for user and every property will have some value. These properties includes username, time restriction, logon to etc. This ldap is also a **schema**, Schema stores the data that has information about the object structure.

**LDAP** server hosts this ldap database , ldap clients perform operations using lsap queries, (Similar to sql query).

LDAP schema is the basic structure of each object and decides the properties of theat object. This ldap schema can be extended by adding and removing properties of an object.

LDAP uses distinguished names to identify any object distinguidhe name of user1. But remember that these distinguished name are stored in such fashion, CN (Comman Name)=user1, OU=sales, OU=pune, DC=cdac, DC=lab.

# Kerberose

It is an authenticatio protocol it procides ticjet based authentication. It provides **Single Sign On (SSO)**. It means user needs to login once same login works on all other computers.

Kerberose server creates a realm which maps to a domain name. ALl decices within this realm accept the tickets issued by the kerberose server. *You might ask, why we are using Kerberose?* It is because, kerberose is through which we are able to make forest boundaries, it allows trust to be created between the kerberose. This allows users form on realm to lgoin to computers in toher realm using the same credentials. 

Remember that both LDAP and kerberose both uses **timestamp** as the limiter. Therefore, time is very important, if the time doesn't match, it query will be rejected.

# How does Kerberose works?

Every DC contains elements such as **KDC**, **TGS**, and **AS**.
It is also called trusted third party communication. When the client sends the 

# FSMO (Flexible Single Master operations) Roles

It consists of two Roles, **Forest-wide** Role and **Domain-wide** Role. Forest wide roles means ther will be only one server in the entire forest performs this role, and another is **Domain-wide** is when there is only one server in each domain will perform these roles.

Lets discuss the roles within the **Forest-wide** Roles:

1. **Schema Master**
  - What Schema master does is it makes sure that active directory schema (ldap schema) is same in the entire forest .
  - Any new domain added in the forest, gets the AD schema from the schema master.
  - Any new updates to AD Schema should be first performed on Schema Master.
  - Then Schema Master will update it to all other domain controllers within a forest.

2. **Domain-naming Master**
  - It makes sure that there isn't any duplicate domains in the forest.

Lets discuss roles within the **Domain-wide** Roles:

1. **RID Master**
  - In a domain as the user account are created on DC and any ADC, ther is a chance that 2 uers get the same SID number. 
  - RID Master takes care of that duplication.
  - The Resource ID master allocated the SID number ot ADC's which they can assign to accounts created on them. This avoids SID duplication.

2. **Infrastructure Master**
  - It performs cross-domain information transfer. It basically communicates with the other domain for the exchange of information.
  - For example, **student1** (of sunbeam.cdac.com) is added to the *acts.cdac.com* by the domain administrator. 

3. **PDC Emulator**
  - It originally used for the backward compatibility with windows NT. It is Primary Domain Controller.
  - Now it works as a time server for the computers within a domain.
  - Also handles usr password changes - communicates other domain user password changes to PDC of that domain.

![alt text](pdc.png)

Now consider the below structure and give the roles that will be assigned to each of the server:

![alt text](roles.png)  

- Remember in case of **Schema Master**, the first domain will be assigned the **Schema Master**. Then, in case of the **Domain-naming Master**, it will be assigned to the same as Schema Master. 

- Thus in case of the srv6, there is no ADC yet created for the domain, so it will have all the domain-wide roles.

Now if you create a new role with only domain, as given below example, it will have all the roles of the forest and domain. Refer to [Day 5](../day5/day5.md) to learn ahead about the **Transfer of roles**.

![alt text](roles-2.png)

### `Netdom query fsmo`

If you look at the `netdom query fsmo` you'll find the RID master and all kinds of roles within it.

Now lets discuss about the infrastructure Master

Here's a detailed explanation of the specified topics related to networking concepts, IPv4/IPv6 addressing, DFS implementation, branch office solutions, and WDS concepts.

# Core & Distributed Network Concepts

### 1. **Software-Defined Networking (SDN)**
- **Definition:** SDN is an approach to network management that enables dynamic, programmatically efficient network configuration to improve network performance and monitoring. It separates the control plane (network management) from the data plane (data forwarding).
- **Benefits:** Centralized management, flexibility in network resource allocation, and automation of network operations.

### 2. **Wide Area Network (WAN)**
- **Definition:** A WAN is a telecommunications network that extends over a large geographic area, connecting multiple Local Area Networks (LANs). It typically involves leased telecommunication lines or satellite links.
- **Usage:** Organizations use WANs to connect branch offices across cities or countries, allowing for data sharing and communication.

### 3. **Local Area Network (LAN)**
- **Definition:** A LAN is a network that connects computers and devices in a limited geographic area, such as a single building or campus. It allows for high-speed data transfer and resource sharing.
- **Characteristics:** Typically owned and managed by a single organization, LANs use Ethernet or Wi-Fi technologies.

### 4. **Virtual Local Area Networks (VLANs)**
- **Definition:** VLANs are used to segment a physical network into multiple logical networks. Devices on the same VLAN can communicate with each other as if they were on the same physical network, regardless of their actual physical location.
- **Benefits:** Improved security, reduced broadcast traffic, and better management of network resources.

## IPv4/IPv6 Addressing and Subnetting

### 1. **IPv4 Addressing**
- **Structure:** IPv4 addresses are 32-bit numerical labels written in decimal format as four octets (e.g., 192.168.1.1).
- **Subnetting:** Dividing an IP address into subnets allows for efficient IP address management and improved network performance. CIDR notation (e.g., /24) is commonly used to denote subnet masks.

### 2. **IPv6 Addressing**
- **Structure:** IPv6 addresses are 128-bit hexadecimal numbers divided into eight groups (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).
- **Transition Technologies:** Techniques such as Dual Stack (running IPv4 and IPv6 simultaneously), Tunneling (encapsulating IPv6 packets within IPv4), and Translation (using NAT64) facilitate the transition from IPv4 to IPv6.

## DFS Implementation

### 1. **DFS Namespaces**
- **Definition:** DFS Namespaces allow administrators to group shared folders located on different servers into a single logical namespace, making it easier for users to access resources.
- **Configuration:** Administrators can create a DFS root that serves as the entry point for users accessing shared folders.

### 2. **DFS Replication**
- **Definition:** DFS Replication is a multi-master replication engine that enables the replication of files across multiple servers.
- **Benefits:** Provides fault tolerance and ensures data consistency across locations.

### 3. **BranchCache**
- **Definition:** BranchCache is a feature that optimizes bandwidth usage by caching content at branch offices, allowing users to access files faster without repeatedly downloading them from headquarters.
- **Deployment Models:** Can be implemented in either distributed cache mode or hosted cache mode.

## Branch Office Solutions

### 1. **Remote Office/Branch Office (ROBO) Solutions**
- These solutions are designed to optimize connectivity and resource access for branch offices that may have limited bandwidth or resources compared to central locations.

### 2. **Optimization Techniques**
- Implementing technologies like WAN optimization, caching solutions, and DirectAccess can enhance performance and reduce latency for remote offices.

## WDS Concepts

### 1. **Windows Deployment Services (WDS)**
- WDS is a server role that allows for the deployment of Windows operating systems over the network using PXE (Preboot Execution Environment).

### 2. **PXE Booting**
- PXE enables client computers to boot from a network interface before booting from local storage devices. This is essential for deploying operating systems in environments without local media.

### 3. **Multicast Deployment**
- Multicast allows multiple clients to receive the same data stream simultaneously during OS deployment, optimizing bandwidth usage by sending one stream instead of multiple unicast streams.

### 4. **Imaging**
- WDS supports capturing and deploying images of Windows operating systems, which can be customized for different hardware configurations.

## Advanced WDS Deployment

### 1. **Multicast Deployment**
- Advanced configurations can leverage multicast for deploying large images efficiently across multiple clients simultaneously.

### 2. **Driver Management**
- WDS allows administrators to manage drivers associated with different hardware models, ensuring that the correct drivers are applied during deployment.

### 3. **Automation**
- Using tools like Windows System Image Manager (WSIM), administrators can automate the deployment process by creating answer files that pre-configure settings during installation.

By understanding these concepts related to networking, addressing, DFS implementation, branch office solutions, and WDS deployment, IT professionals can effectively design and manage robust infrastructure solutions tailored to organizational needs.


# IIS 

Here's a comprehensive overview of the specified topics related to Internet Information Services (IIS), including core concepts, architecture, security, configuration, deployment, management, and troubleshooting.

## IIS Core Concepts

### 1. Websites
- **Definition:** A website in IIS is a collection of web pages and associated resources that are served to users over the internet or an intranet.
- **Configuration:** Each website can have its own settings, including bindings (IP address, port, and hostname), physical path (location of files), and authentication methods.

### 2. Application Pools
- **Definition:** An application pool is a container for one or more websites or applications. It isolates them from other applications on the server.
- **Benefits:** This isolation helps manage resources and improves security; if one application crashes, it does not affect others.

### 3. Virtual Directories
- **Definition:** A virtual directory is a directory that is mapped to a physical directory on the server but does not correspond directly to a URL path.
- **Usage:** It allows administrators to organize content in a way that does not require moving files physically on the server.

## IIS Architecture

- **Request Processing:** IIS uses a request-processing architecture where HTTP.sys listens for incoming requests. When a request is received, it is processed by the Windows Process Activation Service (WAS), which manages application pools and worker processes (w3wp.exe).
- **Modules:** IIS supports various modules that can be added or removed to process requests (e.g., authentication modules, compression modules).
  
## IIS Security

### 1. Authentication
- **Types:**
  - **Anonymous Authentication:** Allows users to access the website without providing credentials.
  - **Windows Authentication:** Uses Windows credentials for user authentication.
  - **Basic and Digest Authentication:** Provide alternative methods for user validation.

### 2. Authorization
- **Role-Based Access Control (RBAC):** Administrators can set permissions based on user roles to restrict access to specific resources.

### 3. SSL/TLS
- **Encryption:** Secure Sockets Layer (SSL) and Transport Layer Security (TLS) are used to encrypt data transmitted between the client and server.
- **Certificates:** SSL certificates must be installed on the server to enable HTTPS connections.

## IIS Configuration

### 1. Bindings
- **Definition:** Bindings define how a website responds to requests based on IP address, port number, and hostname.
- **Configuration Options:** Websites can be configured to listen on multiple bindings for different domains or IP addresses.

### 2. Application Settings
- **Configuration Options:** Settings include .NET CLR version, identity type for application pools, and custom error pages.

### 3. Logging
- **Log File Configuration:** IIS can log requests in various formats (W3C, NCSA). Logs can be configured to capture details such as client IP address, request URL, response status codes, etc.

## IIS Deployment and Management

### Deployment
- **Web Deploy Tool:** A powerful tool for deploying web applications from development environments to production servers.
- **IIS Manager:** The graphical interface used to manage IIS settings, websites, application pools, and security configurations.

### Management
- **Remote Management:** Administrators can manage IIS remotely using IIS Manager or PowerShell commands.
- **Monitoring Tools:** Tools like Performance Monitor and Event Viewer help track server performance and diagnose issues.

## Basic Troubleshooting

1. **Check Event Viewer:**
   - Review logs in Event Viewer for any errors related to IIS or specific applications.

2. **Inspect Log Files:**
   - Analyze IIS log files for unusual patterns or errors that may indicate issues with requests.

3. **Test Connectivity:**
   - Use tools like `ping` or `telnet` to check network connectivity to the server.

4. **Review Application Pool Status:**
   - Ensure that application pools are running and not in a stopped state due to errors.

5. **Use Failed Request Tracing:**
   - Enable tracing for detailed error analysis when requests fail.

By understanding these core concepts and best practices related to IIS, administrators can effectively deploy, manage, secure, and troubleshoot web applications hosted on Windows Server environments.




