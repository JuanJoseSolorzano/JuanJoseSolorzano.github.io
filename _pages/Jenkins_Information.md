---
layout: page
title: Jenkins Information
permalink: /pages/Jenkins_Information/
date: 2021-07-16
---

![Jenkins Emblem]({{site.baseurl}}/assets/images/jenkins/Jenkins_Emblem.png){: width="400" height="400" style="float: left; margin-left: -60px; margin-bottom: 20px;" } 

Here we won't discuss the common questions: **_What is Jenkins?_** or **_What can Jenkins do?_**. Instead, we will demonstrate step-by-step the process of using Jenkins, including how to install it, its dependencies, and more. For this tutorial, we will use a Virtual Machine (VM) running Debian 12 as the operating system and ZSH as the shell.

<nav class="navbar navbar-expand-lg navbar-light" style="margin-bottom:auto; margin-top: auto;"></nav>

## Installing Jenkins
Jenkins is a server application, which means it will run on a machine, sharing and receiving data. The first step is to install the Jenkins server on our system.

1. **Installing Java:** Since Jenkins is a Java application, we need to install Java if it is not already installed.

    ```
    sudo apt update
    sudo apt install openjdk-17-jdk -y
    java --version 
    ```

2. **Installing Jenkins:** In this step, we need to add the Jenkins repository to the Debian package manager. This is necessary because Jenkins is not part of the default Debian package manager. If you are using Windows or another operating system, you might skip this step.

    ```
    curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
    /usr/share/keyrings/jenkins-keyring.asc > /dev/null

    echo 'deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/' | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

    sudo apt update
    ```

    Then, install the Jenkins server:
    ```
    sudo apt install jenkins -y
    ```

3. **Starting Jenkins Server:**
    ```
    sudo systemctl start jenkins
    sudo systemctl enable jenkins
    ```
    [?] Jenkins runs on port 8080 by default, so we need to open this port in our firewall:
    ```
    sudo ufw allow 8080
    sudo ufw reload
    ```

<nav class="navbar navbar-expand-lg navbar-light" style="margin-bottom:auto; margin-top: auto;"></nav>

## Accessing Jenkins
Now that the Jenkins server is running on port 8080, we can access it through a web browser. For example, using Firefox:

```
http://localhost:8080 (http://127.0.0.1:8080)
```

**You will see the following login window:**

![Login Window]({{site.baseurl}}/assets/images/jenkins/login_window.png){: width="600" height="400" }

The password needed is located in: 
```
/var/lib/jenkins/secrets/initialAdminPassword
```
You can retrieve it with:
```
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

Follow the setup wizard, install the suggested plugins, and create a user:

![Suggested Plugins]({{site.baseurl}}/assets/images/jenkins/suggested_plugins.png){: width="600" height="400" }

![User Creation]({{site.baseurl}}/assets/images/jenkins/user_creation.png){: width="600" height="400" }

In the URL configuration step, use your local IP to access Jenkins locally:

![URL Configuration]({{site.baseurl}}/assets/images/jenkins/URL_cnf.png){: width="600" height="400" }

Finally, press the 'Start using Jenkins' button, and you will see the Jenkins dashboard:

![Jenkins Dashboard]({{site.baseurl}}/assets/images/jenkins/Jenkins_Main.png){: width="600" height="400" }

You can also access Jenkins from the host machine (Windows 11):

![Access from Host]({{site.baseurl}}/assets/images/jenkins/Jenkins_from_host.png){: width="600" height="400" }

![Access from Host 2]({{site.baseurl}}/assets/images/jenkins/Jenkins_from_host_2.png){: width="600" height="400" }

## Creating a Job
Now we will create a Jenkins job using the VM as an agent. On the dashboard, you will see the following options:

![Dashboard Options]({{site.baseurl}}/assets/images/jenkins/Job_creation_1.png){: width="600" height="400" }

In this example, we will create a simple periodic task using a pipeline script:

![New Item Creation]({{site.baseurl}}/assets/images/jenkins/New_item_creation.png){: width="600" height="400" }

Then, configure the job by adding a description, a trigger, and defining the pipeline:

![Trigger Example]({{site.baseurl}}/assets/images/jenkins/trigger_example_1.png){: width="600" height="400" }

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

Once the job is saved, you will see the dashboard and the execution status:

![Execution Status]({{site.baseurl}}/assets/images/jenkins/Executed_Job.png){: width="900" height="900" }

Inside the job, you will see the build status, and within each build, you can find the log or console output:

![Build Status]({{site.baseurl}}/assets/images/jenkins/Job_builds_status.png){: width="600" height="400" }

![Console Output]({{site.baseurl}}/assets/images/jenkins/build_status.png){: width="600" height="400" }

## Creating an Agent
In a real environment, we work with agents (nodes). Agents are other servers or computers that host the output of Jenkins jobs. 

For this example, we will use our host machine (Windows 11) as an agent (node). We will create the node and the pipeline in the VM (Debian 12) and specify that this agent (Windows 11) will execute a specific job.

In the "Manage Jenkins" options, find the "Nodes" option:

![Node Creation 1]({{site.baseurl}}/assets/images/jenkins/Node_creation_1.png){: width="900" height="400" }

Currently, we only have the VM agent:

![Node Creation 2]({{site.baseurl}}/assets/images/jenkins/Node_creation_2.png){: width="900" height="400" }

Select '+ New Node', set the agent name, and select the 'Type' as 'Permanent Agent':

![Node Creation 3]({{site.baseurl}}/assets/images/jenkins/Node_creation_3.png){: width="900" height="400" }

Then, fill in all the necessary fields:

![Node Creation 4]({{site.baseurl}}/assets/images/jenkins/Node_creation_4.png){: width="900" height="400" }

![Node Creation 5]({{site.baseurl}}/assets/images/jenkins/Node_creation_5.png){: width="900" height="400" }

Now, we have an agent, but it is not active yet. We need to start the agent on the agent machine (in this case, the host machine). To do this, we need to install some Java dependencies on the agent machine and execute a command to initialize the agent. When you create the agent, you will see the necessary command to start it:

![Node Creation 6]({{site.baseurl}}/assets/images/jenkins/Node_creation_6.png){: width="900" height="400" }

As shown in the image, the agent machine must have Java installed. Open a terminal and run:
```
java --version
```
If Java is not installed, you can find installation instructions here: https://www.oracle.com/java/technologies/downloads/?er=221886

Once Java is installed, execute the following commands:
1. Create a secret file:
```
echo 6b4abf69db4c3718fd370e6af515158c2a44c39a911c07ffde21714f6686c731 >> secret-file
```
2. Download the `agent.jar` from the Jenkins server:
```
curl.exe -sO http://localhost:8080/jnlpJars/agent.jar
```
3. Start the agent:
```
java -jar agent.jar -url http://localhost:8080/ -secret @secret-file -name "Window11_HostMachine" -webSocket -workDir "D:/jenkins"
```
Remember to replace `localhost` with the Jenkins server IP and adjust the directory to the specified path: `D:/jenkins/`.

Now, you will see the following in the Windows terminal:

![Node Creation 7]({{site.baseurl}}/assets/images/jenkins/Node_creation_7.png){: width="900" height="400" }

The node is now active:

![Node Creation 8]({{site.baseurl}}/assets/images/jenkins/Node_creation_8.png){: width="900" height="400" }

For the previously created job, we will specify that it should only be executed by the Windows 11 agent:

![Node Execution 1]({{site.baseurl}}/assets/images/jenkins/Node_execution_1.png){: width="900" height="400" }

![Node Execution 2]({{site.baseurl}}/assets/images/jenkins/Node_execution_2.png){: width="900" height="400" }

Now, we can clone a GitHub repository and find it on the agent machine once the job finishes. To do this, we will modify the pipeline:

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

When running the job, you will see the repository cloned:

![Node Execution 3]({{site.baseurl}}/assets/images/jenkins/Node_execution_3.png){: width="900" height="400" }

![Node Execution 4]({{site.baseurl}}/assets/images/jenkins/Node_execution_4.png){: width="900" height="400" }

## Jenkins & GitHub Webhooks
// ...existing content...