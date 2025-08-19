---
layout: page
title: General Information
permalink: /stuff/
---

Find interesting notes about trainings and courses taken. Have fun!

<details markdown="1">
<summary>Introduction to DevOps</summary>

## What is DevOps?

- The term (development and operations) is an extension of agile development environments that aims to enhance the process of software delivery as a whole.
- DevOps (Development and Operations) engineers work together, following Lean and Agile principles, delivering software in a rapid and continuous manner.

DevOps is not:
- Simply combining development and operations.
- A separate team.
- A tool.
- Just automation.

## What is the goal?

There are three pillars:
- DevOps         -> For speed and agility.
- Microservices  -> For small deployments.
- Containers     -> For ephemeral runtimes.

Culture is the #1 success factor in DevOps. Building a culture of *shared responsibility, transparency, and faster feedback* is the foundation of every high-performing DevOps team. --Atlassian--

To become DevOps, it is necessary to change the company culture. It must change:
- The way people think.
- The way people work.
- The way people are organized.
- The way people are measured.

## Agile perspective

Waterfall > Agile > DevOps are methods for software development and delivery.
Monoliths > SOA > Microservices are architectures: ways that software is built.
Physical servers > VMs > Containers are used to create infrastructure: basic services such as communication and storage.

- 2007 Patrick Debois: Dev and Ops worked ineffectively and not together.
- 2008 Agile Infrastructure.
- 2009 John - Velocity 2009 -"10+ Deploys Per Day" -> Dev and Ops cooperation at Flickr.
- 2010 Continuous Delivery - Through automation of the build, deploy, and test process, along with improved collaboration.
- 2013 Lean principle.

----

# Thinking DevOps

## Code reuse dilemma
- Code has 80% of what you need but 20% is missing.

## Social coding solution
- Discuss with the repo **owner**.
- Agree to develop it.
- Open an **Issue** and assign it to yourself.
- **Fork** the code and make your changes.
- Issue a **Pull Request** to review and merge back.

## Git Repository Guidelines
- The same that we already know about it.

## The size of the batches
Working in small batches means delivering something useful quickly.
Using single piece flow leads to faster feedback loops.

## Minimal Viable Product (MVP)
- MVP is a tool for learning.
- The experiment may fail and that's okay.
- It is the minimal thing that you can do to test your hypothesis.

## Quiz
- Which of these is typical of traditional thinking?
    ANS: Rebuilding 100% of the code to get the 20% change you need.
- Which of these is part of minimum viable product?
    ANS: Should I pivot or persevere?

## Test Driven Development (TDD)
- Test your code, but first create cases and then create code.
- Red->Green->Refactor cycle.
It is important: It saves time when developing, you can code faster and with more confidence, it ensures the code is working as expected, it ensures that future changes do not break your code. In order to create a DevOps CI/CD pipeline, all testing must be automated.

## Behavior Driven Development (BDD)
- BDD focuses on the behavior of the system from the outside in. It looks at the system as a consumer of it.
- BDD uses an approachable syntax that everyone can understand.
- It improves communication.

## Cloud Native Microservices (CNM)
- CNM is a collection of independently deployable microservices.
- Stateless microservices each maintain their own state in a separate database or persistent object store.
- Microservices are loosely coupled services, designed for scalability and communication with APIs.

# Working DevOps
- Culture of teaming and collaboration.
- Agile development as a shared discipline.
- Push smaller releases faster.

## Taylorism
- Is regarding the Industrial Revolution. It describes how to work as automotive line assembly, working in silos.
_Software development is bespoke:_
    - Software development is NOT like assembling automobiles.
    - Most of the parts do not exist yet.
    - Software development is craft work.

- Command and control is not Agile.
- Stop working in silos.
- Let your people amaze you.

- Working DevOps means pushing small releases faster in order to get feedback, minimize risk, and maximize learning.
- Taylorism was designed for factory work, while software development is like craft work.

# Software Engineering vs Civil Engineering
- SW stack is constantly updated.

# Required DevOps behavior
- DevOps delivers a continual series of small changes.
- Development wants innovation and Operations want stability. But you cannot get both.

## Required DevOps behaviors
- Shared ownership and high collaboration.
- Risk management by embracing change.
- Ephemeral infrastructure as code.
- Automated self-service.
- Feedback loops and data-driven responsibility.

## Infrastructure as code
- Described in an executable textual format.
- Configure using that description.
- Configure the system.
- Never perform configurations manually.
- Use version control.

## Continuous Integration and Continuous Delivery
- CI/CD is not one thing.
- Continuous Integration is: Continuously building, testing, and merging to master.
- Continuous Delivery is: Continuously deploying to a production-like environment.

# Align teams with the business
- Each team has its own mission aligned with the business.
- Teams have end-to-end responsibility for what they build.
- Teams should have a long-term mission.

## There is no DevOps Teams
- DevOps is the practice of development and operations engineers working together during the entire software lifecycle, following Lean and Agile principles that allow them to deliver high-quality results.

# DevOps metrics
- A baseline provides a concrete number for comparison as you implement your DevOps changes.
- Old school is focused on mean time to failure (MTTF).
- DevOps is focused on mean time to recovery (MTTR).

## Summary
- You should measure and reward what you want to improve.
- Measuring social metrics leads to improved socialization and measuring DevOps metrics allows you to see progression toward goals.
- DevOps changes the objective of problem resolution from failure prevention to failure recovery.

# Vanity Metrics vs Actionable Metrics
- Vanity metrics may be appealing at first glance, but offer limited actionable insights.
- Actionable metrics provide meaningful ways to measure your processes and work toward goals.

# Comparison of DevOps to Site Reliability Engineering (SRE)
- SRE maintains separate development and operations silos with one staffing pool.
- DevOps breaks down the silos into one team with one business objective.

</details>

<details markdown="1">

<summary>Overview Of Automotive SPICE (ASPICE)</summary>

# The Automotive SPICE (Software Improvement and Capability dEtermination).

Is an adaptation of the **Software Process Improvements and Capability dEtermination** standard (ISO 15504), addapted specially for the Automotive industry.
ASPICE provides a **framework for assessing and imporoving** the software development processes within automotive suppliers and manufactures. It helps ensure high-quiality software, better safety, and reliable performance in vehcles' electronic control units (ECUs)

The ASPICE Model is based on the V-CYCLE, one of the Software Development Life Cycle (SDLC).

## Software Development Life Cycle (SDLC)

Is the process of creating software, from initial planning through deployment and ongoing maintenance

SDLC has the following structure:

    1. Requirements Analysis -> * Business Analyst * Project Manager * Product Manager.
    2. System Design -> * Architect * Designer.
    3. Implementation -> * Developer * Software Implementation.
    4. Testing -> * Verification and Validation * Quality Assurance * Tester.
    5. Deployment -> * Release Manager * DevOps Engineer * IT Operations.
    6. Maintenance -> * Support Engineers * Testers.

Each phase ensures quality and traceability throughout the software development process.

## V - Model (an extension of the traditional Waterfall model)

V-Model is an Verification and Validation model:

![V_MODEL]({{site.baseurl}}/assets/images/stuff_images/ASPICE/vmodel.png)

| Left-side  (develop side)                                                |   Right-Side  (testing side)
|--------------------------------------------------------------------------|------------------|
| Business Requirements Specification (Waht does the user want?)           | User Acceptance Testing 
  System Requirements Specification   (What should the overall system do?) | System Integration Testing (Does the whole system meet the requirements?)
  High Level Design / Architecture    (How will teh system be structure?)  | Component Testing (Do components work together?)
  Low Level Design / Details (How each component be build?)                | Unit Testing (Does each component work?)
  <-> Coding <-> | <-> coding <-> |

```markdown
[VALIDATION]  - and -  [VERIFICATION]
Requirements     ->    User Acceptance
    |                     |
    v                     ^
System Design    ->    System Testing
    |                     |
    v                     ^
Architecture     ->   Integration Testing
    |                     |
    v                     ^
Detailed Design  ->   Unit Testing
    |                     |
    v                     ^
     Implementation (Coding)
```
This is an sequential model, and it is usefull fo requirements well-done. A disvantage is thata design cannot emerge during coding, since each phase must be sequetial. Oeverll, the V-Model provides a structured path from requirements to finished product.

### ISO 26262
    Is an international standard that provides functional safety requirements and processes for electrical and electronic systems within road vehicles. It aims to reduce safety reisks from malfunctions by defining development best practices.

### ISO 21434
    Is a new standard focused on cyber security for road vehicles. It provides a framework and process to manage cyber risks during the product life.  

### ISO 21448
    Is a road vehicles standard that specifies user experience and human-machine interface design.
  
OEM -> Original Equipment Manufacturer: A company that produces parts, components or complete products that are then used in another company's end product.
-  

# ASPICE 3.0 Model

![ASPICE30]({{site.baseurl}}/assets/images/stuff_images/ASPICE/aspice30.png)

The ASPICE model has three process groups: 
    1. Primary Life Cycle Process.
        - System Engineering Process group (SYS)
        - Software Engineering process group (SWE)
        - Acquisition process group (ACQ)
        - Supply process group (SPL)
    2. Organization Life Cycle Process.
        - 
    3. Supporting Life Cycle Process.


## Process Assessment Model

ASPICE defines a process assessment model to evalute and rate the capability of software process in the automitve indudtry. the ASPICE assessment model has two dimensions:

    1. Process dimension:
        * Covers teh software process within the scope of assessment.
    2. Capability dimension:
        * Defines six capability levels (0-5) that indicate the maturity fo each process. Level 0 mean the process is not implemented. Level 5 means the process is optimized.
TheA ASPICE  assessment method provides a standardized way to measure and improve software process against a reference benchmark.  

# Module #2 Describing the ASPICE Model

## ASPICE Model Description

### Primary Life Cycle Process (SYS)

### Primary Life Cycle Process (SYS)

SYS.1 – Requirements Elicitation: Gather, document, and track requirements as required by stakeholders.

SYS.2 – System Requirements Analysis: Analyze and refine the collected requirements to ensure clarity and feasibility.

SYS.3 – System Architectural Design: Establish the overall system architecture and develop the system structure.

SYS.4 – System Integration and Integration Test: Integrate system components and perform integration testing to verify interactions.

SYS.5 – System Qualification Test: Provide evidence that the integrated system meets all specified requirements.

*The System Engineering process group ensures that stakeholder requirements are fully captured, analyzed, and validated throughout the system development lifecycle.*

### Primary Life Cycle Process (SWE)

SWE.1 – Software Requirements Analysis: Collect and analyze software-specific requirements.

SWE.2 – Software Architectural Design: Define the software architecture and allocate requirements to software components.

SWE.3 – Software Detailed Design and Unit Construction: Develop detailed designs and construct software units.

SWE.4 – Software Unit Verification: Verify individual software units against detailed design and requirements.

SWE.5 – Software Integration and Integration Test: Integrate software units and perform integration testing.

SWE.6 – Software Qualification Test: Provide evidence that the integrated software meets all requirements.

*The Software Engineering process group focuses on ensuring that software requirements are addressed, implemented, and verified at each stage of development.*

---
** As a part of Automation Activities, the mostly close ASPICE process areas are:
    Group: Primary life Cycle Process (SWE): 
    - SWE.4 - Software Unit Verification.
    - SWE.5 - Software Integration and Integration Test.
    - SWE.6 - Software Qualification Testing.
---

## ASPICE Process Capability levels
1. Level 0 (Incomplete):
    
    - The process is not implemented or fails t achieve its purpose.

2. Level 1 (Performed):
    
    - The process achieve its purpose.

3. Level 2 (Managed):

    - The performed process is now implemented in a managed fashion.
    - Performance is controlled and maintained.

4. Level 3 (Established):
    
    - The process is established, capable, standardized and maintained.
    - Standards for process performance are stablished.

5. Level 4 (Predictable):
    
    - The process is quantitatively controlled and predictable.
    - Performance varies within narrow, predictable limits.

6. Leve 5 (Innovating):
    
    - The focus in on continuous improvement.
    - Process innovation improve effectiveness and efficiency.

`The capability levels range from an incomplete process at level 0 to a performed procedure at level 1, to managed standardized, and quantiatively controlled process at levels 2-4, to an optimized, continuously improving process at level 5.`

`At Level 0, no code review process exists.`

`Level 1-2 introduce basic manual processes.`

`Level 3 establishes a standardized process.`

`Level 4, quantitative control is added.`

`Level 5, innovative improvements are made through automation and AI.`

</details>

<details markdown="1">
<summary>Advanced Python Development Techniques</summary>

# Set and deques
    ```python
    #Sets do not repeat once output
    example_set = {1,2,3,4,5}
    #Even if you see duplicates within
    example_set = {1,1,2,3,4,5}
    example_set.add(6)
    print(example_set)
    example_set.remove(2)
    print(example_set)
    ```
    ```python
    # A deque is a double-ended queue, it's a generalization of stacks and queues allowing
    # you to efficently add or remove elements.
    from collections impoort deque
    my_deque = deque([1,2,3])
    my_deque.append(4)
    print(my_deque)
    # removing elements from the left
    my_deque.pop()
    print(my_deque)
    # removing elements from the right
    my_deque.popleft()
    print(my_deque)
    ```
## Undo and Redo actions using deques
    ```python
    from collections impoort deque
    undo_stack = deque()
    redo_stack = deque()
    def perform_action(action):
        undo_stack.append(action)
        redo_stack.clear()
    def undo():
        if undo_stack:
            action = undo_stack.pop()
            redo_stack.append(action)
    def redo():
        if redo_stack:
            action = redo_stack.pop()
            undo_stack.append(action)

    split_words = str("Hello world").split()
    for word in split_words:
        perform_action(word)
        
    print(undo_stack)

    # undo action:
    undo()
    print(undo_stack)
    # redo action:
    redo()
    print(undo_stack)
    ```
</details>