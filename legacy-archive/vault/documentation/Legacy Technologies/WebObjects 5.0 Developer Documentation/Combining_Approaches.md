---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/ChoosingYourApproach/Combining_Approaches.html
archived_at: '2026-07-15T08:14:56.192335Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Rapid_Devel_siderations.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Summary.md)

## Combining Approaches

WebObjects does not confine you to a single approach. You
can switch your approach as you develop your application or combine
it with another approach. This is possible in WebObjects because
the business logic is encapsulated in enterprise objects and not
in the application.

### Combining HTML-based and Java Client Approaches

In general, you shouldn't combine a HTML-based approach
(WebObjects HTML-based or Direct to Web) with a Java Client approach
(Java Client or Direct to Java Client) because the combination has
none of the advantages and all of the drawbacks of the individual approaches.
The speed and interactivity of their user interfaces are major advantages
of Java Client applications. These advantage are lost when the applications
also use inherently less-interactive HTML-based interfaces.

Similarly, a major advantage of HTML-based applications is
that any computer with a Web browser can use them. When combined
with Java Client, these applications depend on the quality of the
browser's Java Virtual Machine, if the browser even implements
one. In addition, you must install the client code on the user's
computer or force the user to wait for it to download. The extra
interactivity Java Client adds to the HTML-based approaches is usually
outweighed by the concomitant loss of portability.

### Adding Rapid Development

The WebObjects HTML-based and Direct to Web approaches can
be combined in many ways. You can start with a Direct to Web application,
freeze and customize pages, and add your own pages. You can also
start with a HTML-based application and link its components with
Direct to Web pages.

Direct to Web also provides reusable components, of which
the edit and list components are used the most. If your application
employs forms and lists that work with enterprise objects, these
components can save you a tremendous amount of time.

You can also mix Java Client and Direct to Java Client applications.
If you're developing a Java Client application and you need a
Direct to Java Client controller (a window that edits an enterprise
object, for example), you can easily instantiate one. Also, you
can freeze an interface in Direct to Java Client and edit it with
Interface Builder.

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Rapid_Devel_siderations.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Summary.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
