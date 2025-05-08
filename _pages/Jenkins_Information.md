---
layout: page
title: Jenkins Information
permalink: /pages/Jenkins_Information/
date: 2021-07-16
---

# Jenkins
Here we won't talk abut the common questions: **_What is Jenkins?_** or **_What can Jenkins do?_**. No, we will demostrate step by step the process of Jenkins, how to install, how to install its dependencies, etc. For this laboratory, we will use a Virtual Machine (VM) where be installed a Debian12 Operate System and and ZSH as a shell. 

## Installing Jenkins
Jenkins is a server, which means that Jenkins application will be running in a machine sharing and reciving data. The first step is install the Jenkins server in our system.

1. **Installing Java:** Since Jenkins is a Java application we will need to install Java if we do not have installed it yet.

    ```
    sudo apt update
    sudo apt install openjdk-17-jdk -y
    java --version 
    ```
2. **Installing Jenkins:** In this step we will need to add the Jenkins repository to the debian package manager, but this is only because Jenkins is not part of debian package manager, if you are using Windows or other Operting System, you might be skip this.
    ```
    curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
    /usr/share/keyrings/jenkins-keyring.asc > /dev/null

    echo 'deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/' | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

    sudo apt update
    ```
    Then install Jenkins Server:
    ```
    sudo apt install jenkins -y
    ```
3. Start Jenkins Server:
    ```
    sudo systemctl start jenkins
    sudo systemctl enable jenkins
    ```
    Jenkins is running on port 8080 by default, so we will need to opened it in or firewall:
    ```
    sudo ufw allow 8080
    sudo ufw reload
    ```

## Open Jenkins
Now, we have Jenkins server running on port 8080, so we can access it through an a webpage. In this case I will use firefox:
```
http://localhost:8080 (http://127.0.0.1:8080)
```
**You will see the following login window:**
![Chungking Express Screencap 1]({{site.baseurl}}/assets/images/jenkins/login_window.png)

The password needed is in: 
```
/var/lib/jenkins/secrets/initialAdminPassword
You can get the content with:
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```


install the suggested plugins option, and create an user:

![Chungking Express Screencap 2]({{site.baseurl}}/assets/images/jenkins/suggested_plugins.png)
![Chungking Express Screencap 3]({{site.baseurl}}/assets/images/jenkins/user_creation.png)

In the URL option, in this case we will use our local IP to get acces localy:

![Chungking Express Screencap 4]({{site.baseurl}}/assets/images/jenkins/URL_cnf.png)

finally, press 'start using Jenkins' button, and you will see:

![Chungking Express Screencap 5]({{site.baseurl}}/assets/images/jenkins/Jenkins_Main.png)

We can also access to Jenkins from the host machine (Windows11):

![Chungking Express Screencap 6]({{site.baseurl}}/assets/images/jenkins/Jenkins_from_host.png)

![Chungking Express Screencap 7]({{site.baseurl}}/assets/images/jenkins/Jenkins_from_host_2.png)

## Creating a Job
No we will create a Jenkins job using the VM as an agent.
In the Dashboard, we can see the following options:

![Chungking Express Screencap 8]({{site.baseurl}}/assets/images/jenkins/Job_creation_1.png)

In this example we will create a simple periodic task using a pipeline script:

![Chungking Express Screencap 9]({{site.baseurl}}/assets/images/jenkins/New_item_creation.png)

And then configure the adding a description, a trigger and defying the pipe line:

![Chungking Express Screencap 10]({{site.baseurl}}/assets/images/jenkins/trigger_example_1.png)

As an example, this will be the pipeline:
```
pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                sh 'echo $SHELL'
                sh 'ls -la'
            }
        }
    }
}
```
Once the Job is saved you will see the dashboard and the execution status:
![Chungking Express Screencap 11]({{site.baseurl}}/assets/images/jenkins/Executed_Job.png)

Inside of the Job, you will see the builds status, and inside of each build you will find the log or the console output:

![Chungking Express Screencap 12]({{site.baseurl}}/assets/images/jenkins/Job_builds_status.png)

![Chungking Express Screencap 13]({{site.baseurl}}/assets/images/jenkins/build_status.png)

## Creating an Agent
In a real environment we will working with agents (Nodes). The agents are others servers or computers which works as host to store the output of a Jenkins Job. 
For the following example, we will use our host machine (Windows11) as a Agent (node), so we will create the node and the pipiline in the VM (Debian12) and and we will specifiy to use this agent (Windows11) to execute an especific Job:

1. In Manage Jenkins options we will find the Node Option:

![Chungking Express Screencap 14]({{site.baseurl}}/assets/images/jenkins/Node_creation_1.png)

Right now, we only have the VM agent:

![Chungking Express Screencap 15]({{site.baseurl}}/assets/images/jenkins/Node_creation_2.png)

2. Select '+ New Node' and set the agent name and we select the 'Type' as 'Permanent Agent'

![Chungking Express Screencap 16]({{site.baseurl}}/assets/images/jenkins/Node_creation_3.png)

Then, fill all the necessaries space:

![Chungking Express Screencap 17]({{site.baseurl}}/assets/images/jenkins/Node_creation_4.png)

![Chungking Express Screencap 18]({{site.baseurl}}/assets/images/jenkins/Node_creation_5.png)

Now, we'll have an Agent, but it is not working yet, we need to start the agent in the agent machine, in this case, in the host machine. To do this we will need to install some Java dependencies on our Agent machine, and execute a command to initialize the agent. When you just recently created the Agent you will see the command necessary to start the agent:

![Chungking Express Screencap 19]({{site.baseurl}}/assets/images/jenkins/Node_creation_6.png)

As you can see in the image, it is necessary that the Agent machine have the Java package installed, 
1. In the Agent machine we need to have Java installed, open a terminal and run:
```
java --version
```
to see if java is installed, if not, you can find how to install here: https://www.oracle.com/java/technologies/downloads/?er=221886

Once Java is installed, you will be able to executed the command:
create a secret file:
```
echo 6b4abf69db4c3718fd370e6af515158c2a44c39a911c07ffde21714f6686c731 >> secret-file
```
Get the agent.jar from Jenkins server:
```
curl.exe -sO http://localhost:8080/jnlpJars/agent.jar
```
Start the Agent:
```
java -jar agent.jar -url http://localhost:8080/ -secret @secret-file -name "Window11_HostMachine" -webSocket -workDir "D:/jenkins"
```
Remember, you will need to change the localhost to the Jenkins server IP, and change the directory to the specified: 'D:/jenkins/'

Now you will see in the windows terminal something like:
![Chungking Express Screencap 20]({{site.baseurl}}/assets/images/jenkins/Node_creation_7.png)

Now the node is active:
![Chungking Express Screencap 21]({{site.baseurl}}/assets/images/jenkins/Node_creation_8.png)

Now, for the previos created Job, we will indicate that only will be executed it by the windows11 Agent:

![Chungking Express Screencap 22]({{site.baseurl}}/assets/images/jenkins/Node_execution_1.png)

![Chungking Express Screencap 23]({{site.baseurl}}/assets/images/jenkins/Node_execution_2.png)

Now, we could clone a GitHub repository and find it in the Agent machine once the Job fished. To do this, we will change the pipeline:

```
pipeline {
    agent {
        label 'Window11_HostMachine'
    }
    stages {
        stage('Clone Repository') {
            steps {
                bat 'powershell -C "git clone https://github.com/JuanJoseSolorzano/Bash_Scripting.git"'
            }
        }
    }
}
```
When running you will see the repository cloned:

![Chungking Express Screencap 24]({{site.baseurl}}/assets/images/jenkins/Node_execution_3.png)

![Chungking Express Screencap 25]({{site.baseurl}}/assets/images/jenkins/Node_execution_4.png)

## Jenkins & GitHub webhooks
....
....
....