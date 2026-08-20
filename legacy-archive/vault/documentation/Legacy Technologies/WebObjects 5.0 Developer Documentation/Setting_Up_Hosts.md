---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/Setting_Up_Hosts.html
archived_at: '2026-07-15T08:12:08.018895Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Deployment%20Tasks.md)[!](Installing_Applications.md)

## Setting Up Hosts

An application host is a machine that runs application instances.
For Monitor to be able to identify a host, it has to be running
a wotaskd process. See ["Choosing What to Install"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Installation/iChoosing_What_to_Install.html) and ["Confirming That wotaskd Is Active"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Installation/iConfirming__d_Is_Active.html).

### Adding a Host

Before you can deploy applications, you need to tell Monitor
which hosts you want to use for deployment. (See ["Load Balancing"](Load_Balancing.md#apple-ijbusskjijcue) for
additional information regarding load balancing and hosts added
in Monitor.) [Figure 6-1](#apple-ijbusrkkiffes) shows Monitor's Hosts page, which you use to add
and configure hosts.

__Figure
6-1 The Hosts page__

![[image: ../Art/hostadd.gif]](../Art/hostadd.gif)

1. In Monitor,
   click the Hosts tab.
2. Enter the name or IP address of the host you want to add in
   the host text input field.

   The machine must be running a wotaskd
   process in the port that Monitor sends its lifebeats to.

   Avoid
   using a __loopback__ address (a connection that does
   not go over the network), such as `localhost` or `127.0.0.1`.
   If you do, it must be the only application host in your site.
3. Chose the appropriate platform from the pop-up menu.
4. Click Add Host.

[Figure 6-2](#apple-ijbusrkcjfdeq) shows the Hosts page after a host has been added.

__Figure
6-2 Newly added host in Monitor__

![[image: ../Art/hostadd2.gif]](../Art/hostadd2.gif)

### Configuring a Host

To change the configuration of an application host, click
the Config button on the Hosts page. A page similar to the one in [Figure 6-3](#apple-ijbusr2fifbuu) appears.
It allows you to set the type of the host and to resynchronize configuration
information if needed.

__Figure
6-3 Host configuration page__

![[image: ../Art/hostconfigure.gif]](../Art/hostconfigure.gif)

### Viewing a Host's Configuration

To display the configuration for a host, click YES, on the
Hosts page. A page similar to the one in [Figure 6-4](#apple-ijbusr2cirbuq) is displayed in a separate
Web browser window.

__Figure
6-4 Host configuration information page__

![[image: ../Art/monwotaskdconfig.gif]](../Art/monwotaskdconfig.gif)

This page displays the current state of the host in several
sections.

The section visible in [Figure 6-4](#apple-ijbusr2cirbuq) shows the contents of
the host's `SiteConfig.xml` file.
For more information on the `SiteConfig.xml` file,
see ["Configuration Files"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/DeploymentElements/iConfiguration_Files.html).

The next section shows the adaptor configuration sent to local
HTTP adaptors, which lists all running application instances that
wotaskd knows about (this includes Monitor processes).

```xml
<?xml version="1.0" encoding="ASCII"?>
<adaptor>
    <application name="JavaMonitor">
        <instance id="-8888" port="8888" host="ebruce2.apple.com"/>
    </application>
</adaptor>
```

Note that the instance ID of the Monitor process is negative.
When wotaskd receives a lifebeat from an application instance that
has not been registered (added to your site through Monitor), it
discloses the instance to the Web server with a negative ID number. This
allows developers (internal users) to connect to instances through
the HTTP adaptor for testing purposes. To address security concerns,
external users can connect to instances with negative ID numbers
only if they know the instance's port number.

To connect to a development instance through the Web server,
the instance must run on the same computer that the Web server runs
on, and the computer must be the `localhost`.

Next is the local adaptor configuration sent to remote HTTP
adaptors. This section lists all instances that are active, registered
(configured through Monitor), and available to external users.

```xml
<?xml version="1.0" encoding="ASCII"?>
<adaptor>
  <application name="Payroll" urlVersion="4">
    <instance id="1" port="2001" host="ebruce.apple.com"/>
  </application>
  <application name="HR" urlVersion="4">
    <instance id="1" port="2002" host="ebruce.apple.com"/>
  </application>
</adaptor>
```

The next section shows the contents of the HTTP adaptor configuration
file. If you tell wotaskd to write the HTTP adaptor configuration
file, it lists all the registered application instances on the site,
whether they are running or not. (This file is identical across
all the site's application hosts.) See ["The HTTP Adaptor Configuration File"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/WebObjectsAdaptors/iState_Discovery.html) for
more information and an example of the file's contents.

The last section lists information on the wotaskd process's
environment, including its port and multicast address.

```
The Configuration Directory is: /Library/WebObjects/Configuration/
Wotaskd is NOT writing WOConfig.xml to disk
The multicast address is: 239.128.14.2
This wotaskd is running on Port: 1085
Wotaskd is NOT responding to Multicast
WOAssumeApplicationIsDeadMultiplier is 4
The System Properties are: ...
```

[!](Deployment%20Tasks.md)[!](Installing_Applications.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
