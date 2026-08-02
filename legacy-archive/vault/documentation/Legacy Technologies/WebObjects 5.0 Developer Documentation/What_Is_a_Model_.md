---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Concepts/What_Is_a_Model_.html
archived_at: '2026-07-15T08:13:58.309652Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/JavaClient/Images/previous.gif)](What_Is_an__ise_Object_.md)[![Next](attachments/JavaClient/Images/next.gif)](What_Are_EO_ngContexts_.md)

## What Is a Model?

One of the fundamental features of Enterprise Objects Framework
is that it maps the data in relational databases to objects. The
correspondence between an enterprise object class and stored data
is established and maintained by using a model. A model defines,
in entity-relationship terms, the mapping between enterprise object
classes and a database.

The following table describes the database-to-object mapping
provided in a model:

__|  |  |  |
| --- | --- | --- |
| Database element | Model object | Object mapping |__| Data dictionary | EOModel | - |
| Table | EOEntity | Enterprise object class |
| Column | EOAttribute | Enterprise object class instance variable |
|  |  | (class property) |
| Row | - | Enterprise object instance |

In addition to storing a mapping between the database schema
and enterprise objects, a model file stores information needed to
connect to the database server. This connection information includes
the name of an adaptor to load so that Enterprise Objects Framework can
communicate with the database. (WebObjects provides a JDBC adaptor
that allows you to connect to any JDBC-compliant database.)

[![Previous](attachments/JavaClient/Images/previous.gif)](What_Is_an__ise_Object_.md)[![Next](attachments/JavaClient/Images/next.gif)](What_Are_EO_ngContexts_.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
