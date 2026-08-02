---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.a.html
archived_at: '2026-07-15T08:10:01.047438Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](Prefetching.md) [!](Mixing%20Languages%20in%20an%20Application.md)

#  Caching an Entity's Objects

##  Synopsis

Describes how to cache data from reference tables so that applications don't have to keep fetching the tables from the database and comparing them to what's in memory. For example, you could cache a RentalTerms table whose rows are used to populate a popup list.

##  Description

You can set an entity to cache its enterprise objects in memory. This caching allows Enterprise Objects Framework to evaluate queries in memory, thereby avoiding round trips to the database. This is most useful for read-only entities, where there is no danger of the cached data getting out of sync with database data. Additionally, this technique should only be used with small tables, since it fetches all of an entity's enterprise objects into memory the first time any object of this entity is needed from the database.

For example, using the sample Rentals database, you might cache the entity RentalTerms. RentalTerms objects specify check out length, cost, and deposit amount for different types of rentals--new release movies, video games, and laser discs, for example. Since the set of all RentalTerms enterprise objects is fairly small, is essentially read-only, and is used very frequently, RentalTerms is a good candidate for entity caching.

###  Setting an Entity to Cache Objects

Using EOModeler, check the Cache in Memory option in the Advanced Entity Inspector for the entity, or to set it programmatically, use the EOEntity method
setCachesObjects
(
setCachesObjects:
in Objective C).

###  Limitations

- 

  An entity's cache of objects is maintained per EODatabaseContext. Consequently, a WebObjects application that establishes separate database connections for each session, for example, so each user can connect with a different database username and password, does not get the same performance benefits from entity caching that other applications can.
- 

  The relationships of a cached object are not automatically cached. For example, consider an application that makes conference room reservations. This application has a ConferenceRoom entity with a relationship to a Building entity. Since a company's set of conference rooms and buildings is fairly small and fixed, it makes sense to cache both these entity's. You can either set both entities to cache their objects or you can set ConferenceRoom's relationship to Building to prefetch its destination objects.
- 

  If you need to apply qualifiers to cached data, be aware that evaluating a qualifier in memory is frequently slower than refetching the data from the database when the qualifier is large or is applied to many objects.

##  See Also

##  Questions

- 

  How do I keep from fetching the same data over and over again?
- 

  How do I cache commonly accessed objects?
- 

  How do I cache data from reference tables?
- 

  Why are enterprise objects from my cached entity still being faulted in?

##  Keywords

- 

  Entity
- 

  Cache
- 

  Tables
- 

  Performance

##  Revision History

4 May, 1998. Kelly Toshach. First Draft.

5 May, 1998. Greg Wilson. Added Synopsis, Questions, and Keywords.

---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](Prefetching.md) [!](Mixing%20Languages%20in%20an%20Application.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
