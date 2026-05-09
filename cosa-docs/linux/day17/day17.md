# DNS

DNS is crucial for Active Directory functionality in Windows Server 2016. It's installed automatically with AD DS and serves as the locator service for domain controllers.  Clients and servers use the DNS Client service to resolve computer names to IP addresses and find domain controllers for operations like authentication. Both DNS Server and Client rely on the DNS protocol within TCP/IP's application layer.

For example, when a network user with an Active Directory user account logs in to an Active Directory domain, the DNS Client service queries the DNS server to locate a domain controller for the Active Directory domain. When the DNS server responds to the query and provides the domain controller's IP address to the client, the client contacts the domain controller and the authentication process can begin

# Primary Zone

A primary zone represents the authoritative source of DNS records for a given domain. It's hosted on a designated primary DNS server, which maintains the master copy of the zone file. This file contains all resource records (A, CNAME, MX, etc.) defining the domain's DNS namespace. The primary server is responsible for managing and updating these records.  Administrators directly modify the zone file on the primary server, which then propagates these changes to secondary servers through zone transfers.  The primary server is crucial for maintaining data integrity and consistency within the DNS infrastructure.

We have a primary zone `ns1.example.com`, then secodary zone `ns2.exmaple.com`, and a stub zone for `something.example.com`. Create a primary zone of the primary server using bind server, which will contain all the records for the name servers. But first we need to create a primary zone and then create a zone file that will contain records. 

```
options {
    directory "/var/named";  // Path to zone files
    allow-transfer { none; }; // Restrict zone transfers initially
    // ... other options
};


zone "example.com" IN {
    type master;
    file "example.com.zone"; // Zone file name
    allow-transfer { ns2.example.com; }; // Allow transfers to secondary
};
```

Now all we need to do is create the zone file for the nameservers, though we have taken the example of nameservers but there can be various records for the servers, printers, routers etc.

```
$TTL    86400
@       IN      SOA     ns1.example.com. admin.example.com. (
                                2023102701 ; Serial number (YYYYMMDDXX)
                                3600       ; Refresh
                                1800       ; Retry
                                604800     ; Expire
                                86400 )   ; Negative Cache TTL
; Name servers
        IN      NS      ns1.example.com.
        IN      NS      ns2.example.com.
; Host records (A records)
ns1     IN      A       192.168.1.10  // IP of ns1
ns2     IN      A       192.168.1.20  // IP of ns2
www     IN      A       192.168.1.100 // IP of www.example.com
```

# Secondary Zone

Secondary zones provide redundancy and enhance performance by replicating the primary zone data to other DNS servers.  These secondary servers act as read-only copies, serving DNS queries and reducing the load on the primary server.  Zone transfers, typically using AXFR or IXFR protocols, ensure that secondary servers stay synchronized with the primary server. This mechanism distributes query load, increases availability in case of primary server failure, and reduces latency for clients geographically closer to a secondary server. Secondary zones are essential for building a resilient and scalable DNS infrastructure.

Secondary zone is the zone that allows your server to copy all the zone files from the master server, that is why this is called slave server. All you need to do is create the secondary zone. 

```
options {
    directory "/var/named";
    allow-transfer { none; };
    // ...other options ...
};


zone "example.com" {
    type slave;
    file "slaves/example.com.zone"; // Can be any name; often in a "slaves" directory
    masters { 192.168.1.10; }; // IP of the primary server (ns1)
};
```

The secondary server will automatically download the zone file from the primary server. You don't create it manually.

# Stub Zone

Stub zones offer a streamlined mechanism for resolving names across different DNS namespaces. Instead of replicating an entire zone, a stub zone contains only the necessary information to locate the authoritative name servers for a specific delegated subdomain. This typically includes NS records and glue A records.  When a query for a name within the stub zone's domain is received, the server uses the information in the stub zone to contact the authoritative servers directly, bypassing the iterative query process.  Stub zones reduce DNS traffic, improve resolution speed, and simplify management by centralizing the configuration of referrals to external domains.

The stub zone will container

```
zone "sales.example.com" IN {
    type stub;
    file "stubs/sales.example.com.zone";
    masters { 192.168.10.50; 192.168.10.60; }; // IPs of authoritative servers for sales.example.com
};
```

The stub zone file will contain only NS records for something.example.com, automatically downloaded from the specified master servers.

# Setting up DNS Server

First you need to install the bind and bind-utils, and then you need to go to the named.conf and need to comment the following lines.

```
options{
    // listen-on port 53 .. 
    // listen-on-v6 port 53 .. 
}
```

Now you need to change the `allow-query {localhost; 172.16.164.0/24}`, then you need to add forward zone configuration, so forward zone is used for providing the database information. 

Now you need to go to named.conf file and then you can configure the forward zone and backward zone, this can be done using the following command.

Now we need to update the forward zone and backward zone using the **named-checkconf** is going to contain the forward.

Now you need to add the actual server to the static entry, **/var/named/example.local.db**
.....

Then you need to change the chown, similarly we did in LDAP, because we need to change the default permission for the **system user** running the service. 

Now we need to enable the server and start the service. Go and look into the **status**, you need to check if the service is running successfully.

```
firewall-cmd --add-service dns --permanent
firewall-cmd --relaod
firewall-cmd --
```

Now after configuring you need to do client side configurations, you need to add the resolution ip address inside the resolv.conf.

```
nameserver <ip-address>
```

What is happening is that when we trying to nslookup to the domain name, it is getting fetched from the name server, that is, the server itself. We have had a DNS server. 

# SELinux

SELinux haveSecurity Policy base, it is a kind of database which is collection of policies that secures the files, ports, and entities.   policies contains three things, one is source, another is target, and the permission regarding the source and target. Baically there is server running that enforces those permissions on the source and target. 

# How to configure it?

The first thing you need to do is, taking the password and then you need to.

All the context will end with port number as assigned, we need to attach a context lable and we need to attach on the port. 