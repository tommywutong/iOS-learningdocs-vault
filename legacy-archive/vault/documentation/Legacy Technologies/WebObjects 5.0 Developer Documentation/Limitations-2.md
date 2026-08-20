---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/JavaClient/Limitations.html
archived_at: '2026-07-15T08:15:12.189354Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Advantages__nt_Approach.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Guidelines__Java_Client.md)

## Limitations

Java Client applications compare very favorably to traditional
desktop applications and other distributed, multitier, Java-based
architectures. They compare favorably to an HTML-based approach,
too, but you trade some of the advantages of an HTML-based application
for an improved user interface.

The client portion of a Java Client application can take the
form of an application or an applet. The trade-offs are different
with each. Providing the client portion as an application requires
more system administration than using an HTML-based approach. HTML-based Web
applications require no software installations on client systems.
Users need only a Web browser to access the applications. With Java
Client applications, however, the application should usually be
pre-installed on client machines.

The alternative to providing the client portion as an application
is providing it as an applet that runs in a browser. The system
administration requirements of this approach are comparable to those
of HTML-based Web applications: no client installations are required. Instead
of running a preinstalled application, users transparently download
an applet to a browser in which the applet runs. This download,
however, is the disadvantage of using an applet. No matter how simple
the Java Client user interface is, the size of the applet is considerable.
Thus, it takes longer for a Java Client applet to start up than
for a Java Client application; and the slower the client's connection
is, the longer it takes for the applet to start up.

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Advantages__nt_Approach.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Guidelines__Java_Client.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
