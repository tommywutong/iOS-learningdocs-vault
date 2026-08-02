---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.8.html
archived_at: '2026-07-15T08:10:00.977951Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](Viewing%20the%20SQL%20Log.md) [!](Prefetching.md)

#   Batch Faulting to Improve Performance

##  Synopsis

Describes how to fault several objects at once.

##  Discussion

When you access an enterprise object that has not yet been faulted, Enterprise Objects Framework (EOF) issues a query against the database to load in the object's data. This query loads only the data needed for that particular object. This mechanism normally increases the efficiency of the framework, but it can sometimes be expensive when faulting multiple records.

Batch faulting instructs EOF to fetch data for several objects if any one of them faults. It is useful if you know that when you fetch a particular relationship, you will also fetch other relationships.

###  Example

In the Movies example database, a Movie has a one-to-one relationship to a PlotSummary. Suppose you have a WOComponent that lets you browse through movies and their summaries in sets of ten. Without batch faulting, EOF will retrieve the PlotSummary data by making ten separate queries to the database every time the component displays a group of Movies. You can use batch faulting to ensure that every time any one of the PlotSummary objects is faulted, nine more are faulted along with it, significantly reducing the number of queries against the database.

###  How to Use

The following are three different ways to enable batch faulting.

Use EOModel's batch faulting field in the "Advanced Entity" inspector. This is the easiest way to implement batch faulting, but also the least precise, since EOF chooses which faults to batch. Beware of setting this number too high--EOF may generate a SQL statement that is rejected by the database server.

1. 

   Call
   EODatabaseContext
   's
   batchFetchRelationship:forSourceObjects:editingContext:
   . This will fault all of the objects related to the objects in the SourceObjects array.
2. 

   Use the
   EODatabaseContext
   delegate methods
   databaseContext:shouldFetchArrayFault:
   and
   databaseContext:shouldFetchObjectFault:
   . By selectively returning NO to these methods, you can choose which objects to fault.

###  When Not To Use

Don't use batch faulting when reducing memory use is more important than increasing database performance. You may fetch more objects than are needed.

Don't use batch faulting when you know that all the particular relationships for a series of fetched objects will be faulted. Use prefetching instead.

##  See Also

- 

  [Prefetching](Prefetching.md#apple-gi2damrr)

##  Questions

- 

  How do I fetch multiple EOFaults at once?
- 

  How can I increase the performance of my fetches?
- 

  How can I minimize database access?
- 

  How can I increase response time?

##  Keywords

- 

  Batch
- 

  Fault
- 

  Performance
- 

  Fetching

##  Revision History

- 

  1 July, 1998. Paul Haddad. First Draft.
- 

  2 July, 1998. Paul Haddad. Completed When to Use sentence.
- 

  5 November, 1998. Clif Liu. Second Draft.

---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](Viewing%20the%20SQL%20Log.md) [!](Prefetching.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
