---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.2c.html
archived_at: '2026-07-15T07:59:56.140863Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.2b.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.2d.md)

##   What is a Model?

One of the fundamental features of Enterprise Objects Framework is that it maps the data in relational databases to objects. The correspondence between an enterprise object class and stored data is established and maintained by using a _model_
. A model

defines, in entity-relationship terms, the mapping between enterprise object classes and a database.

The following table describes the database-to-object mapping provided in a model:

|   Database Element |   Model Object |   Object Mapping |
| --- | --- | --- |
|   Data Dictionary |   EOModel |   -- |
|   Table |   EOEntity |   Enterprise object class |
|   Column |   EOAttribute |   Enterprise object class instance variable |
|  |  |   (class property) |
|   Row |   -- |   Enterprise object instance |

In addition to storing a mapping between the database schema and enterprise objects, a model file stores information needed to connect to the database server. This connection information includes the name of an adaptor to load so that Enterprise Objects Framework can communicate with the database.

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.2b.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.2d.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
