---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Administration/Improving_Performance.html
archived_at: '2026-07-15T08:11:56.984019Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Monitoring_Activity.md)[!](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/index.html)

## Improving Performance

Performance is a major concern of website administrators.
This section provides a list of areas to check to achieve the maximum
performance possible.

- Configure
  your operating system so that it delivers the highest performance
  for your needs. Check your operating system's documentation and
  your Web server's documentation for performance-tuning information.
- When possible, use an API-based HTTP adaptor instead of a
  CGI adaptor.
- Make sure that the applications are written to perform optimally.

  The
  WebObjects developer documentation contains coding suggestions that
  help improve the performance of WebObjects applications.
- Enable component-definition caching for all applications.

  When
  applications are deployed, component-definition caching should be
  enabled so that each component's HTML and declarations files are
  parsed only once per session.
- Shut down and restart application instances periodically.

  Scheduling
  instances to shut down and restart periodically increases application performance
  and reliability by reducing the effects of memory leaks. For more
  on scheduling, see ["Scheduling Settings"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iApplication__Properties.html).

  If
  your applications use custom scheduling algorithms to shut down
  themselves, you should not use Monitor's scheduling feature. Instead,
  just use Monitor's auto-recover feature. For more information,
  see ["Auto Recover"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iApplication__Properties.html).
- Consider changing the physical configuration of your system.

  Determine
  the size of a single application instance (you can find this data
  on the application's instance statistics page) and multiply it
  by the number of instances you intend to run on a given computer.
  (For information on the instance statistics page, see ["The Instance Statistics Page"](Monitoring_Activity.md#apple-krifqusfiyytanq).) The result is the amount of physical memory
  needed for that application. You have to add the memory required
  by the operating system, Web server, and any other applications
  that run constantly on the computer. The result is the amount of
  physical memory that should be installed on the computer.
- Try to reduce the size of the application instance by limiting
  the amount of state that it stores. Set the session timeout value
  to ensure that sessions expire after a reasonable length of time.
  See ["WOSessionTimeOut"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iCommand_Line_Arguments.html) for
  details on setting the session timeout interval for application
  instances.
- Make sure that all static content is served by the Web server,
  not your application.

If you use WebObjects Deployment mainly to deploy applications
that access a datasource, you'll achieve the best performance
with a dedicated datasource server and a separate server for WebObjects
applications.

[!](Monitoring_Activity.md)[!](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/index.html)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
