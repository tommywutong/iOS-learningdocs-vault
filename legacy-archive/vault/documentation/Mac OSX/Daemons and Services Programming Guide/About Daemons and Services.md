---
title: Daemons and Services Programming Guide
apple_id: 10000172i
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html
archived_at: '2026-07-15T08:16:29.183007Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Designing%20Daemons%20and%20Services.md)

# About Daemons and Services

Many kinds of tasks that do not require user interaction are most effectively handled by a process that runs in the background. You can use a daemon or service to:

- Provide server functionality, such serving web pages.
- Coordinate access to of a shared resource, such as a database.
- Perform work for a foreground application, such as file system access.

__Figure I-1__  Daemons and services are started by launchd in two separate session contexts

!

This document provides information that developers of daemons and other low-level system services need to write their code and incorporate it into the startup process. It also provides some useful information for system administrators who must manage the startup process on the computers they manage.

### Design your Background Process

OS X provides a variety of background process types with different characteristics, designed for a different situations. There are also several ways for other processes to communicate with background processes. Choosing the appropriate design for a background process is an important first step.

### Implement your Background Process

Having made the design decisions, you are ready to begin writing code. These chapters guide you through the process of creating specific types of background jobs.

### Running Jobs on a Timed Schedule

Although it is recommended that background jobs be launched on demand, in some cases running the job on a timed schedule is the most appropriate solution.

_Logging Reference_ explains how to use the logging mechanisms provided by the system to assist during debugging and end-user troubleshooting.

_[Daemons and Agents](https://developer.apple.com/library/archive/technotes/tn2083/_index.html#//apple_ref/doc/uid/DTS10003794)_ provides additional details about implementing launch daemons and agents.

_[Kernel Programming Guide](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_ and _[Kernel Extension Programming Topics](../../Darwin/Kernel%20Extension%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrt)_ describe how to write kernel extensions and other kernel-level background processes.

_[Networking Overview](../../Networking%20Internet%20Web/Networking%20Overview/About%20Networking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrq)_ describes the APIs available for sending and receiving data across the network.

[Next](Designing%20Daemons%20and%20Services.md)

