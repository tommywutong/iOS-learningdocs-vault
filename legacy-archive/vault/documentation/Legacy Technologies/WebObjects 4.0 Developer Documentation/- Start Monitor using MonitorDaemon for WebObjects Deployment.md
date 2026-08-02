---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects33.html
archived_at: '2026-07-18T01:23:52.872362Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects32.md)

## Making Monitor and MonitorProxy Fail-safe

Because Monitor is a critical piece of any deployment, you should take measures to make sure that it does not fail. To help you achieve this aim, WebObjects provides a simple command-line tool, __MonitorDaemon__. This tool restarts Monitor or __MonitorProxy__ when they fail. How you use MonitorDaemon depends on the WebObjects deployment platform.

### Using MonitorDaemon on Windows NT

When WebObjects is properly installed, the Services Control panel contains two services which use __MonitorDaemon__ to keep Monitor and __MonitorProxy__ running.: "Apple WebObjects Monitor" and "Apple WebObjects MonitorProxy." Use these services to keep Monitor and __MonitorProxy__ up and running.
To make Monitor and __MonitorProxy__ start automatically at boot time, you can configure the services to be started Automatically.

### Using MonitorDaemon on Mac OS X Server

On these platforms you can enter the __MonitorDaemon__ tool on a shell command line (such as provided by __Terminal.app__), start it from a shell script, or configure it to launch Monitor or __MonitorProxy__ automatically at boot time.
For command line usage you pass as arguments the path to the application you want to be launched and then any arguments you want to launch it with. So to start __MonitorDaemon__ for Monitor, you might give the following command:

```
MonitorDaemon
/System/Library/WebObjects/Applications/Monitor.woa/Monitor
```


To have Monitor launched at system boot time, you must add a startup script to __/etc/startup__. The scripts in __/etc/startup__ follow a naming convention whereby the first four characters of the script filename are numbers. These numbers signify the order in which the system runs the scripts in __/etc/startup__. You should start Monitor and __MonitorProxy__ near the end of the boot cycle.
You could add the following script, named __3000_Monitor__, to __/etc/startup__ to start __MonitorDaemon__ when the system boots and have it keep Monitor running:

```
#!/bin/sh

#
# Start Monitor using MonitorDaemon for WebObjects Deployment
#
. /etc/rc.common

# the following is one line:
/System/Library/WebObjects/Applications/Monitor.woa/MonitorDaemon
/System/Library/WebObjects/Applications/Monitor.woa/Monitor &
```


