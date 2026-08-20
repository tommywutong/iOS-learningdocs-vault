---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/AppShutdown.html
archived_at: '2026-07-15T07:55:53.532204Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.md) [!Previous Section](PerformanceTuning.md)

## Periodically Shutting Down the Application

The longer an application runs, the more memory it consumes. As more memory is consumed, the server machine's performance begins to degrade. For this reason, you may find that performance is greatly improved if you occasionally stop an application instance and start it again.
The Monitor application lets you specify when each application instance should shut down. By default, WebObjects applications never shut down unless you manually shut them down (which you can do by clicking the On/Off switch in the Application Inspector Instance Status field).
To set up periodic application shutdown, do the following:

- In the Application Inspector, click the More button to show the Application Instance Inspector in the bottom frame.
- Scroll down until you see the check box labeled Scheduling Enabled. Click this check box.
- Choose how the application should determine when to shut down and restart. There are several options:

- __Application cycling__. You can have an application terminate itself at the end of a given period of time. To set this up, choose Daily, Weekly, or one of the numerical Hourly settings in the Application Cycling pop-up list, then, if applicable, set the time of day at which you want the application to shut down. (You should choose a time when a minimum number of users is trying to access the application. For example, if all of your users are on the West Coast of North America, you can set the application to shutdown at 2:00AM PST.)

If you want all applications to use the same settings, you can change the default shut-down time on Monitor's Configuration Options page. Press the Options button in the Main Menu and scroll until you see the same application shut-down options as described here. When you change the settings on this page, it affects any applications you add in the future; existing application settings are not affected.

- __Shut down and start at set times__. You can have an application terminate itself and start itself at a given date and time. Check the Future Shutdown check box and enter the time at which the application should shut down. If you want it to restart at a set time as well, click the Future Startup checkbox and enter the time at which you want it to start.

Tip: To have an application instance start up when you start up the Monitor, set it to start at a date in the past. This ensures that a dead instance of that application can be recovered. For example, you might have set an application instance to auto-recover from a shutdown. Suppose that the application crashes at a time when Monitor isn't running (because it has crashed as well). Your instance won't restart because Monitor isn't around to make it restart. If you schedule the application to start in the past, it will start as soon as a Monitor instance starts.

- __Session count__. An application can terminate if the number of active sessions falls below a certain number. Set this number in the Minimum Active Sessions field. Then click the check box labeled Enabled Inactivity Self-Kill.

If Minimum Active Sessions and Enable Inactivity Self-Kill are set, you can, if necessary, click Refuse New Sessions in the Application Inspector at any time while the application is running. When Refuse New Sessions is enabled, the application will not accept any requests from users it does not already know about. After all of the current sessions have expired, the application instance shuts down.

Using the session count to terminate an application is a much more graceful way of shutting down application instances. Scheduled shutdowns will terminate the application no matter how many users are accessing it at that moment. However, if you set Minimum Active Sessions, and Enable Inactivity Self-Kill, it allows all currently active sessions to complete before the application shuts down.

- If you want the application to restart automatically after it is shut down, click the Auto-Recover button in the Application Inspector. If this setting is not enabled, you'll have to manually restart the application instance.
- Click Save Settings.

You can programmatically set up an application to shut down in addition to setting it using the Monitor. If the two settings conflict, the Monitor settings override the application's settings. For more information, see the _[WebObjects Developer's Guide](../DevGuide/DevGuideTOC.md)_.

[!Table of Contents](ServingWebObjectsTOC.md) [!Next Section](LoadBalancing.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
