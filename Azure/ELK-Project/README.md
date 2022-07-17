READ.me

## Automated ELK Stack Deployment

The files in this repository were used to configure the network depicted below.

![ELK-Network-Diagram](https://user-images.githubusercontent.com/71857368/113761958-0d04e080-96e6-11eb-9a3c-9e169000f74e.png)

ELK-Network-Diagram.png

These files have been tested and used to generate a live ELK deployment on Azure. They can be used to recreate the entire deployment pictured above. Alternatively, select portions of the ELK installation YAML file may be used to install only certain pieces of it, such as Filebeat.

[Ansible-YAML](https://github.com/MitchellMcEwen/ELK-Project/blob/main/Ansible-YAML)

This document contains the following details:
- Description of the Topology
- Access Policies
- ELK Configuration
  - Beats in Use
  - Machines Being Monitored
- How to Use the Ansible Build

### Description of the Topology

The main purpose of this network is to expose a load-balanced and monitored instance of DVWA, the Damn Vulnerable Web Application.

Load balancing ensures that the application will be highly accessible, in addition to restricting specific inbound access to the network.

Load balancers play an important role in defending the server against distributed denial of service attacks, also known as DDoS attacks. It can do so by directing traffic to multiple servers with enough room for each individual which prevents overflow of traffic on a single server.
DDoS is a very common method of attack currently which is why it is important to include a load balancer from a security standpoint.


The idea of a jump box or a SAW (secure admin workstation) is to have one workstation to login into first before any administrative tasks are carried out and is much more secure than the rest. If non-administrative related tasks are being carried out on the machine it is considered to be a lot more vulnerable to attacks, this could be anything from someone checking emails to another downloading a program. This is why we have one machine labeled as the jumpbox to use only for admin related tasks.

Integrating an ELK server allows users to easily monitor the vulnerable VMs for changes to the log files and system metrics.

Filebeat is a lightweight data shipper used to collect and forward log data.  Filebeat monitors the log files and locations and forwards it to another program called Elasticsearch or Logstash for indexing which simplifies the data for us to be read.
Metricbeat is incharge of recording and forwarding information on the operating system and any other services running on your server. It is used to collect metrics and statistics and forward them to Elasticsearch or Logstash for further analysis

The configuration details of each machine may be found below :

| Name        | Function                      | IP Address | Operating System |
|---------------|-------------------------------|-----------------|-------------------------|
| Jump Box | Gateway                      | 10.0.0.4      | Linux                     |
| Web 1       | Web Server                 | 10.0.0.5      | Linux                     |
| Web 2       | Web Server                 | 10.0.0.7      | Linux                     |
| ELK          | Monitoring Dashboard | 10.1.0.5      | Linux                     |

### Access Policies

The machines on the internal network are not exposed to the public Internet. 

Only the jump box machine can accept connections from the Internet. Access to this machine is only allowed from the following IP addresses:
107.175.40.220 ( Home IP Address )

Machines within the network can only be accessed by jump box machine ( 10.0.0.4 ).
For security purposes i've only allowed my jump box and my home pc to be able to access my ELK server used as a monitoring dashboard. The jump box has access to my ELK server through ssh on port 22 from private ip ( 10.0.0.4 ) and my home pc at 107.175.40.220 through port 5601 using http.

A summary of the access policies in place can be found in the table below.

| Name          | Publicly Accessible | Allowed IP Addresses           |
|---------------|---------------------|--------------------------------|
| Jump Box      | Yes                 | 107.175.40.220                 |
| Web 1         | No                  | 10.0.0.4                       |
| Web 2         | No                  | 10.0.0.4                       |
| ELK           | Yes                 | 10.0.0.4 & 107.175.40.220:5601 |
| Load Balancer | Yes                 | Any                            |




### Elk Configuration

Ansible was used to automate configuration of the ELK machine. No configuration was performed manually, which is advantageous because this gives us the ability to configure multiple servers with one script is much more time efficient, consistent, and secure than manually configuring each server.

The playbook implements the following tasks :
Configures the ELK server to install all programs below with a docker
- Installs docker.io
- Installs python 3 - pip
- Installs docker container
- Increases the amount of virtual memory on the elk container
- Downloads and launches elk docker container with specified ports for logged data to be sent from the web servers to the elk server
- Enables the docker to start on boot 

The following screenshot displays the result of running `docker ps` after successfully configuring the ELK instance.
![DockerScreenshot](https://user-images.githubusercontent.com/71857368/113758299-ad0c3b00-96e1-11eb-9f58-d855de24b3a2.png)


### Target Machines & Beats
This ELK server is configured to monitor the following machines :

| Name   | IP Address |
|-----------|-----------------|
| Web 1  | 10.0.0.5      |
| Web 2  | 10.0.0.7      |

We have installed the following Beats on these machines :
Filebeat
Metricbeat

These Beats allow us to collect the following information from each machine:
Filebeat - Filebeat is used to collect data on log events such as user login time and id or even program errors, start times, and stop times.
Metricbeat - Metricbeat is used to collect metrics and statistical data about the operating system and other running software on the server.

### Using the Playbook
In order to use the playbook, you will need to have an Ansible control node already configured. Assuming you have such a control node provisioned : 

SSH into the control node and follow the steps below :
- Copy the elk-playbook.yaml file to /etc/ansible directory.
- Update the host file to include the web servers and elk servers with the appropriate private ip addresses. 
- Run the playbook, then navigate to the web servers through ssh and the elk server through port 5601 http at  ( http://13.64.224.110:5601/app/kibana#/home ) to check that the installation worked as expected. 
- The screenshot below is an example of what you should see when connecting to the public ip address of the ELK server after the dockers and beats have been installed and are up and running : 
![KibanaDashboard](https://user-images.githubusercontent.com/71857368/113758303-ada4d180-96e1-11eb-94d5-17e97cfccfb8.png)
- Click on explore your own and you will be redirected to a page that allows you to add any APM’s, Log’s, Metrics, or Security Events known as SIEM.
- This is where you are able to create a custom dashboard configuration that displays all previously specified information, from each server listed within the hosts file.



