---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EODataSource.html
archived_at: '2026-07-15T08:11:39.590423Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EODataSource

> **__Inherits
> from:__**
> : NSObject

> **__Conforms to:__**
> : NSObject
> : (NSObject)

> __Declared in:__ : EOControl/EODataSource.h

---

## Class Description

---

EODataSource is an abstract class that defines a basic API
for providing enterprise objects. It exists primarily as a simple
means for a display group (EODisplayGroup from EOInterface or WODisplayGroup
from WebObjects) or other higher-level class to access a store of
objects. EODataSource defines functional implementations of very
few methods; concrete subclasses, such as EODatabaseDataSource (defined
in EOAccess) and EODetailDataSource, define working data sources by
implementing the others. EODatabaseDataSource, for example, provides
objects fetched through an EOEditingContext, while [EODetailDataSource](EODetailDataSource-2.md#apple-ineeurcdjjbus) provides objects
from a relationship property of a master object. For information
on creating your own EODataSource subclass, see the section ["Creating a Subclass"](EODataSource-4.md#apple-ineeurckjbdem).

An EODataSource provides its objects with its [fetchObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcu3povzggzjpmzsxiy3ij5rguzldorzq) method. [insertObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcu3povzggzjpnfxhgzlsorhwe2tfmn2du) and [deleteObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcu3povzggzjpmrswyzlumvhwe2tfmn2du) add
and remove individual objects, and [createObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcu3povzggzjpmnzgkylumvhwe2tfmn2a) instantiates a new object.
Other methods provide information about the objects, as described
below.

## Method Types

---

> **Accessing the objects**
> : [- fetchObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcu3povzggzjpmzsxiy3ij5rguzldorzq)
>
> **Inserting and deleting
> objects**
> : [- createObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcu3povzggzjpmnzgkylumvhwe2tfmn2a)
> : [- insertObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcu3povzggzjpnfxhgzlsorhwe2tfmn2du)
> : [- deleteObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcu3povzggzjpmrswyzlumvhwe2tfmn2du)
>
> **Creating detail data
> sources**
> : [- dataSourceQualifiedByKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcu3povzggzjpmrqxiyktn52xey3fkf2wc3djmzuwkzccpffwk6j2)
> : [- qualifyWithRelationshipKey:ofObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcu3povzggzjpof2wc3djmz4vo2lunbjgk3dboruw63ttnbuxas3fpe5g6zspmjvgky3uhi)
>
> **Accessing the editing
> context**
> : [- editingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcu3povzggzjpmvsgs5djnztug33oorsxq5a)
>
> **Accessing the class description**
> : [- classDescriptionForObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcu3povzggzjpmnwgc43tirsxgy3snfyhi2lpnzdg64spmjvgky3uom)

## Instance Methods

---

### classDescriptionForObjects

`- (EOClassDescription *)classDescriptionForObjects`

Implemented by subclasses to return an EOClassDescription
that provides information about the objects provided by the receiver.
EODataSource's implementation returns nil.

---

### createObject

`- (id)createObject`

Creates a new object, inserts it in the receiver's
collection of objects if appropriate, and returns the object. Returns nil if
the receiver can't create the object or can't insert it. You
should invoke [insertObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcu3povzggzjpnfxhgzlsorhwe2tfmn2du) after
this method to actually add the new object to the receiver.

As
a convenience, EODataSource's implementation sends the receiver's
EOClassDescription a [createInstanceWithEditingContext:globalID:zone:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5rxezlborsus3ttorqw4y3fk5uxi2cfmruxi2lom5bw63tumv4hiothnrxweylmjfcdu6tpnzstu) message
to create the object. If this succeeds and the receiver has an EOEditingContext,
it sends the EOEditingContext an [insertObject:](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnzzwk4tuj5rguzldoq5a) message to register
the new object with the EOEditingContext (note that this does _not_ insert
the object into the EODataSource). Subclasses that don't use EOClassDescriptions
or EOEditingContexts should override this method _without_ invoking __super__'s
implementation.

__See Also:__  [- classDescriptionForObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcu3povzggzjpmnwgc43tirsxgy3snfyhi2lpnzdg64spmjvgky3uom), [- editingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcu3povzggzjpmvsgs5djnztug33oorsxq5a)

---

### dataSourceQualifiedByKey:

`- (EODataSource *)dataSourceQualifiedByKey:(NSString
*)relationshipKey`

Implemented by subclasses to return a detail
EODataSource that provides the destination objects of the relationship
named by _relationshipKey_. The detail
EODataSource can be qualified using [qualifyWithRelationshipKey:ofObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcu3povzggzjpof2wc3djmz4vo2lunbjgk3dboruw63ttnbuxas3fpe5g6zspmjvgky3uhi) to
set a specific master object (or to change the relationship key).
EODataSource's implementation merely raises an NSInvalidArgumentException;
subclasses shouldn't invoke __super__'s
implementation.

---

### deleteObject:

`- (void)deleteObject:(id)anObject`

Implemented by subclasses to delete _anObject_.
EODataSource's implementation merely raises an NSInvalidArgumentException;
subclasses shouldn't invoke __super__'s
implementation.

---

### editingContext

`- (EOEditingContext *)editingContext`

Implemented by subclasses to return the receiver's
EOEditingContext. EODataSource's implementation returns nil.

---

### fetchObjects

`- (NSArray *)fetchObjects`

Implemented by subclasses to fetch and return
the objects provided by the receiver. EODataSource's implementation
returns nil.

---

### insertObject:

`- (void)insertObject:(id)object`

Implemented by subclasses to insert _object_.
EODataSource's implementation merely raises an NSInvalidArgumentException;
subclasses shouldn't invoke __super__'s
implementation.

---

### qualifyWithRelationshipKey:ofObject:

`- (void)qualifyWithRelationshipKey:(NSString
*)key
ofObject:(id)sourceObject`

Implemented by subclasses to qualify the receiver,
a detail EODataSource, to display destination objects for the relationship
named _key_ belonging to _sourceObject_. _key_ should
be the same as the key specified in the [dataSourceQualifiedByKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcu3povzggzjpmrqxiyktn52xey3fkf2wc3djmzuwkzccpffwk6j2) message
that created the receiver. If _sourceObject_ is nil,
the receiver qualifies itself to provide no objects. EODataSource's
implementation merely raises an NSInvalidArgumentException; subclasses
shouldn't invoke __super__'s implementation.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
