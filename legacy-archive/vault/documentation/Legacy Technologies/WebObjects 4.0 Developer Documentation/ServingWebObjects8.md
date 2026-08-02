---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects8.html
archived_at: '2026-07-18T01:23:56.220571Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects7.md)

## Deploying on Multiple Hosts

Creating a deployment environment sometimes involves more than one HTTP server and many WebObjects application instances running on each server. The Monitor application is designed to run on a single machine. Thus there can only be one copy of Monitor running at a time and managing the same set of hosts. To make several hosts available to Monitor, a service called __MonitorProxy__ must be running. With a __MonitorProxy__ running the Monitor application can remotely administer a host machine.
A large WebObjects deployment could be depicted as in the following diagram:

!

Machine 1 acts as the web server and load balancer between all the application servers running on Machines 2, 3, and 4. You should run Monitor on the same host as the web server and the WebObjects adaptor since Monitor is involved in modifying and updating the __WebObjects.conf__ file. which the adaptor uses to find instances.

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects9.md)
