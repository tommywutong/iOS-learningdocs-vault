---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.40.html
archived_at: '2026-07-15T08:09:16.619538Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Enterprise%20Objects%20Framework%20Concepts.md) [!](Note%20to%20Oracle%20Users.md) [!](What%20is%20a%20Model.md)

---

#   What is an Enterprise Object?

An enterprise object is like any other object, in that it couples data with the methods for operating on that data. However, an enterprise object class has certain characteristics that distinguish it from other classes:

- 

  It has properties that map to stored data; an enterprise object instance typically corresponds to a single row or record in a database.
- 

  It knows how to interact with other parts of the Framework to give and receive values for its properties.

The ingredients that make up an enterprise object are its class definition and the data values from the database row or record with which the object is instantiated. An enterprise object also has a corresponding model that defines the mapping between the class' object model and the database schema.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Enterprise%20Objects%20Framework%20Concepts.md) [!](Note%20to%20Oracle%20Users.md) [!](What%20is%20a%20Model.md)
