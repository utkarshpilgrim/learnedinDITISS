### WAN Security

Earlier multiple technologies for WAN were in use but die to cloud adoption technologies like SD-WAN came into picture and changed everything. Earlier technologies like Frame Relays, Leased (T1/T2) Lines, ATM (Asynchroneous Transfer Mode) were used. But they are not used more. 

- **MPLS (Multi Protocol Label Switching)** - Now that it is method of 

**WEP (Wireless Equivalency Protocol)** works on the architecture that allows you to connect on the internet same as that of the Access-point. You know that when you are trying to connect the network, you need to connect through the WEP network and provide the passwords.

WEP version1 - Uses TRIP, DES (32 bits)
WEP version2 - Uses Triple DES, AES.

*What is Triple DES?* The text will be encrypted for the three times, once it gets encrypted then again for two more times, the DES is applied three times. *Don't think what needs to be done for security, think what hacker could do.*

*Another is AES.* AES is the most advance system as it composed to 128 bits algorithm.


### GRE Tunnel

Before we get into the technolgy, we need to understand that with standard NAT, there is a problem faced in the industry. Every time you can use Overloading of NAT and expect to have a stable connection as ability to be communicate fromthe outside to the inside isn't possible, therefore to get the better view at the problem, look at problem statement.


**Problem statement** - 

![alt text](gre-tunnel.png)


**Generic Routing Encapsulation** is the method used in the industry in order to add another header, L3 Header, nothing but the network layer header. This header is the one that takes on the entry of Inside global and Outside global, thus, after the header the tunneling provides themedium to carry on the packet to the destination and the at destination **80.1.1.1** is able to recieve that packet, knowing that this is going to be the **171.30.2**.

*How we can do it?* Use the tunneling commands given below to configure the tunnel on router A and Router B:

```
A(config)# ip route 172.16.30.0 255.255.255.0 tunnel0 
A(config)# ip route 172.16.30.0 255.255.255.0 172.16.20.1
A(config)# ip route 172.16.30.0 255.255.255.0 172.16.20.2
A(config)# int tunnel0
A(config-if)# no shut
A(config-if)# ip address 172.16.20.1 255.255.255.0
A(config-if)# tunnel source 75.1.1.1
A(config-if)# tunnel destination 80.1.1.1
A(config-if)# ip mtu 1420
```

The Configuration of the `ip add 172.16.20.1 255.255.255.0` is the tunnel0 configuration.

The last lines of command, `tunnel 75.1.1.1` and `tunnel 80.1.1.1` are to tell the source and destination of the tunnel. And remember for every tunnel you need to create a new tunnel that will pass your frame and data to the destination.

Now you need to configure the path to you ISPs, that can also be internet. Remember that the the line below that specifies the path to the ISP, `ip route 0.0.0.0 0.0.0.0 75.1.1.2` tells the router to the send it the ISPs router, then above that its ISPs routing and all, that will decide the routing path.

```
A(config)# ip route 0.0.0.0 0.0.0.0 75.1.1.2
```

Similarly B's configuration can be written:

```
B(config)# ip route 172.16.10.0 255.255.255.0 tunnel0
B(config)# int tunnel0
no shut
B(config-if)# ip address 172.16.20.2 255.255.255.0
B(config-if)# tunnel source 75.1.1.1
B(config-if)# tunnel destination 80.1.1.1
B(config-if)# no
```

# IPSec 

There are two typese of IP security, one is Tunnel Mode and Transport Mode. When your packet is going through the internet, the packet is basically encrypted with payload. It basically tries to protect the src and dest IP address. 

- When the company choose to go directly to the public servers, then they need Transport Mode 
- When the company choose to be more secure not exposing the servers to the internet or publically accessible, then they need Tunnel Mode. 

Tunnel Mode also hides the data, as there is IP header within the IP header so it is impossible to know whether this is tunneling or the Regular IP header.
 
Let's delve deeper into Internet Key Exchange (IKE) and Pre-Shared Keys (PSKs) within the context of IPsec.

**Internet Key Exchange (IKE)**

IKE is the framework used by IPsec to establish a secure channel for negotiating and managing Security Associations (SAs).  Think of SAs as the blueprints for the secure connection.  They define parameters like encryption algorithms, authentication methods, and key lifetimes.  IKE automates the process of creating and managing these SAs, eliminating the need for manual configuration.

IKE operates in two phases:

* **Phase 1 (IKE SA establishment):** This phase establishes a secure channel between the two communicating parties. It negotiates the parameters for this secure channel, including:
    * **Encryption Algorithm:**  e.g., AES, 3DES
    * **Hash Algorithm:** e.g., SHA-256, MD5
    * **Authentication Method:**  This is where PSKs or digital certificates come into play (more on this below).
    * **Diffie-Hellman (DH) Group:** Used for secure key exchange without actually transmitting the key itself.

* **Phase 2 (IPsec SA establishment):** Once the secure channel is established in Phase 1, Phase 2 negotiates the parameters for the actual IPsec connection used to protect data traffic. This includes:
    * **IPsec Protocol:**  ESP (Encapsulating Security Payload) or AH (Authentication Header)
    * **Encryption Algorithm:**  e.g., AES, 3DES
    * **Hash Algorithm:** e.g., SHA-256, MD5
    * **Security Parameter Index (SPI):** A unique identifier for each SA.

**IKE versions:**  IKEv1 and IKEv2 exist. IKEv2 is generally preferred as it's simpler, more efficient, and supports mobility better.

**Pre-Shared Key (PSK)**

A PSK is a secret key that is shared between the two communicating parties *before* the connection is established.  It's like a password.  In the context of IPsec and IKE, the PSK is used during Phase 1 authentication.  Both sides use the same PSK to prove their identity and derive the encryption keys for the IKE SA.

**PSK Advantages:**

* **Simplicity:**  Easy to configure and implement, especially for smaller networks or site-to-site VPNs.

**PSK Disadvantages:**

* **Scalability:** Managing PSKs becomes difficult in larger networks.  Distributing and updating them securely can be challenging.
* **Security:**  If the PSK is compromised, the entire security of the connection is compromised.

**PSK vs. Digital Certificates**

While PSKs offer simplicity, digital certificates are generally considered more secure, especially for larger and more complex networks.  Certificates provide stronger authentication because they rely on a trusted third party (Certificate Authority) to verify the identity of each communicating party.  They also offer better scalability as they eliminate the need for pre-sharing secret keys.

**How IKE and PSK work together:**

1. **Initiation:** One device initiates the IKE process.
2. **Phase 1 Negotiation:** Both devices exchange proposals for IKE SA parameters, including the authentication method (PSK in this case).
3. **PSK Authentication:** Both devices use the pre-shared key to authenticate each other.  They don't actually exchange the PSK itself, but rather use it to generate unique cryptographic values that prove they both know the secret.
4. **IKE SA Establishment:** Once authenticated, the IKE SA is established, creating a secure channel.
5. **Phase 2 Negotiation:**  The devices negotiate the IPsec SA parameters.
6. **IPsec SA Establishment:**  The IPsec SA is established, and secure data transfer can begin.


**In summary:** IKE provides the framework for establishing secure connections, while PSKs provide a simple method for authentication within that framework. While practical for smaller deployments, PSKs have scalability and security limitations compared to digital certificates.  Understanding these components is crucial for configuring and troubleshooting IPsec VPNs.
