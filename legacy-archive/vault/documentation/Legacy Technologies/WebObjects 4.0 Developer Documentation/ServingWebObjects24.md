---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects24.html
archived_at: '2026-07-18T01:23:40.957709Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects23.md)

### Obtaining Information From Monitor

The Applications page gives an overall view of a deployment. It shows which applications are configured, how many instances each application has, and which of these is currently running. You get to the Applications page by clicking the Applications button in Monitor's banner. A screen similar to the following example is displayed:

!

Click a hyperlink in the Application column to start a session with an instance of that application.
The Application Detail View page of the Monitor application provides you with detailed information about all configured instances of a WebObjects application. Click the Detail View button next to an application in the Applications page to go to the detail page, which looks similar to the following example:

!

At the top of the page is the title of the application. When one or more instances of an application are running then, this title becomes a hyperlink. Clicking on the hyperlink opens a new browser window and connects to the running application.
The tables of the Application Detail View contain various information and controls:

|  Column |  Description |
|  Host / Port |  The host name and the port that the instance runs on. If the instance is running, this information is hyperlinked; clicking starts a new session with the instance. |
|  Status |  Indicates whether the instance is running (ON) or is stopped (OFF). Clicking this control starts and stops the instance (see "[Starting and Stopping an Application Instance](ServingWebObjects20.md#apple-gyzdmna)" for details). |
|  Schedule |  Indicates whether scheduling is enabled. When ON is displayed, the Status, Auto-Recover, and Refuse New Sessions indicators are disabled; scheduling is responsible for setting all of those states on a schedule basis. See "[Automatic Scheduling](ServingWebObjects30.md#apple-guytana)" for information on scheduling. |
|  Auto-Recover |  Displays the Auto-Recover setting for this instance. ON indicates that Monitor should start a new instance upon failure or shutdown of an instance. You can set this state when you configure the instance (see "[Setting Command-Line Arguments in Monitor](ServingWebObjects22.md#apple-gy3tmoa)"). |
|  Refuse New Sessions |  Displays whether the instance is refusing new sessions (YES). If this is the case, all requests from new clients are redirected to another instance that is not refusing. |
|  Statistics. |  Statistics. |
|  Transactions |  Total number of requests this instance has serviced since it was started. |
|  Active Sessions |  Total number of sessions that are still active for the instance. |
|  Average Idle Period |  the average amount of time that the instance is idle between requests. |
|  Deaths |  The number of unexpected failures or deaths this instance has had. These exclude "expected" deaths, which include scheduled shutdowns or a manual shutdowns (using Monitor's interface). |
|  Exceptions |  If your instance has an uncaught exception, Monitor may record the number of these exceptions here. When there are exceptions, a small blue triangle appears; click this to inspect the messages describing the exceptions. |
|  WOStats |  Click this button to open a new browser window and connect to the WOStats direct action to view detailed statistics about this instance. |
|  Config |  Click this button to link to the Instance Configuration page for this instance. |
|  Delete |  Click to remove this instance permanently. Deleting an instance also terminates the instance immediately if it is running. |
|  Transaction Rate |  This small table indicates the overall transaction rate for the current application. This table reflects the number of transactions that the application as a whole (all of its instances) is servicing per minute and per second. |

```
```

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects25.md)
