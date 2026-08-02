---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/StartApps.html
archived_at: '2026-07-15T07:56:04.537059Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.md) [!Previous Section](InstallApps.md)

## Starting WebObjects Applications

As described previously, there are two ways to start an application: autostart and manual. Autostarting applications occurs when the user types the application's URL in a web browser; the WebObjects adaptor looks for a running instance of that application and starts one if it cannot find one. Autostarting is not recommended for deployment, It's convenient but when you allow autostarting, it becomes more difficult to monitor the applications progress. Instead, you can use the Monitor application's interface to start applications. (The application will sit idle until a user tries to access it.) Another alternative is to start applications from the command line. You might start from the command line when you need to see the debugging messages written to standard output. This section describes how to manually start an application using the Monitor or the command line.

[!Table of Contents](ServingWebObjectsTOC.md) [!Next Section](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/StartAppsUsingMonitor.html)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
