---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.9.html
archived_at: '2026-07-15T08:14:54.752437Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.8.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.a.md)

#   Prefetching

##  Synopsis

Describes how to fetch all related objects at once.

##  Discussion

When the Enterprise Objects Framework (EOF) fetches an enterprise object, it creates EOFault objects for the enterprise object's relationships. Each time you access one of these EOFaults, EOF fetches the data from the database. This procedure works well and minimizes the amount of unneeded data fetching from the database. However, each time an EOFault is accessed, a separate database query is performed. Using a technique called "batch faulting" can reduce the number of database queries. If you know that you will be faulting all instances of a particular relationship, you can use a technique called "prefetching" to skip the EOFault creating stage and produce a single database query to load all related objects.

By using EOFetchSpecification's
setPrefetchingRelationshipKeyPaths
to specify the key paths of relationships, the Enterprise Objects Framework uses the qualifier of the fetch specification along with the related attributes to perform a joined query against the related objects' table, thereby causing all the appropriate objects to be loaded from the database at once.

###  An Example

A Movie has a to-one relationship to a Studio. Suppose that you have a WOComponent that lets you query movies and display all the movies with their studios. Without using prefetching, every time the component displays a group of Movies, EOF makes a separate query to the database to get each Studio. You can use prefetching to ensure that every time the movies are fetched, all the appropriate studios are also fetched, significantly reducing the number of database queries.

###  How to Use Prefetching

Following are two different ways to enable prefetching:

- 

  Use EOModeler's Prefetching tab to specify relationship key paths for a particular fetch specification.
- 

  Send
  setPrefetchingRelationshipKeyPaths
  to the fetch-specification object. This method takes an array of strings designating relationship key paths.

###  When to Use Prefetching

You can use prefetching when you know that a particular relationship will always be accessed. It is more instructive, however, to know when _not_
to use prefetching:

- 

  Don't use prefetching when memory usage is more important then database performance.

By prefetching, you may fetch in more objects than you need, and thus waste memory.

- 

  Don't use prefetching when you have fetch limits on a fetch.

Because prefetching uses the qualifier of the original fetch, it fetches all the related objects, regardless of any limit placed on the original fetch. If you issue a fetch that returns 10,000 records, but use fetch limit to only get 100 of them, the prefetching hint will cause all 10,000 relationships to be fetched.

- 

  Don't use prefetching when performing multiple queries that return the same records.

Using the movie-query screen example described earlier, suppose that a user makes a query for all movies that have the letter "a" in their titles. This returns a large number of movies and causes several studios to be fetched. If the user does another query for all movies with the letter "e" in their titles, the resulting records will overlap those previously fetched and EOF will refetch several studios. In this case, batch-faulting is more appropriate; all of the movies with the letter "a" in their names have had their faults fired and EOF fetches only the studios for movies containing the letter "e" and not the letter "a" in their names.

##  See Also

- 

  [Batch Faulting to Improve Performance](Batch%20Faulting%20to%20Improve%20Performance.md#apple-gm2tmojy)
- 

  [Setting a Fetch Limit](Setting%20a%20Fetch%20Limit.md#apple-gi3domjt)

##  Questions

- 

  How do I fetch all related objects at once?
- 

  How can I increase the performance of my fetches?
- 

  How can I minimize database access?
- 

  How can I increase response time?
- 

  When should I not use prefetching?

##  Keywords

- 

  Relationship
- 

  Key
- 

  Path
- 

  Prefetching
- 

  Batch
- 

  Fault
- 

  Fetching

##  Revision History

2 July, 1998. Paul Haddad. First Draft.

17 November, 1998. Terry Donoghue. Second Draft.

```

```

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.8.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.a.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
