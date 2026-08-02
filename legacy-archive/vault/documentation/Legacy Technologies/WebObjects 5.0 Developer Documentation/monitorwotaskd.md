---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeploymentAdditions/monitorwotaskd.html
archived_at: '2026-07-15T08:12:19.085907Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

__Monitor and wotaskd__

This document describes changes made to Monitor, wotaskd, and application instance interactions since WebObjects 4.5

__Overview__

The lifebeat mechanism has been changed to improve reliability and response times to changes of instance state. Lifebeats from WebObjects applications are now sent over TCP sockets with a default period of 30 seconds. If the application is multithreaded the lifebeats will be sent from their own thread; otherwise, a timer in the main run loop will send them. Lifebeats are of four types: has started, lifebeat, will stop, and will crash. These types allow wotaskd to be notified quickly of changes and enable the web server adaptor to respond quickly. For example, if an application is exiting normally, the 'will stop' lifebeat is sent from the application to wotaskd. This is especially useful when scheduling is used. See the Adaptor documentation for information on changes to the web server adaptor since WebObjects 4.5.

Monitor has been updated to be more responsive and perform more validation:

- Communication timeouts are nearly an order of magnitude shorter when communicating with unresponsive wotaskds.

- Hosts are only valid if they can be resolved to an IP address.

- Application names and arguments are stripped of invalid characters.

- The user interface has been updated.

wotaskd has been updated to be more responsive and reliable:

- Communication timeouts are shorter.

- wotaskd's listen port is configurable.

- Applications are started with that wotaskd's listen port as their lifebeat destination port.

- Applications not in the SiteConfig are registered with a negative port number. This allows developers to test their applications through the web server adaptor without making them available to the outside world. (See the Adaptor changes documentation.)

The configuration directory for wotaskd and Monitor can be changed using the default "-WODeploymentConfigurationDirectory <Path>".

__Monitor__

Monitor should be run on one and only one host for a site. Each instance of Monitor maintains its own SiteConfig information that is pushed to the application host. When you have two instances of Monitor running on different hosts and launching applications on the same host, each Monitor instance will alternately push their different SiteConfig information to the application host, overwriting the other©s information each time. (For example, with wotaskd running with the same listen port on all hosts, if you run Monitor on Host D, add an application that runs on Host B and Host E, then run Monitor on Host Z and add an application to run on Host B you are going to have conflicts on Host B because Monitor run from Host D and Host Z will have different SiteConfigs. These different SiteConfigs will be pushed to Host B, alternately overwriting each other. Do not do this.)

When a host is deleted in Monitor the instances running on that host are stopped and the SiteConfig on that host is reset to an empty state as long as Monitor is not also running on that host.

The exception history has been removed from the detail page.

Hosts and Applications

Hosts

Monitor now ensures that it can resolve a hostname or IP address before it will add it to the list of hosts; unresolved names will not be accepted. Monitor will also not allow you to add the same host more than once. Hosts are considered equivalent if they resolve to the same IP address.

Applications

When you add an application in Monitor the name will be stripped of characters that could cause problems if present in URLs or XML tags. The allowed characters are [A-Z],[a-z],[0-9], "-", and ".".

The additional arguments field is also cleansed of extra spaces and new-line characters at the end of the line. Extra spaces between arguments are removed in an attempt to reduce problems with starting instances. However, this will cause problems if you have custom arguments that contain spaces, e.g. '-WOCustomerDefault "a value with spaces"'.

Application Instance Arguments and Defaults

For complete specifications of the application instance arguments, see Monitor's help page.

wotaskd

__wotaskd Command Line Arguments and Defaults__

For complete specifications of the wotaskd command line arguments and defaults, see Monitor's help page.

__Changing wotaskd's Listen Port__

If you want to change which port is used by applications for their lifebeat messages, you must set the port on wotaskd, Monitor, and all instances launched.

To configure wotaskd to listen on a different port launch wotaskd with "-WOPort•<#>". To configure Monitor and instances to send to a different port launch them with "-WOLifebeatDestinationPort•<#>". Note '<#>' represents the same integer.

wotaskd will automatically launch application instances with -WOLifebeatDestinationPort set to its listen port. Monitor is not started by wotaskd so its startup arguments will also need to be changed to match.

Launched in this way, you can have separate sets of wotaskd/Monitor/instances running on the same network and they won't know about each other. These different groups should not have applications configured with the same names. The instance executables can be the same, just not the name for the application they are known as in the SiteConfig. This is because the instance numbers are not unique across these groups and the web server adaptor will get confused about which application instance maps to which instance.

Accessing wotaskd when a password is set in Monitor

Once a password is set in Monitor, wotaskds running on hosts which are configured in Monitor will no longer respond to http:/<hostname>:1085. In order for a response to be returned, they will require a header with the encrypted password. This is the desired behavior for a deployment environment.

To find out what wotaskd is reporting you can either look at the SiteConfig.conf files on the host, use the new wotaskd link in Monitor's HostsPage, or use the following steps to view the information remotely:

- Look at the SiteConfig.conf on the machine running Monitor

- Find the line with "

Password = <encrypted-string>;"

- Execute

'telnet <hostname> 1085'

- Once connected type:

GET /

password: <encrypted-string>

<return>

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
