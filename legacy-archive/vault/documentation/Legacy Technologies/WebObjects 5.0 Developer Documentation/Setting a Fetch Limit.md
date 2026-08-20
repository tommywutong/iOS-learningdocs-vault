---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.20.html
archived_at: '2026-07-15T08:14:52.340662Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.1f.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.21.md)

#   Setting a Fetch Limit

##  Synopsis

Describes how to limit the number of rows that are fetched in one query.

##  Description

By default, when you fetch enterprise objects from a database, all objects that match the fetch criteria are returned. For large databases with lots of records, this can mean that users have to wait while all objects are fetched. To avoid this, you can limit the number of objects fetched.

Setting a Fetch Limit with EOModeler

You can set a fetch limit using the fetch specification builder in EOModeler:

Expand the entity containing the fetch specification you wish to limit.

1. 

   Select the fetch specification.
2. 

   Click on the Options tab.
3. 

   Specify the fetch limit.
4. 

   Save your model.

###  Setting a Fetch Limit Programmatically

The EOFetchSpecification property
fetchLimit
and
promptsAfterFetchLimit
control the fetch limit behavior. To set the fetch limit you use the
setFetchLimit
method as shown in the following Java code.

```

EOFetchSpecification fs = new EOFetchSpecification("Movie",null,null);
setFetchLimit(20);
movieArray = this.session().defaultEditingContext().
    objectsWithFetchSpecification(fs);
```

##  See Also

- 

  [Fetching with an Editing Context](Fetching%20with%20an%20Editing%20Context.md#apple-ge2tsmzt)
- 

  [Creating Fetch Specifications Programmatically](Creating%20Fetch%20Specifications%20Programmatically.md#apple-gm4tsmjz)
- 

  [Batch Faulting to Improve Performance](Batch%20Faulting%20to%20Improve%20Performance.md#apple-gm2tmojy)

##  Questions

- 

  How do I limit the number of rows that are fetched?

##  Keywords

- 

  Fetch Limit
- 

  Performance

##  Revision History

4 May, 1998. Kelly Toshach. First Draft.

5 May, 1998. Greg Wilson. Added Synopsis, Questions, and Keywords.

19 March, 1999. Clif Liu. Rewrote second section.

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.1f.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.21.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
