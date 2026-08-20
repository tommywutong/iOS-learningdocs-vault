---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/StartMonitor.html
archived_at: '2026-07-15T07:56:05.075139Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.md) [!Previous Section](SetUpMonitor.md)

## Starting Up Monitor

To start up Monitor on Windows NT, choose Monitor from the WebObjects program group in the Start menu.
To start up Monitor on any other system, do the following:

- Open a command shell window.
- Enter these commands:

```
    > cd /NextLibrary/WOApps/Monitor.woa
    > Monitor
```


The Monitor application launches in your default web browser and displays this screen:

!

### Which Copy of Monitor Should I Use?

If you have multiple machines running WebObjects, you can administer them all from a single instance of Monitor on a single machine. It's recommended that you use the copy of Monitor that's installed on the same machine as your HTTP server and WebObjects adaptor. This is because the main purpose of the Monitor is to maintain the public configuration file (__WebObjects.conf__), which the WebObjects adaptor uses to find running instances of WebObjects applications. The best way to achieve sharing of the __WebObjects.conf__ file is to have your HTTP server and Monitor run on the same machine. The alternative-having Monitor on a separate machine-would require that the two machines share a file system through network access.
Monitor can communicate with WebObjects applications running on remote hosts; however to launch applications on remote hosts it uses a lightweight daemon named __MonitorProxy__. For example, the following figure shows a WebObjects site spread across four machines. One machine contains the HTTP server, and the other three machines contain WebObjects applications. You would run the Monitor application on the machine containing the HTTP server. That Monitor application would use the __MonitorProxy__ daemons on the other three machines to launch applications. All other communication goes directly between Monitor and the WebObjects application.

!

### Starting Up MonitorProxy

As mentioned in the previous section, if you have a multiple machine configuration, you need to run Monitor on one machine and run __MonitorProxy__ daemons on the other machines. You can start up __MonitorProxy__ daemons the same way you start up Monitor:
To start up __MonitorProxy__ on Windows NT, do the following:

- Navigate to the directory _NeXT_ROOT___/NextLibrary/WOApps/Monitor.woa__ in the Explorer.
- Double-click __MonitorProxy.exe__.

To start up __MonitorProxy__ on any other system, do the following:

- Open a command shell window.
- Enter these commands:

```
    > cd $NEXT_ROOT/NextLibrary/WOApps/Monitor.woa
    > MonitorProxy
```


You probably want to set up your system so that __MonitorProxy__ starts up at system boot time.
__Note:__ If you're running Monitor on a Solaris or HP-UX machine, you must start up __MonitorProxy__ on that machine as well. As you'll learn later, Monitor requires the local __MonitorProxy__ to start up applications on Solaris and HP-UX.

[!Table of Contents](ServingWebObjectsTOC.md) [!Next Section](InitialSetup.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
