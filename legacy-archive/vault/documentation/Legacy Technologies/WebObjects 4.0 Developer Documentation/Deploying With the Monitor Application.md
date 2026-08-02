---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects5.html
archived_at: '2026-07-18T01:23:53.051181Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects4.md)

# Deploying With the Monitor Application

Monitor is an application that facilitates the administration of local and remote deployments of WebObjects applications. Itself a WebObjects application, Monitor provides a simple graphical user interface for performing common administrative tasks such as:

- Adding and removing instances of applications
- Starting and stopping the execution of application instances
- Automatically restarting an instance upon failure
- Sending electronic mail to administrators when an instance fails
- Scheduling instances to be automatically started and stopped at specified intervals
- Configuring instances to be run on remote hosts

Monitor's interface reflects three distinct configurable entities: applications, instances, and hosts. An "application" represents a WebObjects application abstractly. An "instance" represents a specific instance of an application on a particular host; an instance is either running or stopped. A "host" represents a server available to run instances of WebObjects applications.

## Setting Up the Monitor Application

When WebObjects is installed, the Monitor application (__Monitor.woa__) is put in _NEXT_ROOT___/Library/WebObjects/Applications/__. Monitor's images should also be installed in your web server's document root under _DOC_ROOT___/WebObjects/Monitor.woa__. Verify that both these paths exist before you attempt to start Monitor.
Depending on your platform and on other factors related to your deployment, you might want to configure your server to launch Monitor automatically when it starts up. If you're using Monitor on Windows NT, then see "[Setting up Monitor and MonitorProxy as Services on Windows NT](ServingWebObjects11.md#apple-gyydoni)" , which describes how to set up Monitor as a service.

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects6.md)
