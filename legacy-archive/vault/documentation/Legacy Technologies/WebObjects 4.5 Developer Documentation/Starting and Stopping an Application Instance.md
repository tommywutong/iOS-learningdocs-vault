---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-27.html
archived_at: '2026-07-15T08:04:49.773080Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Deploying%20With%20Monitor.md) [!](Creating%20Application%20Instances.md) [!](Setting%20Command-Line%20Arguments%20in%20Monitor.md)

---

# Starting and Stopping an Application Instance

You start an instance from the Application Detail View page. To get to this page, click Applications in the top banner, then click the Detail View button in the row of the instance you wish to start. Or, from the Application Configuration page for an application, you can get to the Application Detail View page by clicking the Detail View button in the upper right corner of the page. In either case, a page similar to the following should then appear:

!

The button that looks like a power switch in the Status column reports the current state of your instance: ON or OFF. The rest of the table reports other information about your instance. For more details, see [Obtaining Information From Monitor](Obtaining%20Information%20From%20Monitor.md#apple-gqytinby).

1. Click the power switch.
> The Detail View page is refreshed and the power switch appears in an animated toggle state, signifying that Monitor is trying to start your instance.

2. After a few seconds, click the Refresh button.
> Monitor will refresh the Detail View page and with success your instance will be running and the power switch will be on.

If successful, this procedure starts an instance of the application (note that it isn't displayed in your web browser). When one or more instances are running, the name of the application above the table of instances turns green, becoming a hyperlink that, when clicked, access an instance of the application. In addition, the host name and port number for each instance also become hyperlinks; clicking one of these accesses a specific instance.

If after completing the startup procedure, the instance's power switch is off, it might be due to one of the following reasons:

- Your instance failed to start and exited; check the instance's error messages in the web server's error log to find out why.
- Your instance is still starting up and Monitor has not yet received notification of a successful start. Wait a few seconds and refresh the display.
- Monitor couldn't start your instance because the path was wrong or the executable did not exist. In this case, an error message will be displayed above the instances table when the display is refreshed.

Monitor starts an instance of your application by creating a new task with the executable; it passes along all the appropriate arguments from the Instance Configuration page for that instance. Monitor starts instances of your application by first locating a running __wotaskd__
daemon or service on the appropriate host. If it finds a __wotaskd__
, it passes the application arguments to it. If it cannot contact a __wotaskd__
, it does not start the application.

Clicking the Status switch for an instance when it is ON stops the instance. Clicking the Start All button causes Monitor to attempt to start all application instances that are currently stopped; clicking the Stop All button causes Monitor to stop all instances that are currently running.

#### [Setting Command-Line Arguments in Monitor](Setting%20Command-Line%20Arguments%20in%20Monitor.md#apple-obtwmslefu4tonru)

#### [Starting Up Applications From the Command Line](Deploying-29.md#apple-obtwmslefu4tqnbz)

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Deploying%20With%20Monitor.md) [!](Creating%20Application%20Instances.md) [!](Setting%20Command-Line%20Arguments%20in%20Monitor.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
