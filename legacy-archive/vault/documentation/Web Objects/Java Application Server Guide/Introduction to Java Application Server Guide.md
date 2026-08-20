---
title: Java Application Server Guide
apple_id: TP40002323
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Conceptual/J2EE_JavaAppServerGuide/Introduction/Introduction.html
archived_at: '2026-07-18T02:14:23.193066Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Application%20Server%20Overview.md)

# Introduction to Java Application Server Guide

JBoss is a powerful Java-based open-source application server that is very popular among Java 2, Enterprise Edition (J2EE) application developers. This document describes how to configure and use the JBoss application server in OS X Server, which lets you deploy J2EE applications easily and reliably.

This document is intended for system administrators, J2EE application assemblers, and developers. It assumes you have a solid background in system administration and J2EE technology. You must be familiar with OS X Server, especially how to use Terminal to issue shell commands. Knowledge of database engines, such as MySQL, is helpful but not required.

This document has the following chapters:

- [Application Server Overview](Application%20Server%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgmrtfvbuqmrrgqwueqsdijcuer2b) provides an overview of JBoss for OS X Server.
- [Configuring Applications](Configuring%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgmrtfvbuqmrrguwueqkkiveesr2e) explains how to perform certain tasks with the deployment tool, such as opening, configuring, and saving application archives.
- [Configuring and Deploying Sun’s Pet Store](Configuring%20and%20Deploying%20Sun%E2%80%99s%20Pet%20Store.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgmrtfvbuqmrrgywueq2ji5buiqkc) walks you through configuring and deploying Sun’s Pet Store application in OS X Server.
- [Administering Application Servers](Administering%20Application%20Servers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgmrtfvbuqmrrg4wugsscindeessh) teaches you how to manage application servers, which are JBoss instances running on one or more computers.
- [Balancing User Load and Replicating Sessions](Balancing%20User%20Load%20and%20Replicating%20Sessions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgmrtfvbuqmrrhawueqkkjjduor2d) explains how to enable an application to be distributable among cluster nodes and walks you through configuring HTTP load balancing for Pet Store using three computers.

This document also contains a revision history, a glossary, and an index.

To use this document to its fullest, you should download its companion files, which are packaged in `Application_Server_companion.zip`, located in the same webpage from which you obtained this document.

For an introduction to J2EE, visit [http://java.sun.com/j2ee](http://java.sun.com/j2ee). You can get detailed information on JBoss at [http://jboss.org](http://jboss.org/).

[Next](Application%20Server%20Overview.md)

