# Let have an offical talk on PKI

*What it is?* It is ISO authentication frameowrk that uses public key cryptography and the X.509 standard. X.509 standard is one of the ISO 27001 standard that defines what are the fields that are defined in the digital certificate. It is the root of the Certification Authority, it is like DNS, in this case, there are chain of trust that defines who trust whom.

# Basics of Communication

In order to trust the webiste, you need to trust that this is **authentic** identity. Once the certicate is the what confirms the authenticity. That is why there is trust. Everything that is happening behind the scene when you are using the HTTPS, it is taken care by the PKI modal, and PKI is all about Asymmetric key exhange.

<div style="border-left: 4px solid #193497; background-color: #dfaea1; padding: 10px; border-radius: 5px;">
<strong>Note: </strong> It is important to understand that there are two things one is private key and another is public key, why we are using private key, because we want to tell the reciever that we are the only entity who send the data/messge. When we encrypt data using our private key, it can be decrypted using our public key. 

We encrypting data using recievers public key so that it can be decrypted using recievers private key only, ensuring the confidentiality. 

Infact when it comes to exchaning private and public keys, you can't just share the private and public keys, you need to first establish a connection, certificates 
</div>
<br>

# What is Certificate?

It is basically, 

- **An Object and entity**

- **Indentifies 

- **Authorised by authentic authority**


# Entities and Functions

- Certificate Authorities
- Registration Authorities
- Certificates
- Certificates repository
- Certificate revocation system
- Keys
- Timstamping
- Client-side software, and 
- Users

# What is Digital Certificate?

- It is the credential/mechanism used to associate a public key with a collectio of components in a manner that is sufficient to uniquely identify the claimec owner.

- The certificate is created and signed (digital signature) y a trusted third party, which is a Certificate Authority (CA).

- When a CA signs the certificate , it binds the indviduals' identity to the public keu, and the CA takes liability for the authenticity of that individual. 

Similar to DNS, it has the same concept, meaning there can be internal as well as external CA. 

# How Browsers checks the Validation?

Browasser looks for the Certificate Revocation and Certificate Revocation List (CRL) entry for the revoked certificates, meaning those certificates whose private keys are compromised, meanig when it comes to the certificates revokation, those certificategs will be having their entry oisnide teh CRL list. 

The browser will chek fo the *Query OCSP responder server to confirm the current validity of certificates*. The browser is able to get this when the secure connection is requested to the website. 

# Attacks against Cryptography

There are various attacks that keeps on happeing over the mathematics of the cryptogrpahy. 

- **Flaws in mathematics**, meaning there can be various flaws but this is a more research based aspect of security where flaws needs to be configured and noticed contineously.

# Security Attacks & Threats

# Types of Attack

It could be internal and external.

# Denial of Service (DoS, DDoS)

# Symtoms of attacks

# Intruders Types

- There can be **State Sponsored**, meaning that there can be Espionage, disruption, political influences. 

- By gaining control of a CA, they can issue fraudulent certificates for any domain, enabling widespread surveillance and man-in-the-middle attacks. They might use advanced persistent threats (APTs) to infiltrate CA systems.

- They could set up their own fake CAs and try to get their root certificates included in trust stores, although this is difficult with modern operating systems and browsers.

- Then there can be **Script Kiddies**.

# Regular technology but is called Screened-Host Firewalls

![alt text](https://securitywing.com/wp-content/uploads/2012/09/screened-host-firewall.jpg)

It is just another technology that is uses the 

# UTM (Unified Threat Management)

When it comes to unified threat management, it is unified threat management, baiscally it has various components of the security, such as anti-virus, firewalls, DoS feature, MAC spoofing and other fewatures. This is just having all the combined features of the security including firewalls inside an hardware. 

- Basic setup of the UTM, 

# Honeypot

# SIEM/OSSIM

In this section we are going to look at the open source SIEM, that will help us inspect using various security tools. Our **goal** is to inspect and analyze the log that will be generated over the OSSIM running machine, when an attacker will try to login through ssh into the deb1 machine. 

Machine required. One main machine that will run OSSIM, we will set up OSSIM. Another machine deb1, though which an attacker (another machine) will try to login and his log will be generated. 

- **Install OSSIM**. We need minimum 50GB hardisk. Number of CPU cores is 2, number of processors 2. RAM should be minimum 4GB, but ideally there should be 8GB. 

- Start the machine and *wait* till it gets load. Once loaded, you need to start with configuration, enter the default gateway, password and all and carry on with *installation*. 

- Start the web interface on the machine and access it using the following steps?

We need to add the debian machine, using some scans. Go to the **Assets & groups**, select assets, and you'll be able to find the debian machines on the local network. But before that we need to move the debian machine and install the `rsyslog`.

- **Install the rsyslog**,

```
sudo apt-get intall rsyslog
```

- And move to `/etc/ssh/sshd.config` file 

- Uncomment two lines below the **`Logging`** and restart the service.

```
sudo systemctl restart ssh
```

- You should be able to find the **auth.conf** file.

Now we are going to install the **Host-based Intrusion Detection System**, for which we are going to install `osec` but before installing you need to install the following packages. 

```
sudo apt-get install build-essential libevent-dev libpcre2-dev libz-dev libssl-dev ca-certificate libsystemd-dev
```

Next, we need to generate a key to connect the agent and server, for that you need to go to **Environment Detection** > **Agent** > **Add Agent** > Add the IP address of the debian machine. Once the key is generated copy the key or store it somewhere.   

Next, download the **resource file** from the local server and install and extract the file. After that you'll need to run the **install.sh** file. Enter the language, enter the agent, press enter for installing the default path and then enter the IP address of the OSSIM server. After that you need to enter `y/yes` for everything else. 

Once installation of osec will be complete. We need to connect the client/host and the server using that key we generated earlier. Follow the steps ahead.

- Create the file `/var/ossec/queue/rids/sender`.

- Run the command to connect the client to the server. 

```
sudo /var/ossec/bin/manage_agents
```

- It will ask to choose from I and Q. Select I.

- Then paste your key that you extracted earlier. 

- Now you need to start the service, using the following command.

```
sudo /var/osec/bin/ossec-control/ start
```

- Now check if you are able to see the client connected, you need to open the Dashboard inside the **Environment**. 

- Now move to **Analysis**, then **Security Events**, find **REAL-TIME**.

What you need to do on attacker machine, just try doing ssh on the attacker machine. 

```
ssh shuhari@<ip-address>
```


# `iptables` LAB: Blocking Traffic From China

The Purpose of this lab is to block the traffic from china, menaing we'll be setting up a machine that will be assumend as traffic of China, and on our main machine we'll be configuring the iptables for preventing the same traffic. Steps are as follows.

- Install the following dependiencies.

    ```
    sudo apt-get install -y automake ca-certificates gcc libc6-dev libnet-cidr-lite-perl libtext-csv-xs-perl libxtables-dev linux-headers-$(uname -r) make pkg-config unzip whet xz-utils
    ```

- Check for the `which iptables` 

- Then extract the file from the local server. 

```
tar -xf http://192.168.0.52/sw/security_tools/firewall/iptables/xtables-addons-3.26.tar.xz
```

- Move to the folder that we extracted and `./configure`, we need to `make` and perform the `make install`.

```
# Configure
./configure

sudo make 

sudo make install 
```

- The official file for the xtables will be located here, `/usr/local/libexec/xtables-addons/xp-geoip-dl`, move to this location and do `ls -l`.

- Now perform the build using the following cmd.

```
xt-geoip-build

xt-geoip-dl
``` 