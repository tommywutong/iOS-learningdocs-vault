---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/BatchFaulting.html
archived_at: '2026-07-15T08:00:54.483978Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Batch Faulting to Improve Performance

##  Synopsis

Describes how to fault several objects at once.

##  Discussion

When you access an Enterprise Object (EO) that has not yet been faulted, Enterprise Objects Frameworks (EOF) issues a query against the database to load in the EO's data. This query loads only the data needed for that particular EO. This mechanism normally increases the efficiency of the framework, but it can sometimes be expensive when faulting multiple records.

Batch faulting instructs EOF to fetch data for several objects if any one of them faults. It is useful if you know that when you fetch a particular relationship, you will also fetch other relationships.

####  Example

In the Movies example database,a Movie has a one-to-one relationship to a PlotSummary. Assume that you have a WOComponent that lets you browse through movies and their summaries in sets of ten. Without using batch faulting, EOF will retrieve the PlotSummary data by making ten separate queries to the database every time the component displays a group of Movies. You can use batch faulting to ensure that every time any one of the PlotSummaries is faulted, nine more are faulted along with it. This can significantly reduce the number of queries against a database.

####  How to Use

The following are three different ways to enable batch faulting.

1. Use EOModel's batch faulting field in the "Advanced Entity" inspector. This is the easiest way to implement batch faulting, but also the least precise, since EOF chooses which faults to batch. Beware of setting this number too high-EOF may generate a SQL statement that is rejected by the database server.

2. Call _EODatabaseContext_
's _batchFetchRelationship:forSourceObjects:editingContext:_
. This will fault all of the objects related to the objects in the SourceObjects array.

3. Use the _EODatabaseContext_
delegate methods _databaseContext:shouldFetchArrayFault:_
and _databaseContext:shouldFetchObjectFault:_
. By selectively returning NO to these methods, you can choose which objects to fault.

####  When Not To Use

Don't use when reducing memory use is more important than increasing database performance. By batch faulting, you may fetch more objects than are needed.

Don't use when you know that all the particular relationships for a series of fetched objects will be faulted. Prefetching is a much more efficient way of doing this.

##  See Also

· Performance Tuning

· Prefetching

##  Questions

· How do I fetch multiple EOFaults at once?

· How can I increase the performance of my fetches?

· How can I minimize database access?

· How can I increase response time?

##  Keywords

· Batch Faulting

· Performance

· Fetching in Batches

· Fetching

##  Revision History

· 1 July, 1998. Paul Haddad. First Draft.

· 2 July, 1998. Paul Haddad. Completed When to Use sentence.

· 5 November, 1998. Clif Liu. Second Draft.

```

```


Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
