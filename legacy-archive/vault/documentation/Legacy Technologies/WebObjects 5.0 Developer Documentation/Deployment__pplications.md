---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/SpecialDeploymentIssues/Deployment__pplications.html
archived_at: '2026-07-15T08:12:15.530098Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Special%20Deployment%20Issues.md)[!](Deploying_W_pplications.md)

## Deployment Issues With Java Client Applications

A WebObjects application's developer can produce applications
of two types:

- __HTML-based
  applications__ on which the user interface elements are
  produced using HTML code.
- __Java Client applications__, which use
  Sun's Swing technology to produce a user interface that is more
  appealing and more efficient than HTML-based interfaces. For more
  information on Java Client applications see the WebObjects Java
  Client documentation, available at www.apple.com/developer.

There are two main issues that you should keep in mind when
you deploy and administer Java Client applications:

- __session
  timeout__

  Java Client applications offer the user
  an interface that is very similar to the one offered by regular
  desktop applications. Therefore, they expect Java Client applications
  to behave in a way similar to their desktop applications.

  One
  of the main differences between a desktop application and a Java
  Client application is that Java Client applications open a connection
  to a server-side application. This connection expires after a certain
  period of inactivity. By default, the timeout period is 30 minutes.
  This may not be enough time for an application user that launches
  the application, goes to lunch, and returns to work 45 minutes later.
  When the user tries to use the application (which is still running
  on her computer), she will see a dialog that indicates that her
  session has timed out. In addition, any changes that were not saved
  are lost.
- __traffic level__

  In HTML-based applications,
  the packets sent between the Web browser and the Web server tend
  to be large. However, the size of the packets doesn't vary much
  (the server always sends the entire page to the browser). In Java
  Client applications, the packets sent by the server during application
  startup can be large (the entire application or part of it is downloaded);
  subsequent packets are relatively small (user-entered data and search
  results, for example).

[!](Special%20Deployment%20Issues.md)[!](Deploying_W_pplications.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
