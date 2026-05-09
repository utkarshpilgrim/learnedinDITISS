# Securing Email Communication

You need to setup the mail server, you need to configure a email client. Two user certificate are to be formed for secure communication, these certificates will be used for the trasfer of the mails via MUA (mail user agent). 

- **userone**

  - 004-001-DB-one.dbx
  - 004-002-CSR-one.pem
  - 004-033-CRT-one.crt
  - 004-004-CRT_CHAIN_KEY-one.pfx

- **usertwo**
  
  - 005-001-two.dbx
  - 005-002-CSR-two.pem
  - 005-003-CRT-two.crt
  - 005-004-CRT_CHAIN_KEY-two.dbx


In reality the root CA is not needed, only the certifcates are inportant for he communication. So we are only going to do that. 

- Create the new database for the **userone**, where we are going to create the userone daabase. Create the certificate for the uer, and here in command name you need to put the same email that uyou privoded to the MUA. 

- Digital signature, noo repudiation, key Enshipment, Data Enshipment. Make sure to check inside the certificate. 

# Prerouting chain


# Snort Service Decomposition

Snort is performing two jobs, one of frisking and another of parsing, meaning it is inspecting in binary (all the data that it is capturing) and another is parsing which is converting it to the human readable format. This is not very efficient and effective when it comes to the performance. 

Therefore, we will install another tool **Barnyard** which will take all the input that is generated using the Snort and it will trasnfer all of it to the Barnyard whih will convert the data in huiman readable format. 

Let get into the basic configuration of the snort-barnyard configuration. So lets start with the basic prerequisites of the installing certains packages and libs. 

```
sudo apt-get install -y autoconf automake default-libmysqlclient-dev dos2unix libmariadb-dev-compat libmariadbd-dev libtool mariadb-client mariadb-server unzip
```

Downgrade the `libpcap` version.

```
sudo dpkg -s libpcap0.8 | grep Version
sudo dpkg -s libpcap0.8-dev | grep Version

# downgrade the version
sudo apt-get install purge libpcap0.8 libpcap0.8-dev
```

Install the libpcap version from the local server.

```
# install and extract from local server

sudo dpkg -i libpcap libpcap-dev
```

```
sudo nano /etc/snort/snort.conf

# Step #6
output unified2: filename snort.u2, limit 128
```

Go to /tmp folder and download the barnyard source code, unzip the file and do the steps.

```
sudo tar -zxf barnyard_folder
```

Run `autogen.sh` file and it will create the configure file.

```
sudo ln -s /usr/include/dumbnet.h /usr/include/dnet.h
```

```
sudo ldconfig
```

```
sudo ./configure --with-mysql --with-mysql-libraries=/usr/lib/x86_64-linux-gnu

sudo make

sudo make install
```

Check and don't change the directory. Remember this waldo file is for tracking, whenever there is update, there needs a tracking done through waldo file.  

```
which barnyard

sudo cp etc/barnyard2.conf /etc/snort/
sudo mkdir /var/log/barnyard2
sudo chown snort:snort /var/log/barnyard2/
sudo touch /var/log/snort/barnyard2.waldo
sudo chown snort:snort /var/log/snort/barnyard2.waldo
```

```sql
sudo mysql -u root -p
```

```sql
CREATE DATABASE IF NOT EXISTS snort;
USE snort;
source /tmp/barnyard2-master/schemas/create_mysql
```

```sql
CREATE USER 'snort'@'localhost' IDENTIFIED BY 'toor';

GRANT CREATE, INSERT, SELECT, DELETE, UPDATE ON snort.* to 'snort'@'localhost';

exit
```

```
sudo nano /etc/snort/barnyard2.conf

# write the command in barnyard2.conf
output database:log, mysql, user=snort password=toor dbname=snort host=localhost
```

```
sudo chmod o-r /etc/snort/barnyard2.conf
```

```
sudo nano /etc/snort/rules/local.rules

# write the rule
alert ip any any -> any any (msg: "Kuch Bhi"; sid:100001; rev:1;)
alert ip any any -> any any (msg: "Form1"; sid:100002; rev:1;)
alert ip any any -> any any (msg: "Form2"; sid:100003; rev:1;)
alert ip any any -> any any (msg: "Form3"; sid:100004; rev:1;)
```

Installing the perl script. This is to do the mapping of message, such that when these messages can be extracted. 

```
chmod 755 create-sidmap.pl
sudo sh -c "./create-sidmap /etc/snort/rules > /etc/snort/sid-msg.map"
```

Rmemeber when you'll start the snort, then only te snort.u2 file will be created, meaning it the problem arives, you need to check u2 is created, 

```
# file will be created here
ls -l /va/log/snort
```

```
sudo snort -q -i ens33 -u snort -g snort -c /etc/snort/snort.conf
```

Now after running this command how will you check that file is getting created in `/var/log/snort`

Next, another check you need to perform on database.

```
sudo mysql -u root -p

USE snort;

SELECT COUNT(*) FROM iphdr;
```

```
sudo barnyard2 -c /etc/snort/barnyard2.conf -d /var/log/snort/ -f snort.u2 -w /var/log/snort/barnyard2.waldo -g snort -u snort
```

Now we need connect the debian 8 as well as debian 12 using the base program. 

```
cat /etc/apt/sources.list
```

```
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf

# change bind address
bind-address = 0.0.0.0

sudo systemctl restart mariadb
```

This is where we are to connect with the debian8 machine, for that we first need to start with granting permission to the user who will connect with mysql of the main server (snort server).

```
# connecting to remote user that is debian 8
sudo mysql -u root -p

GRANT CREATE, INSERT, SELECT, DELETE, UPDATE ON snort.* TO 'snort'@'192.168.80.137' IDENTIFIED BY 'toor';
```

Note that the IP *`192.168.80.137`* is the IP address of the debian 8 machine. Now install the mariadb-client (debian 8).

```
apt-get install mariadb-client
```

---

```
sudo apt-get install apache2 php5 p7zip libapache2-mod-php5 php5-mcrypt php5-mysqlnd libphp-adodb unzip

# at the time of installation copy the path that will appear
```

```
# install to deb8
ls -l | grep base

# extract it
tar -zxf base-1.4.5.tar.gz
```

```
sudo chmod -R www-data:www-data /var/www/html/base/

sudo chown -R www-data:www-data /var/www/html/base/
```

```
sudo nano /etc/php5/apache2/php.ini

# look for the second occurence of error_reporting
error_reporting = E_ALL & ~E_NOTICE
```

Now restart your apache.


```
sudo systemctl restart apache2
```

Now move to chrome and look for `http://


# Suricate IDS

Install the package. 

```
sudo apt-get install suricata

sudo systemctl restart suricata
```

Add the following rules in the file `/etc/suricata/suricata.yaml`.

```
# add interface
-interface: ens33

# below suricata-rules
rules-files:
  - suricata.rules
  - local.rules
```

Create rules.

```
# etc/suricata/rules/local.rules
alert icmp any any -> any any (msg: "Kuch Bhi ICMP"; sid: 123; rev:1;)

# restart the suricata and check status
sudo systemctl restart suricata
sudo systemctl status suricata

sudo tail -f /var/log/suricata/fast.log
```

# Blockchain

Blockchain is the methodology, the process of trying different nonces to find a valid hash is called mining. The first miner to find a suitable nonce "wins" and gets to add the new block to the blockchain. They are rewarded with cryptocurrency for their computational effort.





