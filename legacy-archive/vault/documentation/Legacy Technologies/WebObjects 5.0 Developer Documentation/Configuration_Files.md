---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/DeploymentElements/Configuration_Files.html
archived_at: '2026-07-15T08:12:09.957738Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Managing%20Application%20Instances.md)[!](Lifebeats.md)

## Configuration Files

You use Monitor to configure your site. With it you configure
hosts, applications, and application instances. You also define
schedules for restarting instances and choose the algorithm used
to balance the user load among the instances of an application.
For details on the tasks that you can perform using Monitor, see ["Deployment Tasks"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/iDeployment_Tasks.html).

The `SiteConfig.xml` file,
which is maintained on each host's configuration directory by wotaskd,
stores the configuration choices you make in Monitor. You should
not modify the contents of this file directly. The user under which
wotaskd runs must have read and write privileges to `SiteConfig.xml` and
the user under which Monitor runs must have read privileges.

You can create another configuration file (the HTTP adaptor
configuration file), which is called `WOConfig.xml` by
default. This is the file the HTTP adaptor uses to obtain your site's configuration
when you choose the configuration file method for the adaptor.

[Figure 5-1](#apple-ijbusqscifdue) shows how the configuration files are distributed
in a deployment with one Web server and two application hosts. For
information on how to generate the HTTP adaptor configuration file,
see ["Creating the HTTP Adaptor Configuration File"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/WebObjectsAdaptors/iState_Discovery.html).

__Figure
5-1 WebObjects configuration-file distribution__

![[image: ../Art/configurationfiles.gif]](../Art/configurationfiles.gif)

[!](Managing%20Application%20Instances.md)[!](Lifebeats.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
