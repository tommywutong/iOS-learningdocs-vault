---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-37.html
archived_at: '2026-07-15T08:04:55.849872Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Monitoring%20Application%20Activity.md) [!](Monitoring%20Application%20Activity.md) [!](Logging%20and%20Analyzing%20Application%20Activity.md)

---

# Obtaining Information From Monitor

The Applications page gives an overall view of a deployment. It shows which applications are configured, how many instances each application has, and which of these is currently running. You get to the Applications page by clicking the Applications button in Monitor's banner. A screen similar to the following example is displayed:

!

Click a hyperlink in the Application column to start a session with an instance of that application.

The Application Detail View page of the Monitor application provides you with detailed information about all configured instances of a WebObjects application. Click the Detail View button next to an application in the Applications page to go to the detail page, which looks similar to the following example:

!

At the top of the page is the title of the application. When one or more instances of an application are running, this title becomes a hyperlink. Clicking on the hyperlink opens a new browser window and connects to the running application.

The tables of the Application Detail View contain various information and controls:

| Column | Description |
| --- | --- |
| Host / Port | The host name and the port that the instance runs on. If the instance is running, this information is hyperlinked; clicking starts a new session with the instance. |
| Status | Indicates whether the instance is running (ON) or is stopped (OFF). Clicking this control starts and stops the instance. |
| Schedule | Indicates whether scheduling is enabled. When ON is displayed, the Status, Auto-Recover, and Refuse New Sessions indicators are disabled; scheduling is responsible for setting all of those states on a schedule basis. See "[Automatic Scheduling](Automatic%20Scheduling.md#apple-geytgnzt)" for information on scheduling. |
| Auto-Recover | Displays the Auto-Recover setting for this instance. ON indicates that Monitor should start a new instance upon failure or shutdown of an instance. You can set this state when you configure the instance; see [Setting Command-Line Arguments in Monitor](Setting%20Command-Line%20Arguments%20in%20Monitor.md#apple-gqydsmrz). |
| Refuse New Sessions | Displays whether the instance is refusing new sessions (YES). If this is the case, all requests from new clients are redirected to another instance that is not refusing. |
| Transactions | Total number of requests this instance has serviced since it was started. |
| Active Sessions | Total number of sessions that are still active for the instance. |
| Average Transaction | The average length, in seconds, of this instance's transactions . |
| Average Idle Period | The average amount of time that the instance is idle between requests. |
| Deaths | The number of unexpected failures or deaths this instance has had. These exclude "expected" deaths, which include scheduled shutdowns or a manual shutdowns (using Monitor's interface). |
| Exceptions | If your instance has an uncaught exception, Monitor may record the number of these exceptions here. When there are exceptions, a small blue triangle appears; click this to inspect the messages describing the exceptions. |
| WOStats | Click this button to open a new browser window and view detailed statistics about this instance. See [Accessing the Application Statistics Page](Accessing%20the%20Application%20Statistics%20Page.md#apple-g44damzq) for more information. |
| Config | Click this button to link to the Instance Configuration page for this instance. |
| Delete | Click to remove this instance permanently. Deleting an instance also terminates the instance immediately if it is running. |

In addition, the "Transaction Rate" table indicates the overall transaction rate for the current application. This table reflects the number of transactions that the application as a whole (all of its instances) is servicing per minute and per second.

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Monitoring%20Application%20Activity.md) [!](Monitoring%20Application%20Activity.md) [!](Logging%20and%20Analyzing%20Application%20Activity.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
