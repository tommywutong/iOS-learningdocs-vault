---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EODataSource.html
archived_at: '2026-07-18T01:28:35.336438Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOCooperatingObjectStore-2.md)
[!](EODataSource-4.md)

---

# EODataSource

__Inherits From:__
NSObject

__Conforms To:__ NSObject (NSObject)

__Declared in:__ EOControl/EODataSource.h

EODataSource is an abstract class that defines a basic API for providing enterprise objects. It exists primarily as a simple means for a display group (EODisplayGroup from EOInterface or WODisplayGroup from WebObjects) or other higher-level class to access a store of objects. EODataSource defines functional implementations of very few methods; concrete subclasses, such as EODatabaseDataSource (defined in EOAccess) and EODetailDataSource, define working data sources by implementing the others. EODatabaseDataSource, for example, provides objects fetched through an EOEditingContext, while [EODetailDataSource](EODetailDataSource-2.md) provides objects from a relationship property of a master object. For information on creating your own EODataSource subclass, see the section "[Creating a Subclass](EODataSource-4.md)."

An EODataSource provides its objects with its __fetchObjects__ method. __insertObject:__ and __deleteObject:__ add and remove individual objects, and __createObject__ instantiates a new object. Other methods provide information about the objects, as described below.

**Accessing the objects**

**- fetchObjects**

**Inserting and deleting objects**

**- createObject

**- insertObject:

**- deleteObject:******

**Creating detail data sources**

**- dataSourceQualifiedByKey:

**- qualifyWithRelationshipKey:ofObject:****

**Accessing the editing context**

**- editingContext**

**Accessing the class description**

**- classDescriptionForObjects**

---

#### classDescriptionForObjects

- (EOClassDescription \*)__classDescriptionForObjects__

Implemented by subclasses to return an EOClassDescription that provides information about the objects provided by the receiver. EODataSource's implementation returns __nil__ .

---

#### createObject

- (id)__createObject__

Creates a new object, inserts it in the receiver's collection of objects if appropriate, and returns the object. Returns __nil__ if the receiver can't create the object or can't insert it. You should invoke __insertObject:__ after this method to actually add the new object to the receiver.

As a convenience, EODataSource's implementation sends the receiver's EOClassDescription a [__createInstanceWithEditingContext:globalID:zone:__](EOClassDescription-3.md)message to create the object. If this succeeds and the receiver has an EOEditingContext, it sends the EOEditingContext an [__insertObject:__](EOEditingContext-3.md)message to register the new object with the EOEditingContext (note that this does _not_ insert the object into the EODataSource). Subclasses that don't use EOClassDescriptions or EOEditingContexts should override this method _without_ invoking __super__ 's implementation.

__See also:__ - __classDescriptionForObjects__ , - __editingContext__

---

#### dataSourceQualifiedByKey:

- (EODataSource \*)__dataSourceQualifiedByKey:__ (NSString \*)_relationshipKey_

Implemented by subclasses to return a detail EODataSource that provides the destination objects of the relationship named by _relationshipKey_. The detail EODataSource can be qualified using __qualifyWithRelationshipKey:ofObject:__ to set a specific master object (or to change the relationship key). EODataSource's implementation merely raises an NSInvalidArgumentException; subclasses shouldn't invoke __super__ 's implementation.

---

#### deleteObject:

- (void)__deleteObject:__ (id)_anObject_

Implemented by subclasses to delete _anObject_. EODataSource's implementation merely raises an NSInvalidArgumentException; subclasses shouldn't invoke __super__ 's implementation.

---

#### editingContext

- (EOEditingContext \*)__editingContext__

Implemented by subclasses to return the receiver's EOEditingContext. EODataSource's implementation returns __nil__ .

---

#### fetchObjects

- (NSArray \*)__fetchObjects__

Implemented by subclasses to fetch and return the objects provided by the receiver. EODataSource's implementation returns __nil__ .

---

#### insertObject:

- (void)__insertObject:__ (id)_object_

Implemented by subclasses to insert _object_. EODataSource's implementation merely raises an NSInvalidArgumentException; subclasses shouldn't invoke __super__ 's implementation.

---

#### qualifyWithRelationshipKey:ofObject:

- (void)__qualifyWithRelationshipKey:__ (NSString \*)_key___ofObject:__ (id)_sourceObject_

Implemented by subclasses to qualify the receiver, a detail EODataSource, to display destination objects for the relationship named _key_ belonging to _sourceObject_. _key_ should be the same as the key specified in the __dataSourceQualifiedByKey:__ message that created the receiver. If _sourceObject_ is __nil__ , the receiver qualifies itself to provide no objects. EODataSource's implementation merely raises an NSInvalidArgumentException; subclasses shouldn't invoke __super__ 's implementation.

---

[!](EOCooperatingObjectStore-2.md)
[!](EODataSource-4.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
