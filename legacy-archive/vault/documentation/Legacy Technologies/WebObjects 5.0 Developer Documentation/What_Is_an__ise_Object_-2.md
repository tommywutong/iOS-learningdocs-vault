---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Concepts/What_Is_an__ise_Object_.html
archived_at: '2026-07-15T08:13:58.345072Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/JavaClient/Images/previous.gif)](Enterprise__rk_Concepts.md)[![Next](attachments/JavaClient/Images/next.gif)](What_Is_a_Model_.md)

## What Is an Enterprise Object?

An enterprise object is like any other object, in that it
couples data with the methods for operating on that data. However,
an enterprise object class has certain characteristics that distinguish
it from other classes:

- It has properties
  that map to stored data; an enterprise object instance typically corresponds
  to a single row or record in a database.
- It knows how to interact with other parts of the Framework
  to give and receive values for its properties.

The ingredients that make up an enterprise object are its
class definition and the data values from the database row or record
with which the object is instantiated. An enterprise object also
has a corresponding model that defines the mapping between the class'
object model and the database schema.

[![Previous](attachments/JavaClient/Images/previous.gif)](Enterprise__rk_Concepts.md)[![Next](attachments/JavaClient/Images/next.gif)](What_Is_a_Model_.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
