---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-23.html
archived_at: '2026-07-15T08:04:44.707656Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Deploying%20With%20Monitor.md) [!](Setting%20Up%20Monitor.md) [!](Adding%20a%20Host%20to%20Monitor.md)

---

# Deploying on Multiple Hosts

Creating a deployment environment sometimes involves more than one HTTP server and many WebObjects application instances running on each server. To make several hosts available to Monitor, a daemon (or, on NT, a service) called __wotaskd__
must be running on each host. With __wotaskd__
running the Monitor application can remotely administer a host machine. When WebObjects is installed on a particular host, __wotaskd__
is automatically configured to run whenever that host machine is restarted.

Although there is no technical reason why you cannot have multiple copies of Monitor running, because Monitor maintains some information locally it is possible for multiple Monitors managing a common set of hosts to get out of sync. Thus, there ought to be only one copy of Monitor running at a time managing a given set of hosts.

The following diagram depicts one possible WebObjects deployment scenario:

!

Machine 1 acts as the web server and load balancer between all the application servers running on Machines 2, 3, and 4. Monitor should be running on the same host as the web server and the WebObjects adaptor, and is responsible for maintaining the __WebObjects.conf__
file.

#### [Adding a Host to Monitor](Adding%20a%20Host%20to%20Monitor.md#apple-obtwmslefu3danjy)

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Deploying%20With%20Monitor.md) [!](Setting%20Up%20Monitor.md) [!](Adding%20a%20Host%20to%20Monitor.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
