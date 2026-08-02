---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-44.html
archived_at: '2026-07-15T08:05:00.777763Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Administrative%20Tasks.md) [!](Playing%20Back%20a%20Session.md) [!](Automatic%20Scheduling.md)

---

# Improving Performance

Performance is a major concern of web site administrators. This section provides a list of areas to check to achieve the maximum possible performance.

- Configure your operating system so that it delivers the best performance possible for your needs. Check your operating system's documentation and your web server's documentation for performance tuning information.
- When possible, use an API-based adaptor in place of the default CGI adaptor.

> The API-based adaptors have a performance advantage over CGI adaptors in that the associated server can dynamically load the adaptor; servers using CGI adaptors, on the other hand, spawn a new adaptor process for each request and kill the process after the response is provided.

- Make sure that the applications are written to perform optimally.

> The _WebObjects Developer's Guide_
> offers some suggested coding practices to improve performance.

- Enable component-definition caching for all applications.

Component-definition caching is off by default as a convenience for programmers debugging applications. When the application is deployed, component-definition caching should be enabled so that each component's HTML and declarations files are parsed only once per session. Component-definition caching can be enabled programmatically by sending __setCachingEnabled:__
to the WOApplication object (in Java, WebApplication). You can also use the Monitor to enable caching by doing the following:

1. Click "Applications" in the Monitor banner.
2. Click the Config button in the row corresponding to the application for which you want to enable component-definition caching.
3. Click New Instance Defaults.
4. Ensure that Caching Enabled is checked.
5. Click Update for New Instances, or ensure that the left-hand checkbox is also checked and click Update for New and Existing Instances.

- Shut down and restart application instances periodically.
> Because no program is ever perfect, WebObjects applications may leak a certain amount of memory per transaction. For this reason, you should periodically shut down and start up each application instance as described in "[Automatic Scheduling](Automatic%20Scheduling.md#apple-geytgnzt)" in this guide.

- Perform load balancing or increase the listen queue depth to improve response time for a specific application.

- If the response time is consistently slow, add more application instances so that the load is balanced among those instances. For more information, see the section "[Load Balancing](Load%20Balancing.md#apple-gmytsmrq)" in this guide.
- If the response time is sometimes acceptable and sometimes slow, consider increasing the size of the listen queue, which holds requests awaiting processing. For more information, see the section "[Increasing the Listen Queue Depth](Increasing%20the%20Listen%20Queue%20Depth.md#apple-geztqmzw)" in this guide.

- Consider changing the physical configuration of your system.
> Determine the size of a single application instance (you can look this up on the application's WOStats page) and multiply that number by the number of instances you intend to run on a given machine. The result is the amount of physical memory that should be installed on that machine.

> If you can't add that much physical memory, increase the amount of virtual memory to cover the difference between the physical memory needed and the physical memory you have.

- Try to reduce the size of the application instance by limiting the amount of state that it stores. Set the session time-out value to ensure that sessions expire after a reasonable length of time. Shut down and restart the application more often to reduce its size.

If you use WebObjects mainly for applications that access a database, you'll achieve the best performance with a dedicated database server and a separate server for WebObjects applications.

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Administrative%20Tasks.md) [!](Playing%20Back%20a%20Session.md) [!](Automatic%20Scheduling.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
