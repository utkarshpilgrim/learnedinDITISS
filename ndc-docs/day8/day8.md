# PKI LAB

Create the files, i.e., database files 001-RootCA, 002-SubCA, and 003-tinku.

- Create database, it will ask for password, enter password and in order to look at what XCA you are working look th at bottom of the window. 

- Next, create database for the Subordinate CA. 

- Create the database for Tinki. 

We've created database for all the three. So what we are going to do? 

- We need to export the certificatge file inside the RootCA, we need to create the certificate inside root. (**RootCA.dbx**, **RootCA.crt**)

- Next, for the subCA we are going to process the CSR inside the SubCA that is `.pem` file and another certificate `.crt` file. 
  - 002

- Next, Tinku is will also have a CSR, tinku will be issued with the 
  - 003-001tinku.dbx
  - 003-002tinku.pem
  - 003-003tinku.crt
  - 003-004tinku.pfx


- Now create the private key for root CA, then we will create the certificate and export the certificate to the RootCA path. Remember that we have createed the certificate for the RootCA.

- We can import the Certificate of RootCA to the Tinku, why, because we need to create ethe chain.

- Now we need to create the CSR for the SubCA and we need to export the CSR, we will export it to the subCA path. 

- The CSR we have generated we need to import that CSR insie the root, now we need to sign this vertificate for teh SubCA. 

- Now we need to export this signed certificate that we signed to the subca folder.

- Now Tinku database, we need to import the SUBCA signed certificate for the tinku.

- Now we only have to go with tinku, we need to create teh CSR for the Tinku, meanig we need to vreate the certificate for the Tinku. This we've created the CSR for TINKU.

- Export this CSR for the Tinku in his folder. 

- Now we need to import the CSR inside the SubCA, import the Tinku CSR to the A, create the certificate. 

- Now we need to create the 


# Snort on Linux

- Install the fresh debian machine deb1 and install the pre-requisites.

```
sudo apt-get install -y bison ca-certificates flex gcc libdumbnet-dev libluajit-5.1-dev libnghttp2-dev libpcap-dev libpcre3-dev libssl-dev make opensll wget zlib1g-dev
```

- Now we can maintain the snort src code, by making the directory. Download the src code, amd extract.

```
sudo mkdir -p /usr/src/snort_src

sudo cp <daq-src-file> /usr/src/snort_src
```

- Install daq, it's simple, go to the file and install the source code, `./configure`

- Then, `sudo make`.

- Then, `sudo make install`.

- Run the cmd `sudo ldconfig` to load daq libraries, without this nothing will work. 

- Now we need to install the snort from the source code. But there is a *twist*.
  - `netconfig.h` was the file that was within the path `/usr/include`, but in our machine. Thus include the softlink to the file, this file is inside the `/usr/include/tirpc`, so snort might not be able to see the config file. 
    ```
    sudo ln -s /usr/include/tirpc/netconfig.h /usr/include/
    ```

- Now there are other header files that needs to be moved from `/usr/include/tirpc/rpc/` to `/usr/include/rpc`. There are around 15 to 20 files that needs to moved, *so, werite a shell script*.

```
sudo ln -s /usr/include/
```

- Now download the src code of the snort, using the following cmd.

```
sudo cp <snort-src> /usr/src/snort_src
```

- Now repeat the process, `./configure`, `make`, and `make install`.

- Now your snort is insalled. Run snot in packet capture mode.

```
sudo snort -i ens33
```

- Now you can run snort in IDS mode, but we can't run the snort using the root, therefore we need to create te snort. 

```
# create a user
sudo useradd snort -r -s /usr/sbin/nologin -c SNORT_IDS -g snort

# create three directories
sudo mkdir -p /etc/snort/rules
sudo mkdir /var/log/snort
sudo mkdir /usr/local/lib/snort_dynamicrules
```

Yet the configuration files are not in our `/etc/snort/`, so we need to store the config file, we need to copy some the configuration files from src to destination.

```
sudo cp /usr/src/snort_src/snort-2.9.20/etc/*.conf* /etc/snort/

sudo cp /usr/src/snort_src/snort-2.9.20/etc/*.map /etc/snort/
```

We still need to create three files inside the `/etc/snort/rules/`.

```
sudo touch /etc/snort/rules/{white_list,black_list,local}.rules
```

Now we need to add the permissions.

```
sudo chmod -R 5775 /etc/snort
sudo chmod -R 5775 /var/log/snort
sudo chmod -R 5775 /usr/local/lib/snort_dynamicrules/

sudo chown -R 5775 snort:snort /etc/snort
sudo chown -R 5775 snort:snort /var/log/snort
sudo chown -R 5775 snort:snort /usr/local/lib/snort_dynamicrules/
```

Next, we need to make inside the `/etc/snort/snort.conf` file.

```
# change 1
var 

# change 2
var WHITE_LIST_PATH /etc/snort/rules
var BLACK_LIST_PATH /etc/snort/rules
```

Go to `Step #7` and add the following rules.

```
include $RULE_PATH/local.rules
include $RULE_PATH/white_list.rules
include $RULE_PATH/black_list.rules
```

Now run the cmd to run the snort. 
```
sudo snort -T -c /etc/snort/snort.conf
```

Now move to snort rules. 

```
sudo nano /etc/snort/rules/local.rules
```

Add the rule to it. 

```
alert ip any any -> any any (msg: "IP Packet Detected"; sid: 100001;)
```
Now we can finally run the snort.

```
sudo snort -i ens33 -u snort -g snort -c /etc/snort/snort.conf -A console
```

# Fail2ban LAB

```
sudo apt-get install -y iptables python3-systemd fail2ban
```

```
fail2ban-server --version
```

```
sudo systemctl status fail2ban
```

```
# main configuration file
ls -l /etc/fail2ban/jail.conf

# but we create a override file
sudo nano /etc/faile2ban/jail.local
```

```
[sshd]
backend=systemd
enabled=true
port=22
filter=sshd
maxretry=3
bantime=3600
findtime=600
```

```
sudo systemctl status fail2ban
sudo systemctl restart fail2ban
```

```
sudo fail2ban-client status

sudo fail2ban-client status sshd
```

```
iptables -L
```

### Doing attack

```
ssh shihari@<ip-address>
```

Attempt for wrong password. After you will be able to perform wrong attempts on the machine, and server will block the IP address and will update the iptables. Basically it is preventing that IP that violated the `maxretry=3` and will block the IP for a time.

# Next-gneration firewall (NGFW)

- Part of the third-generation firewall technology.

- Combine traditional firewall with other netwwork device filtering functinoalituies , such as :

  - in-line deep packet inspection (DPI)
  - an intrusion prevention system (IPS)
  - TLS/SSL encrypted traffic inspection
  - website filtering
  - QoS/bandwidth management
  - antivirus inspection
  - third-party identity management integration (i.e LDAP, RADIUS, Active Directory), etc. You can integrate these firewalls with the concepts like Active Directory, say a org running the AD can implement firewalls within their AD database. 

- Palo Alto Networks, Fortinet, Check Point, Cisco Firepower. All these are called Next-genration firewalls. 

- Focuses on Deep packet inspection (DPI), application awareness and control, intrusion prevention system (IPS) functionality, user identity integration, advanced malware detection.

- ALthough they offer more features and granular control over the application and access control but they have few **disadvantages**, meaning they can be costlier and hard to configure, they also consume huge amount of resources and therefore can affect the performance.

# Split Tunnel and Full Tunnel VPN

There is differnce between split tunneling where the traffic that is meant for the VPN or the virtual network that you are connected will go via that a seperate tunnel whereas all the external traffic will take the normal path, thus the dst IP will decide which interface is to used in order to send the traffic. 

Whereas the full tunnel will not differentiate between the networks, meaning it won't devide the interface based on the dst IP, if the traffic is meant to go via the VPN server. 

# Strong Authentication

Stong Authentication involves the MFA, such that compromised method can't compromise other methods of authentication.

# FIDO (Fast Identity Online)

Again!

# Deligated Authorization

Delegated authentication is a process where a service (the relying party) trusts another service (the identity provider) to authenticate users on its behalf, meaning instead of handling user authentication itself, the relying party delegates this responsibility to the identity provider. This allows users to access multiple services using a single set of credentials managed by the identity provider. The key benefit is simplified user management and a single sign-on (SSO) experience.

- **OAuth** - Primarily an *authorization* framework. It enables a client application (e.g., a mobile app) to access resources on a resource server (e.g., a web API) on behalf of a user without sharing the user's credentials (username/password) with the client.

- **OpenID** - This sits over the OAuth, basically an *authentication* layer over the OAuth. It extends OAuth by adding an identity layer, allowing the client application to verify the user's identity and obtain basic profile information.


**Technical Differences:**

| Feature          | OAuth 2.0                               | OpenID Connect (OIDC)                          |
|-----------------|-------------------------------------------|-----------------------------------------------|
| **Primary Goal** | Authorization (access to resources)       | Authentication (verify user identity)           |
| **Identity**     | Does not provide user identity information | Provides user identity information (ID Token) |
| **Scope**       | Defines the permissions requested by the client | Includes `openid` scope to request authentication |
| **ID Token**     | Not present                              | JSON Web Token (JWT) containing user information |
| **Endpoints**   | Authorization endpoint, token endpoint     | Additional endpoints (e.g., userinfo endpoint) |

<br>

# LAB: 

- **deb1** - This machine needs to be given the network of 192.168.80.X network.

- **deb2** - Enable IP forwading to the make the deb1 and deb2  communicate with each other, meaning 

```
# Setting ip-forwarding
cat /proc/sys/net/ipv4/ip-forwarding

# 

```

- **deb3** - This machine needs to be given the network of 192.168.50.X. This means when we'll be recieving the packets, we'll be getting the SOURCE IP of the 
