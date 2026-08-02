---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Introduction/The_WebObje_Environment.html
archived_at: '2026-07-15T08:12:11.565930Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](The_WebObje_yment_Model.md)[!](Keeping_Your_Site_Secure.md)

## The WebObjects Deployment Environment

You need to master two important aspects of WebObjects Deployment:
the communication paths of client requests and server activity,
and the deployment tools you use to configure your site.

### Communication Paths

Communication among the elements that make up a deployment
occurs in two paths: the data path and the control path.

A client HTTP request takes the data path after it reaches
your Web server. [Figure 2-4](#apple-ijauuskejbceu) shows how an HTTP request that your Web server receives
is passed to the elements that generate the response.

__Figure
2-4 The data path of a WebObjects deployment__

![[image: ../Art/datapath.gif]](../Art/datapath.gif)

__Monitor__ requests take the control path
to propagate configuration changes to application hosts and, ultimately,
application instances. These include adding application instances, and
starting and stopping instances according to a schedule that you
define. The HTTP adaptor can obtain site information by polling __wotaskd__ processes
or by reading the adaptor configuration file. (See ["Deployment Tools"](#apple-krifqusfiyytamy) for
information about Monitor and wotaskd.) [Figure 2-5](#apple-ijauuq2kjbbeo) shows the control path.

__Figure
2-5 The control path of a WebObjects
deployment__

![[image: ../Art/controlpath.gif]](../Art/controlpath.gif)

[Figure 2-6](#apple-ijauuq2jijcee) shows how the data path and control path are differentiated
in the rest of the book.

__Figure
2-6 The symbols used to represent the
data path and the control path__

![[image: ../Art/messagepaths.gif]](../Art/messagepaths.gif)

### Deployment Tools

The main tools you use to manage your site are wotaskd and
Monitor. Normally, one wotaskd process runs on each application
host. If you want to concurrently deploy multiple sites on the same
hardware, you can configure a computer to run more than one wotaskd
process. This essentially provides you with several independent
application hosts per computer.

You manage a group of application hosts using Monitor, a tool
that uses your Web browser as its user interface. Monitor lets you
set, among other things, instance scheduling and the load-balancing
algorithm to be used for each application. Because each Monitor
process maintains state information locally, you must run only one
instance of Monitor per site. [Figure 2-7](#apple-ijauuskgjbcek) shows two application
sites on one computer.

__Figure
2-7 Two sites deployed on one computer__

![[image: ../Art/twoenvironments.gif]](../Art/twoenvironments.gif)

[Figure 2-8](#apple-ijauursiivbuo) shows how you can distribute application instances
among two computers.

__Figure
2-8 Two sites deployed on two computers__

![[image: ../Art/twoofeach.gif]](../Art/twoofeach.gif)

After you configure your site using Monitor, it enforces that
configuration by performing tasks such as stopping and restarting
application instances according to a schedule you set, and sending
email notifications when problems arise. The HTTP adaptor performs
load balancing across the instances of each application on your
site.

For detailed information on the subjects introduced above,
see the following chapters or sections:

- ["HTTP Adaptors"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/WebObjectsAdaptors/iHTTP_Adaptors.html) shows
  you the different ways in which you can configure the WebObjects
  adaptor.
- ["Deployment Tasks"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/iDeployment_Tasks.html) describes
  how you use Monitor to configure your site.
- ["Setting Up Hosts"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/iSetting_Up_Hosts.html) describes
  how you use Monitor to add application hosts to your site.
- ["Configuration Files"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/DeploymentElements/iConfiguration_Files.html) shows
  you how the configuration you define in Monitor is distributed among
  the application hosts of your site.
- ["wotaskd Processes"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/DeploymentElements/iwotaskd_Processes.html) explains
  how wotaskd processes communicate with and manage application instances.
- ["Lifebeats"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/DeploymentElements/iLifebeats.html) explains
  how application instances communicate with a wotaskd process.
- ["Deploying Multiple Sites"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/iDeploying_Multiple_Sites.html) explains
  how to configure your platform to deploy multiple sites concurrently.
- ["Load Balancing"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/iLoad_Balancing.html) describes
  how load balancing works and lists the algorithms that the HTTP
  adaptor can use to implement it.

[!](The_WebObje_yment_Model.md)[!](Keeping_Your_Site_Secure.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
