---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/EditingContext.html
archived_at: '2026-07-15T08:01:10.077803Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Fetching with an Editing Context

##  Synopsis

Describes how to fetch enterprise objects with an editing context.

##  Discussion

Instead of using a display group to fetch objects, you can fetch enterprise objects directly with an EOEditingContext. Fetching from an EOEditingContext gains you more control over how the objects are fetched and enables you to directly manipulate the object graph. To fetch objects with an editing context involves these steps:

1. Obtain an editing context.

For WebObjects applications, each session has its own editing context which is obtained by sending the _defaultEditingContext_
message to the session:

```
anEditingContext = [[self session] defaultEditingContext];
```


2. Specify the qualifier.

To fetch the objects, you must create a qualifier that specifies what objects are qualified for this fetch. For example, to specify that all people having a lastName of "Smith" are qualified to be fetched, use:

```
aQualifier = [EOQualifier qualifierWithQualifierFormat:@"lastName = 'Smith'"];
```


3. Build the fetch specification.

Once the qualifier is created, you build the fetch specification. A basic fetch specification defines the entity to which this fetch is targeted, what objects are qualified for the fetch, and the order in which the fetched objects are sorted.

```
aFetchSpecification = [EOFetchSpecification fetchSpecificationWithEntityName: @"Document" qualifier: aQualifier sortOrderings:nil];
```


More details of the fetch specification can be specified by invoking the appropriate method to the fetch specification. For example, if you want existing objects to be overwritten with fetched values when they have been updated or changed, you can invoke _setRefreshesRefetchedObjects:YES_
on _aFetchSpecification_
.

When the fetch specification is built, you can fetch the objects from the editing context with the method _objectsWithFetchSpecification_
.

```
NSArray * results = [aEditingContext objectsWithFetchSpecification: aFetchSpecification];
```


The results of this fetch is a an array of Enterprise Objects that meets the fetch specification you defined.

####  EOUtilities Convenience API

The EOUtilities Application Program Interface (API) is a collection of convenience methods to simplify common operations with EOF. It is implemented as a category on EOEditingContext in Objective-C and as an abstract class in Java. To perform the fetch above using EOUtilities use:

```
NSArray *Smiths = [[[self session] defaultEditingContext]  objectsMatchingValue:@"Smith" forKey:@"lastName" entityNamed:@"document"];
```


##  See Also

· Creating Sort Orderings

· Fetching Distinct Results

· EOEditingContext

##  Questions

· How do I fetch records from the database?

· How do I use an EOEditingContext to fetch records from the database?

##  Keywords

· Editing Context

· Fetch

##  Revision History

20 July, 1998. Winnie Pun. First Draft.

16 November, 1998. Clif Liu. Second Draft.

```

```


Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
