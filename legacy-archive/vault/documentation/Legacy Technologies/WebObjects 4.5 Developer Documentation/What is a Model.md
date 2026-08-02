---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.41.html
archived_at: '2026-07-15T08:09:16.646734Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Enterprise%20Objects%20Framework%20Concepts.md) [!](What%20is%20an%20Enterprise%20Object.md) [!](What%20are%20EODisplayGroups%20and%20EOEditingContexts.md)

---

#   What is a Model?

One of the fundamental features of Enterprise Objects Framework is that it maps the data in relational databases to objects. The correspondence between an enterprise object class and stored data is established and maintained by using a _model_
. A model

defines, in entity-relationship terms, the mapping between enterprise object classes and a database.

The following table describes the database-to-object mapping provided in a model:

| __ Database Element__ |   Model Object |   Object Mapping |
| --- | --- | --- |
|   Data Dictionary |   EOModel |   -- |
|   Table |   EOEntity |   Enterprise object class |
|   Column |   EOAttribute |   Enterprise object class instance variable |
|  |  |   (class property) |
|   Row |   -- |   Enterprise object instance |

In addition to storing a mapping between the database schema and enterprise objects, a model file stores information needed to connect to the database server. This connection information includes the name of an adaptor to load so that Enterprise Objects Framework can communicate with the database.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Enterprise%20Objects%20Framework%20Concepts.md) [!](What%20is%20an%20Enterprise%20Object.md) [!](What%20are%20EODisplayGroups%20and%20EOEditingContexts.md)
