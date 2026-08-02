---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/PerformanceTuning.html
archived_at: '2026-07-15T07:56:04.051079Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.md) [!Previous Section](PerformanceTesting.md)

## Improving Performance

Performance is a major concern of website administrators. This section provides a list of areas to check to achieve the maximum possible performance.

- Configure your operating system so that it delivers the best performance possible for your needs. Check your operating system's documentation and your web server's documentation for performance tuning information.
- When possible, use an API-based adaptor in place of the default CGI adaptor.

The API-based adaptors have a performance advantage over CGI adaptors in that the associated server can dynamically load the adaptor; servers using CGI adaptors, on the other hand, spawn a new adaptor process for each request and kill the process after the response is provided.

- Make sure that the applications are written to perform optimally.

The [_WebObjects Developer's Guide_](../DevGuide/DevGuideTOC.md) offers some suggested coding practices to improve performance.

- Enable component-definition caching for all applications.

Component-definition caching is off by default as a convenience for programmers debugging applications. When the application is deployed, component-definition caching should be enabled so that each component's HTML and declarations files are parsed only once per session. Component-definition caching can be enabled programmatically by sending __setCachingEnabled:__ to the WOApplication object (in Java, WebApplication). You can also use the Monitor to enable caching by doing the following:

- In the Declared Apps list, click the inspector button for the application to display the application inspector.
- Click the More button to display the application instance inspector.
- Click the Component caching check box.
- Click the Save Settings button at the bottom of the frame.

- Shut down and restart application instances periodically.

Because no program is ever perfect, WebObjects applications may leak a certain amount of memory per transaction. For this reason, you should periodically shut down and start up each application instance as described in "[Periodically Shutting Down the Application](AppShutdown.md#apple-guytana)" in this guide.

- Perform load balancing or increase the listen queue depth to improve response time for a specific application.

- If the response time is consistently slow, add more application instances so that the load is balanced among those instances. For more information, see the section "[Load Balancing](LoadBalancing.md#apple-guytena)" in this guide.
- If the response time is sometimes acceptable and sometimes slow, consider increasing the size of the listen queue, which holds requests awaiting processing. For more information, see the section "[Increasing the Listen Queue Depth](ListenQueue.md#apple-guytmoi)" in this guide.

- Consider changing the physical configuration of your system.

Determine the size of a single application instance (you can look this up on the application's WOStats page) and multiply that number by the number of instances you intend to run on a given machine. The result is the amount of physical memory that should be installed on that machine.

If you can't add that much physical memory, increase the amount of virtual memory to cover the difference between the physical memory needed and the physical memory you have.

You can also try to reduce the size of the application instance by limiting the amount of state that it stores. Set the session time-out value to ensure that sessions expire after a reasonable length of time. Shut down and restart the application more often to reduce its size.

If you use WebObjects mainly for applications that access a database, you'll achieve the best performance with a dedicated database server and a separate server for WebObjects applications.

[!Table of Contents](ServingWebObjectsTOC.md) [!Next Section](AppShutdown.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
