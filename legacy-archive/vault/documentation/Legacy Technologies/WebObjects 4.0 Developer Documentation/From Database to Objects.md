---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/WhatsEOF2.html
archived_at: '2026-07-18T01:19:49.462913Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](What%20Is%20Enterprise%20Objects%20Framework.md) [!Previous Section](The%20Enterprise%20Objects%20Framework%20Difference.md)

# From Database to Objects

Enterprise Objects Framework's database-to-objects mapping sets up a correspondence between database tables and enterprise objects classes so that database rows map to instances of the appropriate class as shown in [Figure 2](#apple-geydeobx).

!

Figure 2. Mapping Between an Enterprise Object Class and a Single Table

The mapping is flexible. For example:

- You can map an enterprise object to a single table, a subset of a table, or to more than one table. For instance, a Person object can get its first and last names from a PERSON table but get its street address, city, state and zip code from an ADDRESS table.
- Generally an enterprise object instance variable maps to a single column, but the column-to-instance variable correspondence is similarly flexible. You can map an instance variable to a derived column, such as "price \* discount" or "salary \* 12".
- You can map an enterprise object inheritance hierarchy to one or more database tables.

In addition to mapping tables to enterprise object classes and database columns to instance variables, the Framework maps database primary and foreign keys to relationships between objects. The Framework defines two types of relationships-to-ones and to-manys-which are both illustrated in [Figure 3](#apple-gyztkma). The relationship a MovieRole has to its Movie is a to-one relationship, while the relationship a Movie has to its MovieRoles is a to-many.

!

Figure 3. Mapping Relationships

For more information on database-to-objects mappings, see the chapter ["Designing Enterprise Objects"](Designing%20Enterprise%20Objects.md#apple-ge2daobr), and to learn how to define this mapping with the EOModeler application, see the book _Enterprise Objects Framework Tools and Techniques_.

## Uniquing

In marrying relational databases to object-oriented programming, one of the key requirements is that a row in the database be associated with only one enterprise object in a given context in your application. Enterprise Objects Framework maintains the mapping of each enterprise object to its corresponding database row, and uses this information to ensure that your object graph does not have two (possibly inconsistent) objects for the same database row. _Uniquing_ of enterprise objects, as this process is called, limits memory usage and allows you to know with confidence that the object you're interacting with represents the true state of its associated row as it was last fetched into the object graph.
Without uniquing, you'd get a new enterprise object every time you fetch its corresponding row, whether explicitly or through resolution of relationships. This is illustrated in [Figure 4](#apple-gy4dgoa).

!

Figure 4. Uniquing of Enterprise Objects

## Resolution of Relationships and Faulting

When the Framework fetches an object, it creates objects representing the destinations of the fetched object's relationships. For example, if you fetch an employee object, you can ask for its manager and immediately receive an object; you don't have to get the manager's employee ID from the object you just fetched and fetch the manager yourself.
The Framework doesn't immediately fetch data for the destination objects of relationships, however. Fetching is fairly expensive, and further, if the Framework fetched objects related to the one explicitly asked for, it would also have to fetch the objects related to those, and so on, until all of the interrelated rows in the database had been retrieved. To avoid this waste of time and resources, the destination objects created are stand-ins, called _faults_, that fetch their data the first time they're accessed. [Figure 5](#apple-gy4dani) illustrates this process.

The framework allows you to tune relationship resolution by _prefetching_ relationships and _batch faulting_. For more information on these features, see the chapter["Answers to Common Design Questions"](Answers%20to%20Common%20Design%20Questions.md#apple-g44tkoa). For more information on the general faulting mechanism, see the chapter ["Behind the Scenes"](Behind%20the%20Scenes.md#apple-ha2tqni).

!

Figure 5. Resolution of a Fault

[!Table of Contents](What%20Is%20Enterprise%20Objects%20Framework.md) [!Next Section](From%20Objects%20to%20Interface.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
