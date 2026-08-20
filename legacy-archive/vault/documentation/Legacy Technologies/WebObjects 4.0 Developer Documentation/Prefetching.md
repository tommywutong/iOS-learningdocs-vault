---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/Prefetching.html
archived_at: '2026-07-15T08:01:25.609491Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Prefetching

##  Synopsis

Describes how to fetch all related objects at once.

##  Discussion

When the Enterprise Objects Framework fetches an object, it creates EOFaults for the object's relationships. Each time you access one of these EOFaults, EOF fetches the data from the database. This procedure works well and minimizes the amount of unneeded data fetching from the database. However, each time an EOFault is accessed, a separate database query is performed. Using a technique called "batch faulting" can reduce the number of database queries. If you know that you will be faulting all instances of a particular relationship, you can use a technique called "prefetching" to skip the EOFault creating stage and produce a single database query to load all related objects.

By using EOFetchSpecification's _setPrefetchingRelationshipKeyPaths_
to specify the key paths of relationships, the Enterprise Objects Framework uses the qualifier of the fetch specification along with the related attributes to perform a joined query against the related objects' table, thereby causing all the appropriate objects to be loaded from the database at once.

####  An Example

A Movie has a to-one relationship to a Studio. Assume that you have a WOComponent that lets you query movies and display all the movies with their studios. Without using prefetching, every time the component displays a group of Movies, the Enterprise Objects Framework makes a separate query to the database to get each Studio. You can use prefetching to ensure that every time the movies are fetched, all the appropriate studios are also fetched. This technique can significantly reduce the number of queries against a database.

####  How to Use Prefetching

Following are two different ways to enable batch faulting:

· Use EOModel's Prefetching tab to specify relationship key paths for a particular fetch specification.

· Send _setPrefetchingRelationshipKeyPaths_
to the fetch-specification object. This method takes an array of strings designating relationship key paths.

####  When to Use Prefetching

You can use prefetching when you know that a particular relationship will always be accessed. It is more instructive, however, to know when _not_
to use prefetching:

· Don't use prefetching when memory usage is more important then database performance.

By prefetching, you may be fetching in more objects than are needed. This will cause your application to use more memory.

· Don't use prefetching when you have fetch limits on a fetch.

Because Prefetching uses the qualifier of the original fetch, it fetches all the related objects, regardless of any limit placed on the original fetch. If you issue a fetch that returns 10,000 records, but use fetch limit to only get 100 of them, the prefetching hint will cause all 10,000 relationships to be fetched.

· Don't use prefetching when doing multiple queries that return the same records.

Using the movie-query screen example described earlier, assume that a user makes a query on all movies that have an "a" in their titles. This would return a large number of movies and would cause several studios to be fetched. Now, if that user does another query using all movies with "e" in their titles, the resulting records would have many of the records previously returned and the Enterprise Objects Framework would refetch several studios. In this case, a batch-faulting mechanism would be more appropriate, since the framework would then fetch only the studios for movies that have an "e" in their names but no "a" since all movies with "a" have had their faults fired.

##  See Also

· Batch Faulting to Improve Performance

· Limit Database Fetches in The WebObjects Developer's Guide

##  Questions

· How do I fetch all related objects at once?

· How can I increase the performance of my fetches?

· How can I minimize database access?

· How can I increase response time?

· When should I not use prefetching?

##  Keywords

· Relationship Key Paths

· Prefetching

· Batch Faulting

· Performance

· Fetching in Batches

· Fetching

##  Revision History

2 July, 1998. Paul Haddad. First Draft.

17 November, 1998. Terry Donoghue. Second Draft.

```

```


Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
