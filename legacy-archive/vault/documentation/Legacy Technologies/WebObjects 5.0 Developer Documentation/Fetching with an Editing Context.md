---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.1a.html
archived_at: '2026-07-15T08:14:51.397874Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.19.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.1b.md)

#   Fetching with an Editing Context

##  Synopsis

Describes how to fetch enterprise objects with an editing context.

##  Discussion

Instead of using a display group to fetch objects, you can fetch enterprise objects directly with an EOEditingContext. Fetching from an EOEditingContext gains you more control over how the objects are fetched and enables you to directly manipulate the object graph. To fetch objects with an editing context involves these steps:

Obtain an editing context.

For WebObjects applications, each session has its own editing context which is obtained by sending the
defaultEditingContext
message to the session:

```

anEditingContext = [[self session] defaultEditingContext];
```


Otherwise you can simply create an editing context.

```

anEditingContext = [EOEditingContext new];
```

1. 

   Create a fetch specification.

The fetch specification is an EOFetchSpecification object that tells EOF which objects you want to fetch and the order they should appear. See the programming topic "Creating Fetch Specifications Programmatically" to find out how to create the fetch specification. An example is given below.

```

aQualifier = [EOQualifier qualifierWithQualifierFormat:    @"lastName = 'Smith'"];aFetchSpecification = [EOFetchSpecification fetchSpecificationWithEntityName:    @"Employee" qualifier: aQualifier sortOrderings:nil];
```

1. 

   Fetch the objects with the editing context.

You use the method
objectsWithFetchSpecification
which returns an array of enterprise objects that meets the fetch specification you have defined.

```

NSArray * results = [anEditingContext    objectsWithFetchSpecification: aFetchSpecification];
```

###  EOUtilities Convenience API

The EOUtilities Application Program Interface (API) is a collection of convenience methods to simplify common operations with EOF. It is implemented as a category on EOEditingContext in Objective-C and as an abstract class in Java. To perform the fetch above using EOUtilities use:

```

NSArray *Smiths = [[[self session] defaultEditingContext]    objectsMatchingValue:@"Smith" forKey:@"lastName"    entityNamed:@"Employee"];
```

##  See Also

- 

  [Creating Fetch Specifications Programmatically](Creating%20Fetch%20Specifications%20Programmatically.md#apple-gm4tsmjz)
- 

  [Setting a WODisplayGroup's Fetch Specification Programmatically](Setting%20a%20WODisplayGroup%27s%20Fetch%20Specification%20Programmatically.md#apple-gi3tanbu)
- 

  EOEditingContext class specification in the _Enterprise Object Framework Reference_

##  Questions

- 

  How do I fetch records from the database?
- 

  How do I use an EOEditingContext to fetch records from the database?

##  Keywords

- 

  EOEditingContext
- 

  Fetch

##  Revision History

20 July, 1998. Winnie Pun. First Draft.

16 November, 1998. Clif Liu. Second Draft.

```

```

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.19.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.1b.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
