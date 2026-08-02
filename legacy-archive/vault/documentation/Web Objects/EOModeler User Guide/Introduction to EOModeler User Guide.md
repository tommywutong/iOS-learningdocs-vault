---
title: EOModeler User Guide
apple_id: TP30001018
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: WebObjects
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/UsingEOModeler/Introduction/Introduction.html
archived_at: '2026-07-18T02:21:55.727211Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Data%20Modeling%20and%20EOModeler.md)

# Introduction to EOModeler User Guide

The Enterprise Object technology brings the benefits of object-oriented programming to database application development. You can use Enterprise Objects to build feature-rich database applications that encapsulate your business logic yet are independent of any particular data source.

One of the most significant problems developers face when using object-oriented programming languages with relational databases is the difficultly of matching relational database tables with the flexibility afforded by objects.

The Enterprise Object technology solves this problem by providing tools for defining an object model and mapping it to a data model. This allows you to create objects that encapsulate both the data and the methods for operating on that data, while taking advantage of the data-access services provided by Enterprise Objects.

This book teaches you how to use EOModeler to build the data models you need to use Enterprise Objects. With EOModeler, you can build data models based on existing data sources or you can build data models from scratch, which you then use to create data structures (tables, columns, joins) in a data source.

This book is an in-depth guide on how to use EOModeler. It does not provide an introduction to the Enterprise Object technology or to WebObjects. Instead, it is meant as supplement to the other introductory WebObjects documentation and also as a general reference guide to EOModeler.

Some features of EOModeler, such as schema synchronization, SQL generation, and Java class file generation are not discussed in this book. These features are best understood in the context of a specific application and so are discussed in the Inside WebObjects series books _Web Applications_ and _Java Client Desktop Applications_.

This book assumes some familiarity with relational databases and with Enterprise Objects. If you’re new to WebObjects and Enterprise Objects, it is recommended that you start with one of the tutorial-based books, either _Web Applications_ or _Java Client Desktop Applications_ depending on the kind of application development you are doing. These books provide conceptual introductions to Enterprise Objects and provide contexts in which to best learn about the technology.

Then, after you’ve read through the introductory material, you’ll probably have questions about advanced data modeling techniques or how to use the advanced features of EOModeler. At that point, you are ready for the information in this book.

The book includes these chapters:

- [Data Modeling and EOModeler](Data%20Modeling%20and%20EOModeler.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjyfvbuqmrqgiwviubr) provides an introduction to data modeling concepts and introduces the data modeling tool provided by WebObjects, called EOModeler.
- [Using EOModeler](Using%20EOModeler.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjyfvbuqmrqgmwviubr) introduces the major user interface elements of EOModeler and teaches you how to use the application.
- [Working With Attributes](Working%20With%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjyfvbuqmrqgqwviubr) teaches you how to work with entity attributes in EOModeler. It describes how to configure attribute characteristics, how to use prototype attributes, and how to flatten attributes.
- [Working With Relationships](Working%20With%20Relationships.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjyfvbuqmrqguwviubr) provides an introduction to relationships between entities. It teaches you how to add and configure relationships in EOModeler, how to specify referential integrity rules in relationships, how to flatten relationships, and how to configure many-to-many relationships.
- [Working With Entities](Working%20With%20Entities.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjyfvbuqmrqgywviubr) teaches you how to work with entities in EOModeler. It describes how to configure entity characteristics in EOModeler, how to configure entities for use in a shared editing context, and how to work with stored procedures in EOModeler.
- [Modeling Inheritance](Modeling%20Inheritance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjyfvbuqmrqg4wviubr) introduces entity inheritance in Enterprise Objects. It describes the three types of entity inheritance and how to model each type using EOModeler.
- [Working With Fetch Specifications](Working%20With%20Fetch%20Specifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjyfvbuqmrqhawviubr) describes how to configure fetch specifications in EOModeler and how to use these fetch specifications programmatically.

You can find further documentation for WebObjects and Enterprise Objects in three places:

- Project Builder’s Developer Help Center, accessible through the Help menu
- Apple’s WebObjects documentation website: [http://developer.apple.com/documentation](https://developer.apple.com/documentation)
- the WebObjects CD-ROM, which contains the WebObjects API reference, various documents in HTML and PDF, examples, what’s new, and legacy documentation
[Next](Data%20Modeling%20and%20EOModeler.md)

