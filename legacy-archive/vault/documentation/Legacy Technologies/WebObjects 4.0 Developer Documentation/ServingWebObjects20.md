---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects20.html
archived_at: '2026-07-18T01:23:38.827663Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects19.md)

## Starting and Stopping an Application Instance

You start an instance from the Application Detail View page. To get to this page, click Applications in the top banner, then click the Detail View button in the row of the instance you wish to start. If you have just added an application instance, and are in the Application Configuration page for the application, click the Detail View button at the top right of the page. A page similar to the following should then appear:

!

The button that looks like a power switch reports the current state of your instance: ON or OFF. The rest of the table reports other information about your instance (for more details see "[Obtaining Information From Monitor](ServingWebObjects24.md#apple-gq4tqnq)" on ).

- Click the power switch.

The Detail View page is refreshed and the power switch appears in an animated toggle state, signifying that Monitor is trying to start your instance.

- After a few seconds, click the Refresh button.

Monitor will refresh the Detail View page and with success your instance will be running and the power switch will be on.

If successful, this procedure starts an instance of the application but does not display it in the web browser. When one or more instances are running, the name of the application above the table of instances turns green, becoming a hyperlink that, when clicked, access an instance of the application. In addition, the host name and port number for each instance also become hyperlinks; clicking one of these accesses a specific instance.
If after completing the startup procedure, the instance's power switch is off, it might be due to one of the following reasons:

- Your instance failed to start and exited; check the instance's error messages to find out why.
- Your instance is still starting up and Monitor has not received notification.
- Monitor couldn't start your instance because the path was wrong or the executable did not exist.

Monitor starts an instance of your application by creating a new task with the executable; it passes along all the appropriate arguments from the Instance Configuration page for that instance. Monitor starts instances of your application in one of two ways, depending on whether the application is on a different host.

- If the application instance is on a different host, it tries to locate a running __MonitorProxy__ on that host. If it finds a __MonitorProxy__, it passes the application arguments to it. If it cannot contact a __MonitorProxy__, it does not start the application.
- If the application instance is to run on the same host as the Monitor, Monitor starts the instance itself.

Clicking the Status switch for an instance when it is ON stops the instance. Clicking the Start All button causes Monitor to attempt to start all application instances that are currently stopped; clicking the Stop All button causes Monitor to stop all instances that are currently running.

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects21.md)
