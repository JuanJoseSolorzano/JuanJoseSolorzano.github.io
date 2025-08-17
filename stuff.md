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