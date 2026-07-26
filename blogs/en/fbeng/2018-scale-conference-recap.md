---
title: '2018 @Scale Conference recap'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2018/09/17/android/2018-scale-conference-recap/'
original_language: en
published: 2018-09-17
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:adb1dee13a3b07b0'
translated: false
---

> 原文：[2018 @Scale Conference recap](https://engineering.fb.com/2018/09/17/android/2018-scale-conference-recap/)　·　Meta Engineering — iOS

The [@Scale Conference](https://atscaleconference.com/events/the-2018-scale-conference/) is an invitation-only technical event for engineers who work on large-scale platforms and technologies. This year’s event took place on September 13 at the San Jose Convention Center, where more than 2,500 attendees gathered to discuss how to build applications and services that scale to millions or even billions of people. The conference featured technical deep dives from engineers at a multitude of scale companies, including **Adobe, Amazon, Cloudera, Cockroach Labs, Facebook, Google, Microsoft, NASA, NVIDIA, Pinterest, and Uber**.

Below are summaries and videos of the three @Scale 2018 keynote addresses and other presentations.

If you’re interested in attending the next event, visit the [@Scale website](https://atscaleconference.com/) and join the [@Scale community](https://www.facebook.com/atscaleevents/).

## Keynote addresses

**Inside NVIDIA’s AI infrastructure for self-driving cars**  
 **Clément Farabet, VP of AI Infrastructure, NVIDIA**

With the race to bring self-driving cars to market, deep learning is crucial to the automotive industry. In his keynote address, Clément discusses in-depth for the first time NVIDIA’s production-level, end-to-end infrastructure and workflows to develop AI for self-driving cars.

Building autonomous vehicles creates scale challenges across multiple areas in the development process and the infrastructure stack. Given the high-risk and costly nature of testing autonomous vehicles in the real-world, billions of simulated and millions of real driving miles are needed to ensure safety requirements are met. However, more than the miles themselves, what matters is training and testing across all possible use cases and scenarios, including 100 different environmental conditions, 100 different transients or variations, and 100 different fault injections.

Clément discusses how NVIDIA’s team is building an AI platform that can support simulation and validation with hardware-in-the-loop at this extreme scale, from the rack-level design optimized for AI and the server design improvements made to minimize bottlenecks in storage, network, and compute. NVIDIA’s supercomputing infrastructure is able to support continuous data ingest from multiple cars (each producing terabytes of data per hour) and enables autonomous AI designers to iterate training new neural network designs across thousands of GPU systems and validate their behavior over multi-petabyte-scale datasets.

The obstacles faced by self-driving cars aren’t limited to the world of autonomous driving. Clément shares how the problems NVIDIA has solved in building this infrastructure for training and inference are applicable to others deploying AI-based services, including innovations in NVIDIA’s inference platform that are pushing the boundaries of what’s possible at scale.

**Glow: A community-driven approach to AI infrastructure**  
 **Jason Taylor, Vice President of Infrastructure, Facebook**

In this keynote address, Jason announces the next steps in Facebook’s efforts to build a [hardware ecosystem for machine learning (ML) through partner support of the Glow compiler](https://engineering.fb.com/ml-applications/glow-a-community-driven-approach-to-ai-infrastructure/). Cadence, Esperanto, Intel, Marvell, and Qualcomm Technologies Inc., a subsidiary of Qualcomm Incorporated, have committed to supporting Glow in future silicon products and technologies.

The rise of AI and machine learning has created a new set of bottlenecks for the network as workloads increase exponentially in size and scale. The traditional models for performance scaling are no longer enough to deal with these new sets of challenges. With an open source framework designed to be community driven, Glow allows partners to more rapidly design and optimize new silicon products for AI and ML processing by leveraging highly optimized compiler software.

**A golden age for computer architecture**  
 **David Patterson, Distinguished Engineer, Google, and Professor, UC Berkeley**

The end of Dennard scaling and Moore’s law are not problems that must be solved but facts that, if accepted, offer breathtaking opportunities. In his @Scale Conference keynote, David discusses how high-level, domain-specific languages and architectures aided by open source ecosystems and agilely developed chips will accelerate progress in machine learning. He envisions a new golden age for computer architecture in the next decade.

## @Scale 2018: Data

**Presto: Fast SQL on everything**  
 **Vaughn Washington, Software Engineering Manager, Facebook**

Presto is an open source, high-performing, distributed relational database system targeted at making SQL analytics over big data fast and easy at Facebook. It provides rich SQL language capabilities for data engineers, data scientists, and business analysts to quickly and interactively process terabytes to petabytes of data. Presto is widely used within at Facebook for interactive analytics with thousands of active users.

Facebook is using Presto to accelerate a massive batch pipeline workload in our Hive Warehouse. Presto is also used to support custom analytics workloads with low-latency and high-throughput requirements. As an open source project, Presto has been adopted externally by many companies, including Comcast, LinkedIn, Netflix, Walmart, and others. In addition, Presto is being offered as a managed service by multiple vendors, including Amazon, Qubole, and Starburst Data. In this talk, Vaughn outlines a selection of use cases that Presto supports at Facebook, describe its architecture, and discuss several features that enable it to support these use cases.

**Run your database like a CDN**  
 **Peter Mattis, VP of Engineering, Cockroach Labs**

Modern businesses serve customers around the globe, but few manage to avoid sending far-flung customer requests across an ocean (or two!) to application servers colocated with a centralized database. This presents two significant problems: high latencies and conflicts with evolving data sovereignty regulations. CockroachDB is a distributed SQL database that solves the problem of global scale using a combination of features including geo-replication, geo-partitioning, and data interleaving, which together allow a customer’s data to stay in proximity while still enjoying strong, single-copy consistency.

Peter’s talk briefly introduces CockroachDB and then explores how it is able to achieve low latency and precise data domiciling in an example global use case.

**Scaled machine learning platform at Uber**  
 **Jeremy Hermann, Head of Machine Learning Platform, Uber**

In this talk, Jeremy discusses Michelangelo, Uber’s machine learning platform. The purpose of Michelangelo is to enable data scientists and engineers to easily build, deploy, and operate machine learning solutions at scale. It is designed to be ML-as-a-service, covering the end-to-end machine learning workflow: manage data, train models, evaluate models, deploy models, make predictions, and monitor predictions. Michelangelo supports traditional ML models, time series forecasting, and deep learning.

Jeremy covers some of the key ML use cases at Uber, the main Michelangelo components and workflows, and newer areas that his team is developing.

**Resource management at scale for SQL analytics**  
 **Tim Armstrong, Software Engineer, Cloudera**

Apache Impala is a highly popular open source SQL interface built for large-scale data warehouses. Impala has been deployed in production at more than 800 enterprise customers as part of Cloudera Enterprise, managing warehouses up to 40 PB in size. Hadoop Distributed File System (HDFS), cloud object stores, and scalable columnar storage engines make it cheap and easy to store large volumes of data in one place rather than spread across many silos. This data attracts queries, and, soon enough, contention for resources arises between different queries, workloads, and organizations. Without resource management policies and enforcement, critical queries can’t run and users can’t interactively query the data. In this talk, Tim discusses the challenges in making resource management work at scale for SQL analytics and how his team is tackling them in Apache Impala.

**Goku: Pinterest’s in-house time-series database**  
 **Tian-Ying Chang, Senior Staff Engineer and Manager of the Storage and Caching Team, Pinterest**  
 **Jinghan Xu, Software Engineer, Pinterest**

In this presentation, Tian-Ying and Jinghandiscuss Goku, a highly scalable, cost-effective, and high-performant online time series database service. It stores and serves massive amount of time series data without losing granularity. Goku can write tens of millions of data points per second and retrieve millions of data points within tens of milliseconds. It supports high compression ratio, downsampling, interpolation, and multidimensional aggregation. It can be used in a wide range of monitoring tasks, including production safety, and IoT. It can also be used for real-time analytics that make use of time series data.

**Amazon Aurora: Design considerations for high throughput cloud-native relational databases**  
 **Sailesh Krishnamurthy, General Manager, Amazon Web Services**

Amazon Aurora is a relational database service for online transaction processing (OLTP) workloads offered as part of Amazon Web Services. In this talk, Sailesh describes the architecture of Aurora and the design considerations leading to that architecture. Sailesh discusses how the central constraint in high throughput data processing has moved from compute and storage to the network.

Aurora brings a novel architecture to the relational database to address this constraint, most notably by pushing redo processing to a multi-tenant scale-out storage service, purpose-built for Aurora. Sailesh describes how this not only reduces network traffic but also allows for fast crash recovery, failovers to replicas without loss of data, and fault-tolerant, self-healing storage. Traditional implementations that leverage distributed storage would use distributed consensus algorithms for commits, reads, replication, and membership changes, and amplify the cost of underlying storage. Sailesh describes how Aurora avoids distributed consensus under most circumstances by establishing invariants and leveraging local transient state. These techniques improve performance, reduce variability, and lower costs.

## @Scale 2018: Machine learning

**Applied machine learning at Facebook: An infrastructure perspective**  
 **Kim Hazelwood, Engineering Manager, Facebook**

Machine learning sits at the core of many essential products and services at Facebook. Kim’s talk describes the hardware and software infrastructure that supports machine learning at global scale. Facebook machine learning workloads are extremely diverse: services require many different types of models in practice. This diversity has implications at all layers in the system stack. In addition, a sizable fraction of all data stored at Facebook flows through machine learning pipelines, presenting significant challenges in delivering data to high-performance distributed training flows. Computational requirements are also intense, leveraging both GPU and CPU platforms for training and abundant CPU capacity for real-time inference. Addressing these and other emerging challenges continues to require diverse efforts that span machine learning algorithms, software, and hardware design.

**Computer vision at scale as cloud services**  
 **Cha Zhang, Principal Researcher, Microsoft Cloud & AI**

In this talk, Cha describes how, as computer vision matures and becomes ready for real-world applications, Microsoft’s team has set a mission to scale and democratize it via cloud services. Starting by integrating some of the latest computer vision work from Microsoft Research, we quickly learned that building such a service at scale requires not only state-of-the-art algorithms but also deep care of customer demands. In this talk, Cha walks through some of the challenges, including data privacy, deep customization, and bias correction, and discusses solutions they have built to tackle these challenges.

**Accelerate machine learning at scale using Amazon SageMaker**  
 **Vlad Zhukov, Head of Engineering, Amazon SageMaker**

Organizations are using machine learning to address a series of business challenges, ranging from product recommendations, demand forecasting, customer churn, medical research, and many more. The ML process includes framing the problem statement, collecting and preparing data, training and tuning, and deploying the models. In this session, Vlad talks about how Amazon SageMaker removes the barriers and complexity associated with building, training, and deploying ML models at scale to address a wide range of use cases.

**Distributed AI with Ray**  
 **Ion Stoica, Professor, UC Berkeley**

Over the past decade, the bulk synchronous processing (BSP) model proved highly effective for processing large amounts of data. Today, however, we are witnessing the emergence of a new class of applications — AI workloads. These applications exhibit new requirements, such as nested parallelism and highly heterogeneous computations.

In this talk, Ion discusses how his team developed Ray, a distributed system that provides both task-parallel and actor abstractions. Ray is highly scalable, employing an in-memory storage system and a distributed scheduler. Ion discusses some design decisions as well as early experiences using Ray to implement a variety of applications.

**Artificial intelligence at Orbital Insight**  
 **Adam Kraft, Computer Vision Machine Learning Lead, Orbital Insight**

Orbital Insight is a geospatial big data company leveraging the rapidly growing availability of satellite, UAV, and other geospatial data sources to understand and characterize socio-economic trends at global, regional, and hyperlocal scales. In this talk, Adam discusses the satellite imagery domain, how it’s evolving, and the various advantages and challenges of working with such imagery. He shares several example applications, demonstrating how machine learning is disrupting this space.

**MLPerf: A suite of benchmarks for machine learning**  
 **Cliff Young, Software Engineer, Google**

The MLPerf effort aims to build a common set of benchmarks that enables the machine learning field to measure system performance for both training and inference from mobile devices to cloud services. In this presentation, Cliff discusses how a widely accepted benchmark suite will benefit the entire community, including researchers, developers, builders of machine learning frameworks, cloud service providers, hardware manufacturers, application providers, and end users.

**Friends don’t let friends deploy black-box models: The importance of intelligibility in machine learning**  
 **Rich Caruana, Principal Researcher, Microsoft**

In machine learning, a trade-off often must be made between accuracy and intelligibility. The most accurate models usually are not very intelligible (e.g., deep nets), and the most intelligible models usually are less accurate (e.g., linear regression). Frequently, this trade-off limits the accuracy of models that can safely be deployed in mission-critical applications such as health care, where being able to understand, validate, edit, and ultimately trust a learned model is important.

In this talk, Rich discusses developing a learning method based on generalized additive models (GAMs) that is often as accurate as full complexity models but even more intelligible than linear models. This makes it easy to understand what a model has learned, and also makes it easier to edit the model when it learns inappropriate things because of unanticipated problems with the data. Making it possible for experts to understand a model and repair it is critical, because most data has unanticipated land mines.

Rich presents a case study in which these high-accuracy GAMs discover surprising patterns in data that would have made deploying a black-box model risky. He also briefly shows how these models are used to detect bias in domains where fairness and transparency are paramount.

## @Scale 2018: Developer tools

**One World: Scalable resource management**  
 **Evan Snyder, Production Engineer, Facebook**

As Facebook’s user base and family of applications grows, it’s important to ensure correctness and performance across many hardware and software platforms. Managing all these combinations for testing would be an operational impossibility for small teams focused on a particular service or feature. To make testing scalable and reliable, Evan discusses how Facebook built a resource management system called One World to allow teams to dependably request the platforms required via a unified API, no matter its type or location.

**Automated fault-finding with Sapienz**  
 **Ke Mao, Software Engineer, Facebook**

Sapienz designs system tests that simulate user interactions with mobile apps. It automatically finds apps’ crashes, and localizes them, tracks them, and triages them to developers. In his talk, Ke covers how Sapienz is deployed at a large scale at Facebook, including continuous integration with Facebook’s development process, fault signals boosted by Infer’s static analysis, and cross-platform testing on both Android and iOS.

**Machine learning testing at scale**  
 **Manasi Joshi, Director of Software Engineering, Google**

Machine learning is infused in all walks of life — and in a lot of Google products, including Google Home, Search, Gmail, and more, and in systems such as those used by self-driving cars and fraud detection. A tremendous amount of effort is being made to improve people’s experiences using products throughout the industry, where products are powered by ML and AI. However, developing and deploying high-quality, robust ML systems at Google’s scale is hard. This can be due to many factors, including distributed ownership, training serving skew, maintaining privacy and proper data access controls, model freshness, and compatibility.

In her @Scale talk, Manasi discusses how Google started an ML productivity effort to empower developers to move quickly and launch with confidence. This effort encompasses building infrastructure for reliability and reusability of software, as well as the extraction of critical ML metrics that can be monitored to make informed decisions throughout the ML life cycle.

**Regression testing against real traffic on a Big Data reporting system**  
 **Trenton Davies, Principal Scientist, Adobe**

Adobe Analytics’ underlying query API handles thousands of complex reporting queries per second across a user base of hundreds of thousands. In his @Scale talk, Trenton discusses how the Adobe engineering team has significantly increased the quality and frequency of releases over the past few years by mirroring production API traffic to its test builds and running regression analysis that compares the API responses of its production and test builds. Adobe’s novel approach allows its engineers to test millions of API permutations using real traffic, without mocking any portion of the system and without affecting the availability of Adobe’s production systems.

**Scaling concurrency bug detection with the Infer static analyzer**  
 **Nikos Gorogiannis, Software Engineer, Facebook**

Concurrency is hard, and inevitable, given the evolution of computing hardware. Helping programmers avoid the exotic and messy bugs that come with parallelism can be a productivity multiplier but is also elusive. Implementing such a service via static analysis and at the scale of Facebook may sound too good to be true. In this talk, Nikos discusses Facebook’s efforts to catch data races, deadlocks, and other concurrency pitfalls by deploying two analyzers based on Facebook Infer that comment at code review time, giving programmers early feedback.

**Integrated Symbolic Execution for Space-Time Analysis of Code: Scalability challenges**  
 **Corina Pasareanu, Associate Research Professor, NASA**

Attacks relying on the space-time complexity of algorithms implemented by software systems are gaining prominence. Software systems are vulnerable to such attacks if an adversary can inexpensively generate inputs that cause the system to consume an impractically large amount of time or space to process those inputs, thus denying service to benign users or disabling the system. The adversary can also use the same inputs to mount side-channel attacks that aim to infer some secret from the observed space-time system behavior.

In her talk, Corina discusses ISSTAC: Integrated Symbolic Execution for Space-Time Analysis of Code. The project has developed automated analysis techniques and implemented them in an industrial-strength tool that allows the efficient analysis of software (in the form of Java bytecode) with respect to space-time complexity vulnerabilities. The analysis is based on symbolic execution, a well-known analysis technique that systematically explores program execution paths and also generates inputs that trigger those paths. Corina gives an overview of the project, highlighting scalability challenges and how they were addressed.

**Testing strategy with multi-app orchestration**  
 **Leslie Lei, Software Engineer, Uber**

Uber’s dual-app experience introduces an interesting challenge for mobile functional testing. In this talk, Leslie introduces methods of doing mobile E2E testing while orchestrating multiple apps. Leslie discusses the pros and cons of each method and how her team has scaled them to run with speed and stability.
