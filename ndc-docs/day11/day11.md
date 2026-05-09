# Logstash Pipeline

Logstash Comprises of three process basically, Extract, Transform, Load which is also callled **ELT**. Think of it as a pipeline, that is referred as set of process that has three phases comprising of, 

- **Config**
  - Input
  - Filter
    - mutate
    - grok
    - dns
  - Output
    - elasticsearch
    - stdout

# Logstash LAB

Take the debian file from the local server named logstash.

```bash
# check if it is installed
dpkg -l <logstash-file>

# check status
sudo systemctl status logstash

# write conf file to read the pipeline
nano pipe1.conf # pipe1 is not mandatory, just need to be a .conf file

# script
input {
    stdin {}
}
output {
    stdout { codec => rubydebug } 
}

# giving input to .conf file
echo "Hello World" | sudo /usr/share/logstash/bin/logstash -f /home/shuhari/pipe1.conf

# now we need to inplement filter
nano /home/shuhari/pipe1.conf

# add filter
filter {
    mutate { uppercase => ["message"] }
}
```

Logstash solves the problem that existes in real world. Logstash is using the filter process that will process the outputs therefore, we will now maekshcnages into out debian file. 

```
# see the history.log file
sudo tail /var/log/apt/history.log

# create the one.conf file
sudo nano one.conf

# write script
input {
    file {
        path => "/var/log/apt/history.log"
        start_position => "end"
        sincedb_path => "/var/lib/logstash/apt.sincedb"
    }
}

filter {
    if [message] =~ /Commandline:/ {
        mutate {
            add_field => { "installation_status" => "installed"}
        }
    }
    else {
        drop { }
    }
}

output {
    elasticsearch {
        hosts => ["http://localhost:9200"]
        index => "apt_logs"
    }
    stdout { codec => rubydebug }
}

# restart the service
sudo systemctl restart logstash

ls -l /var/lib/logstash/

curl -X GET "localhost:9200/_aliases?pretty=true"

sudo apt-get install -y sl

curl -X GET "localhost:9200/_aliases?pretty=true"

curl -X GET "localhost:9200/_apt_logs*/_search?pretty=true"

cat /var/log/apt/history.log | less 

systemctl restart logstash


```

After this you need to watch how we are processing the data.

# Kibana

We saw how to store the data in Elasticsearch, then we looked at how we can process the data using Logstash, next we need to focus on Kibana, where we represent the data.

```
# install kibana


# change in /etc/kibana/kibana.yml
# uncomment
server_port: 5601
server_host: "0.0.0.0"

# check the status
sudo systemctl status kibana
```

Now you need to browse kibana using the IP-address and port number, move to ** ... 

Create data view, provide the name as well as the 


# IPSec

IPSec uses the ISAKMP Interent Security Agreement/Key Management Protocol, which initiates a secure agreement for the two computer to communicate. This is called Security Association, where two computers agree to establish secure communication based on certain protocols, methods of encryption (symmetric, asymmetric, or hash function). 

- First step involves choosing the algorithm (DES, Triple DES), then what algorithm will be used for the message check (MD5, or SHA-256), and how connection will be authenticated, meaning (shared secret key, public-key certificate)

- Second step involves negotiation, meaning whether AH is to used or ESP is to be used, which encryption algo to be used in ESP, or if using AH then which protocols to be used. 


# Nagios: Email Alert Lab

Objective is to recieve an email alert for the health performance. `swaks` needs to be installed, it is used for testing the email functionality. 

```bash
# install software swaks
sudo apt-get install swaks

# check email utility
swaks --to <recipient-email-id> --from <sender-email-id> --auth --auth-user=uerone -auth-password=toor --server sunbeam.shuharilabs.com
```

Now we configure our nagios. 

```bash
# configure file
sudo nano /usr/local/nagios/etc/objects/contacts.cfg

# edit email id
email               nagios@localhost;
```

Now you need to check the `/usr/local/nagios/etc/objects/templates.cfg` and look at some parameters, such as below:

- `d` - DOWN
- `u` - UNREACHABLE
- `r` - HOST RECOVERies
- `f` - HOSTS START AND STOPS FLAPPING
- `s` - HOST OR SERVICE SHEDULED DOWNTIME STARTS AND ENDS

Now move to file `/usr/local/nagios/etc/objects/contacts.cfg`.

```bash
# add entries below email
host_notification_period    24x7
host_notification_options   d,u,r,f,s
host_notification_commands  notify-host-by-email

# move to /usr/local/nagios/etc/objects/command.cfg
sudo nano /usr/local/nagios/etc/objects/command.cfg

# move to /usr/local/nagios/etc/resource.cfg
# enter user id
$USER5$=someuser

# enter the password
$USER6$=sompassword

# smtp server and port
$USER7$=<smtp-server> # for exmaple 172.16.164.134:25

# enter from send id
$USER8$=userone@shuhari.local

# now move to dev_12-1.cfg file and add
notification_enabled    1
notification_period     24x7
notification_interval   1
check_interval          1
notification_options    d,u,r,f,s
contacts                nagiosadmin

# now send mail with subject and body 
swaks --to <recipient-email-id> --from <sender-email-id> --auth --auth-user=uerone -auth-password=toor --server sunbeam.shuharilabs.com -h-Subject "Kubhi Subject" --body "Kuch Bhi Mail body"

# use echo to pipe cmd
echo "My KuchBhi Mail Body" | swaks --to <recipient-email-id> --from <sender-email-id> --auth --auth-user=uerone -auth-password=toor --server sunbeam.shuharilabs.com -h-Subject "Kubhi Subject another" --body "Kuch Bhi Mail body another" - 


# use echo to pipe cmd
echo "[[GABBER IS BACK]]\n\nYO!" | swaks --to <recipient-email-id> --from <sender-email-id> --auth --auth-user=uerone -auth-password=toor --server sunbeam.shuharilabs.com -h-Subject "Kubhi Subject another" --body "Kuch Bhi Mail body another" - 
```

The message is as below:

```bash
# message
/usr/bin/echo -e "**** Nagios *****\n\nNotification Type: $NOTIFICATIONTYPE$\nHost: $HOSTNAME$\nState: $HOSTNAME$\nAddress: $HOSTADDRESS$\nInfo: $HOSTOUTPUT$\n\nDate/Time: $LONGDATESTIME$\n" | /usr/bin/swaks --to $CONTACTMAIL$ --from $USER8$ --server $USER7$ --auth LOGIN --auth-user $USER5$ --auth-password $USER6$ --h-Subject "** $NOTIFICATION$ Host Alert: $HOSTNAME$ is $HOSTSTATES$ **" --body -
```


