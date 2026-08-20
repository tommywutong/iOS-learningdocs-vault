---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/Deploying_Multiple_Sites.html
archived_at: '2026-07-15T08:11:59.498058Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Load_Balancing.md)[!](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Administration/index.html)

## Deploying Multiple Sites

You can deploy and configure separate sites on a set of computers
by running multiple Web servers, each with its own adaptor. Such
a deployment requires a separate group of wotaskd processes running
on the same port. You also need an additional Monitor process to
configure each site.

The default installation of the WebObjects Deployment package
provides you with one site—one wotaskd process per host, running
on port `1085`. To create
a second site, using the same hardware, you'll have to add an
additional wotaskd process to each of the hosts you want to use.

What separates the environments from each other are the `WOPort` and `WOLifebeatDestinationPort` settings
of each wotaskd process, and the configuration directory used for
each site. The application instances send their lifebeats to their WOLifebeatDestinationPort,
while wotaskd processes listen for them in their `WOPort`. [Figure 6-21](#apple-ijbussckindem) illustrates
two sites on one host.

__Figure
6-21 Multiple application environments
on one computer__

![[image: ../Art/multipleappenv.gif]](../Art/multipleappenv.gif)

Because Monitor is not started by a wotaskd process, its WOLifebeatDestinationPort argument
needs to be set to match wotaskd's.

For details on how to set the different command-line argument
values required when starting wotaskd and Monitor processes for
separate application environments, see ["WOPort"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iCommand_Line_Arguments.html), ["WOLifebeatDestinationPort"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iCommand_Line_Arguments.html),
and ["WODeploymentConfigurationDirectory"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iCommand_Line_Arguments.html).

[!](Load_Balancing.md)[!](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Administration/index.html)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
