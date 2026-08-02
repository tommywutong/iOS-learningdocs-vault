---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/ChoosingYourApproach/User_Interf_equirements.html
archived_at: '2026-07-15T08:14:56.294844Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Internet_an__Deployment.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Rapid_Devel_siderations.md)

## User Interface Requirements

The WebObjects development approaches differ in the richness
and response times of the user interfaces and the ease in which
you can make user interfaces with specific layout and flow requirements.

### Rich Widget Selection and Fast Response Times

The Java Client and Direct to Java Client approaches offer
user interfaces with multiple windows and a large selection of widgets,
features commonly found in client-server applications. If your application
needs these features, you should use one of these approaches. The
HTML user interface used by the WebObjects HTML-based and Direct
to Web approaches offers much more limited possibilities.

When you need fast response times from your user interface
(if you're displaying and updating real time data, for example),
you should use the Java Client or Direct to Java Client approaches.
The user's computer manages the highly interactive user interface.

The drawback of the Java Client approaches is you need to
be sure the client code is on the user's computer when the user
runs your application. You can either install it on the user's computer
in advance like a standalone application, which can be inconvenient,
or download it as an applet, which can take a long time.

### Specific Layout and Flow Requirements

If you plan to create an HTML application with specific page
design and flow requirements, you should use the WebObjects HTML
approach. The alternative, Direct to Web, creates applications with
a predefined structure that limits the user interface's flexibility.
Direct to Web is highly customizable, but you need to have a strong understanding
of WebObjects before you can effectively customize the flow of a
Direct to Web application.

Your decision is similar if your application needs the rich
and fast user interface the Java Client approaches offer. If the
user interface has specific layout and flow requirements, you should
use the Java Client approach over the Direct to Java Client approach.

Keep in mind that the Direct to Java Client approach-including
the user interface it generates-is designed expressly for viewing
and editing databases, especially large ones. If your application
requires this capability, you will probably find Direct to Java
Client's user interface extremely well-suited for the task.

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Internet_an__Deployment.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Rapid_Devel_siderations.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
