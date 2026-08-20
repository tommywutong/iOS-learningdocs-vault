---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.1c.html
archived_at: '2026-07-15T08:14:51.448949Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.1b.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.1d.md)

#   Creating Fetch Specifications Programmatically

##  Synopsis

Describes how to create a fetch specification programmatically.

##  Description

EOFetchSpecifications define the way database fetches are performed. They specify such information as the entity to fetch from, which enterprise objects to fetch (a qualifier), the order in which the fetched objects appear (a sort ordering), and other fetch parameters. EOFetchSpecifications are used by an EOEditingContext, the object that actually fetches and maintains the enterprise objects. For more information on fetching, see the programming topics [Fetching with an Editing Context](Fetching%20with%20an%20Editing%20Context.md#apple-ge2tsmzt)
and [Setting a WODisplayGroup's Fetch Specification Programmatically](Setting%20a%20WODisplayGroup%27s%20Fetch%20Specification%20Programmatically.md#apple-gi3tanbu)
.

The simplest type of fetch is unqualified and unordered. For example, to create a fetch specification to fetch all of the Movies in the order they appear in the database you use:

```

EOFetchSpecification fs = new EOFetchSpecification ("Movie",null,null);
```

###  Setting a Qualifier and Sort Ordering

To choose which objects to fetch (for example, to fetch all movies starring Harrison Ford) you need to qualify your fetch using an EOQualifier. The programming topic [Creating EOQualifiers Programmatically](Creating%20EOQualifiers%20Programmatically.md#apple-giytemrr)
discusses how to build an EOQualifier.

To fetch the objects and sort them in a particular order, you need to specify a sort ordering using EOSortOrdering. The programming topic [Creating Sort Orderings](Creating%20Sort%20Orderings.md#apple-gm2tcmbu)
discusses how to build an EOSortOrdering.

When you have a qualifier and a sort ordering, you create the fetch specification using:

```

EOQualifier myQualifier;       // assume existsEOSortOrdering mySortOrdering; // assume existsEOFetchSpecification fs = new EOFetchSpecification     ("Movie",myQualifier,mySortOrdering);
```

###  Other Fetch Parameters

There are several other parameters that you can set to refine the way a fetch is performed.

####  Distinct Fetching

Duplicate records sometimes appear in database fetches, usually when the fetch involves joining multiple tables to satisfy the fetch qualifier. The EOFetchSpecification allows you to specify whether you want these duplicate records with the
setUsesDistinct
method. See the programming topic [Fetching Distinct Results](Fetching%20Distinct%20Results.md#apple-giytqmru)
for more information.

####  Setting a Fetch Limit

By default, when you fetch enterprise objects from a database, all objects that match the fetch criteria are returned. For large databases with lots of records, this can mean that users have to wait while all objects are fetched. To avoid this, you can limit the number of objects fetched. The programming topic [Setting a Fetch Limit](Setting%20a%20Fetch%20Limit.md#apple-gi3domjt)
shows how to do this.

####  Prefetching

Sometimes you know that when you fetch an object, you will always fetch one of its relationships too. By default, EOF fetches the relationship only when you actually traverse it, which results in two fetches (the source object and the relationship). You can improve performance by telling EOF to fetch particular relationships whenever an object is fetched. This is called prefetching and is discussed in the [Prefetching](Prefetching.md#apple-gi2damrr)
programming topic.

##  See Also

- 

  [Fetching with an Editing Context](Fetching%20with%20an%20Editing%20Context.md#apple-ge2tsmzt)
- 

  [Setting a WODisplayGroup's Fetch Specification Programmatically](Setting%20a%20WODisplayGroup%27s%20Fetch%20Specification%20Programmatically.md#apple-gi3tanbu)
- 

  [Creating EOQualifiers Programmatically](Creating%20EOQualifiers%20Programmatically.md#apple-giytemrr)
- 

  [Creating Sort Orderings](Creating%20Sort%20Orderings.md#apple-gm2tcmbu)
- 

  [Fetching Distinct Results](Fetching%20Distinct%20Results.md#apple-giytqmru)
- 

  [Setting a Fetch Limit](Setting%20a%20Fetch%20Limit.md#apple-gi3domjt)
- 

  [Prefetching](Prefetching.md#apple-gi2damrr)

##  Questions

- 

  What is a fetch specification?
- 

  How do I create an fetch specification?
- 

  What does an EOFetchSpecification do?

##  Keywords

- 

  EOFetchSpecification
- 

  Distinct
- 

  Fetch Limit
- 

  Prefetching
- 

  EOQualifier
- 

  EOSortOrdering

##  Revision History

8 March, 1999. Clif Liu. First Draft.

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.1b.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.1d.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
