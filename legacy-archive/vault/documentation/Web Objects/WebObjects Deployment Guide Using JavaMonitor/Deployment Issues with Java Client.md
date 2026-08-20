---
title: WebObjects Deployment Guide Using JavaMonitor
apple_id: TP30001009
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Deployment/Deploying_Applications/SpecialDeploymentIssues/SpecialDeploymentIssues.html
archived_at: '2026-07-18T02:16:09.647984Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects Deployment Guide Using JavaMonitor](Introduction%20to%20WebObjects%20Deployment%20Guide%20Using%20JavaMonitor.md)


[Next](Glossary.md)[Previous](JMX%20Monitoring.md)

# Deployment Issues with Java Client

This chapter addresses special issues you need to address when deploying WebObjects applications using Java Client.

A WebObjects application developer can produce applications of two types:

- __Web applications__ on which the user interface elements are produced using HTML code.
- __Java Client applications__, which use Sun’s Swing technology to produce a user interface that is more appealing and more efficient than HTML-based interfaces. For more information on Java Client applications see the WebObjects Java Client documentation, available at [http://www.apple.com/developer](http://www.apple.com/developer).

There are two main issues that you should keep in mind when you deploy and administer Java Client applications:

- __Session timeout__

  Java Client applications offer the user an interface that is very similar to the one offered by regular desktop applications. Therefore, users expect Java Client applications to behave in a way similar to their desktop applications.

  One of the main differences between a desktop application and a Java Client application is that Java Client applications open a connection to a server-side application. This connection expires after a certain period of inactivity. By default, the timeout period is 30 minutes. This may not be enough time for an application user that launches the application, goes to lunch, and returns to work 45 minutes later. When the user tries to use the application (which is still running on her computer), she will see a dialog that indicates that her session has timed out. In addition, any changes that were not saved are lost.
- __Traffic level__

  In Web applications, the packets sent between the web browser and the web server tend to be large. However, the size of the packets doesn’t vary much (the server always sends the entire page to the browser). In Java Client applications, the packets sent by the server during application startup can be large (the entire application or part of it is downloaded); subsequent packets are relatively small (user-entered data and search results, for example).

For more information on WebObjects’s Java Client technology, refer to _[WebObjects Java Client Programming Guide](../WebObjects%20Java%20Client%20Programming%20Guide/Introduction%20to%20WebObjects%20Java%20Client%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjx)_

[Next](Glossary.md)[Previous](JMX%20Monitoring.md)

