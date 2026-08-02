---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Overview/Programming_Java_Client.html
archived_at: '2026-07-15T08:14:38.297472Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/JavaClient/Images/previous.gif)](Java_Client_and_Classes.md)[![Next](attachments/JavaClient/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Creating/index.html)

## Programming With Java Client

Generally, programming a Java Client WebObjects application
requires some skills and knowledge common to both Enterprise Objects
Framework and WebObjects programmers. However, it also requires
a specific design technique: object partitioning.

Objects on the server and the client can be instances of custom
classes or generic enterprise objects (EOGenericRecord). Objects
that derive from custom subclasses can have different sets of properties
on both the server and the client. Usually, client objects have
the more restricted set of data and behaviors, but it is really
up to you to decide based on the requirements of the application
and your business. As noted earlier, the primary criteria for partitioning
are performance and security. For more on object partitioning see ["Getting Your Project Ready to Receive Custom Classes"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Enhancing/iAdding_Beha_ise_Objects.html) and ["Distributing Business Logic in Java Client Applications"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Enhancing/iAdding_Beha_ise_Objects.html).

[![Previous](attachments/JavaClient/Images/previous.gif)](Java_Client_and_Classes.md)[![Next](attachments/JavaClient/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Creating/index.html)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
