---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EODataSource.html
archived_at: '2026-07-15T08:13:46.685666Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EODataSource

> __Inherits from:__ Object

> __Package:__ com.webobjects.eocontrol

---

## Class Description

---

EODataSource is an abstract class that defines a basic API for providing enterprise objects. It exists primarily as a simple means for a display group (EODisplayGroup from EOInterface or WODisplayGroup from WebObjects) or other higher-level class to access a store of objects. EODataSource defines functional implementations of very few methods; concrete subclasses, such as EODatabaseDataSource (defined in EOAccess) and EODetailDataSource, define working data sources by implementing the others. EODatabaseDataSource, for example, provides objects fetched through an EOEditingContext, while EODetailDataSource provides objects from a relationship property of a master object. For information on creating your own EODataSource subclass, see the section ["Creating a Subclass" (page 63)](EODataSource.Concepts.md).

An EODataSource provides its objects with its [fetchObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiyktn52xey3ff5tgk5ddnbhwe2tfmn2hg) method. [insertObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiyktn52xey3ff5uw443foj2e6ytkmvrxi) and [deleteObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiyktn52xey3ff5sgk3dforsu6ytkmvrxi) add and remove individual objects, and [createObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiyktn52xey3ff5rxezlborsu6ytkmvrxi) instantiates a new object. Other methods provide information about the objects, as described below.

## Method Types

---

> Accessing the objects
> [fetchObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiyktn52xey3ff5tgk5ddnbhwe2tfmn2hg)
>
> Inserting and deleting objects
> [createObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiyktn52xey3ff5rxezlborsu6ytkmvrxi)[insertObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiyktn52xey3ff5uw443foj2e6ytkmvrxi)[deleteObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiyktn52xey3ff5sgk3dforsu6ytkmvrxi)
>
> Creating detail data sources
> [dataSourceQualifiedByKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiyktn52xey3ff5sgc5dbknxxk4tdmvixkylmnftgszleij4uwzlz)[qualifyWithRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiyktn52xey3ff5yxkylmnfthsv3jorufezlmmf2gs33oonugs4clmv4q)
>
> Accessing the editing context
> [editingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiyktn52xey3ff5swi2lunfxgoq3pnz2gk6du)
>
> Accessing the class description
> [classDescriptionForObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiyktn52xey3ff5rwyyltoncgk43dojuxa5djn5xem33sj5rguzldorzq)

## Constructors

---

### EODataSource

`public EODataSource()`

Description forthcoming.

---

## Instance Methods

---

### classDescriptionForObjects

`public EOClassDescription classDescriptionForObjects()`

Implemented by subclasses to return an EOClassDescription that provides information about the objects provided by the receiver. EODataSource's implementation returns `null`.

---

### createObject

`public Object createObject()`

Creates a new object, inserts it in the receiver's collection of objects if appropriate, and returns the object. Returns `null` if the receiver can't create the object or can't insert it. You should invoke [insertObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiyktn52xey3ff5uw443foj2e6ytkmvrxi) after this method to actually add the new object to the receiver.

As a convenience, EODataSource's implementation sends the receiver's EOClassDescription a createInstanceWithEditingContext message to create the object. If this succeeds and the receiver has an EOEditingContext, it sends the EOEditingContext an [insertObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiyktn52xey3ff5uw443foj2e6ytkmvrxi) message to register the new object with the EOEditingContext (note that this does _not_ insert the object into the EODataSource). Subclasses that don't use EOClassDescriptions or EOEditingContexts should override this method _without_ invoking __super__'s implementation.

__See Also:__ [classDescriptionForObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiyktn52xey3ff5rwyyltoncgk43dojuxa5djn5xem33sj5rguzldorzq), [editingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiyktn52xey3ff5swi2lunfxgoq3pnz2gk6du)

---

### dataSourceQualifiedByKey

`public abstract EODataSource dataSourceQualifiedByKey(String relationshipKey)`

Implemented by subclasses to return a detail EODataSource that provides the destination objects of the relationship named by _relationshipKey_. The detail EODataSource can be qualified using [qualifyWithRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiyktn52xey3ff5yxkylmnfthsv3jorufezlmmf2gs33oonugs4clmv4q) to set a specific master object (or to change the relationship key). EODataSource's implementation merely throws an exception; subclasses shouldn't invoke __super__'s implementation.

---

### deleteObject

`public abstract void deleteObject(Object anObject)`

Implemented by subclasses to delete _anObject_. EODataSource's implementation merely throws an exception; subclasses shouldn't invoke __super__'s implementation.

---

### editingContext

`public EOEditingContext editingContext()`

Implemented by subclasses to return the receiver's EOEditingContext. EODataSource's implementation returns `null`.

---

### fetchObjects

`public NSArray fetchObjects()`

Implemented by subclasses to fetch and return the objects provided by the receiver. EODataSource's implementation returns `null`.

---

### insertObject

`public abstract void insertObject(Object object)`

Implemented by subclasses to insert _object_. EODataSource's implementation merely throws an exception; subclasses shouldn't invoke __super__'s implementation.

---

### qualifyWithRelationshipKey

`public abstract void qualifyWithRelationshipKey( String key, Object sourceObject)`

Implemented by subclasses to qualify the receiver, a detail EODataSource, to display destination objects for the relationship named _key_ belonging to _sourceObject_. _key_ should be the same as the key specified in the [dataSourceQualifiedByKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiyktn52xey3ff5sgc5dbknxxk4tdmvixkylmnftgszleij4uwzlz) message that created the receiver. If _sourceObject_ is `null`, the receiver qualifies itself to provide no objects. EODataSource's implementation merely throws an exception; subclasses shouldn't invoke __super__'s implementation.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
