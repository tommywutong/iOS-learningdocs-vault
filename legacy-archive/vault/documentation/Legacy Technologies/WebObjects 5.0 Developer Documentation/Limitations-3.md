---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/D2JC/Limitations.html
archived_at: '2026-07-15T08:14:57.684652Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Advantages__nt_Approach.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Guidelines__Java_Client.md)

## Limitations

Direct to Java Client applications share both the advantages
and limitations of Java Client applications. Thus, Direct to Java
Client applications have the disadvantage of requiring more system
administration than HTML-based Web applications.

In addition, Direct to Java Client applications have the advantages
and limitations of Direct to Web. The learning curve is flat until
you need to customize your application; then it becomes very steep.
You need to understand the layer of Direct to Java Client that generates
the user interface in addition to the Java Client technology. Also,
detailed widget placement (moving a text field three pixels to the
right, for example) is harder to do with Direct to Java Client than
it is with regular Java Client and Interface Builder.

Finally, Direct to Java Client applications are a little slower
than static user interfaces. When you start up the application or
open a new type of window, Direct to Java Client has to make round
trips to the server to get the information it needs to assemble
the user interface. It has numerous optimizations to make user interface
generation fast, but it does incur a performance hit.

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Advantages__nt_Approach.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Guidelines__Java_Client.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
