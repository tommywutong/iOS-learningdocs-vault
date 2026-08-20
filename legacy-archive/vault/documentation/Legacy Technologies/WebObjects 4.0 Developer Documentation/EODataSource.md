---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EODataSource.html
archived_at: '2026-07-18T01:28:25.382442Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOCustomObject.md)
[!](EODataSource-2.md)

---

# EODataSource

__Inherits From:__
Object (Java Client)
NSObject (Yellow Box)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (WebObjects and Yellow Box)

## Class Description

EODataSource is an abstract class that defines a basic API for providing enterprise objects. It exists primarily as a simple means for a display group (EODisplayGroup from EOInterface or WODisplayGroup from WebObjects) or other higher-level class to access a store of objects. EODataSource defines functional implementations of very few methods; concrete subclasses, such as EODatabaseDataSource (defined in EOAccess) and EODetailDataSource, define working data sources by implementing the others. EODatabaseDataSource, for example, provides objects fetched through an EOEditingContext, while [EODetailDataSource](EODetailDataSource.md) provides objects from a relationship property of a master object. For information on creating your own EODataSource subclass, see the section "[Creating a Subclass](EODataSource-2.md)."

An EODataSource provides its objects with its __fetchObjects__ method. __insertObject__ and __deleteObject__ add and remove individual objects, and __createObject__ instantiates a new object. Other methods provide information about the objects, as described below.

## Method Types

**Accessing the objects**

**- fetchObjects**

**Inserting and deleting objects**

**- createObject

**- insertObject

**- deleteObject******

**Creating detail data sources**

**- dataSourceQualifiedByKey

**- qualifyWithRelationshipKeyAndObject****

**Accessing the editing context**

**- editingContext**

**Accessing the class description**

**- classDescriptionForObjects**

## Instance Methods

---

#### classDescriptionForObjects

public EOClassDescription __classDescriptionForObjects__ ()

Implemented by subclasses to return an EOClassDescription that provides information about the objects provided by the receiver. EODataSource's implementation returns __null__ .

---

#### createObject

public java.lang.Object __createObject__ ()

Creates a new object, inserts it in the receiver's collection of objects if appropriate, and returns the object. Returns __null__ if the receiver can't create the object or can't insert it. You should invoke __insertObject__ after this method to actually add the new object to the receiver.

As a convenience, EODataSource's implementation sends the receiver's EOClassDescription a [__createInstanceWithEditingContext__](EOClassDescription.md)message to create the object. If this succeeds and the receiver has an EOEditingContext, it sends the EOEditingContext an [__insertObject__](EOEditingContext.md)message to register the new object with the EOEditingContext (note that this does _not_ insert the object into the EODataSource). Subclasses that don't use EOClassDescriptions or EOEditingContexts should override this method _without_ invoking __super__ 's implementation.

__See also:__ - __classDescriptionForObjects__ , - __editingContext__

---

#### dataSourceQualifiedByKey

public abstract EODataSource __dataSourceQualifiedByKey__ (java.lang.String _relationshipKey_)

Implemented by subclasses to return a detail EODataSource that provides the destination objects of the relationship named by _relationshipKey_. The detail EODataSource can be qualified using __qualifyWithRelationshipKeyAndObject__ to set a specific master object (or to change the relationship key). EODataSource's implementation merely throws an exception; subclasses shouldn't invoke __super__ 's implementation.

---

#### deleteObject

public abstract void __deleteObject__ (java.lang.Object _anObject_)

Implemented by subclasses to delete _anObject_. EODataSource's implementation merely throws an exception; subclasses shouldn't invoke __super__ 's implementation.

---

#### editingContext

public EOEditingContext __editingContext__ ()

Implemented by subclasses to return the receiver's EOEditingContext. EODataSource's implementation returns __null__ .

---

#### fetchObjects

public NSArray __fetchObjects__ ()

Implemented by subclasses to fetch and return the objects provided by the receiver. EODataSource's implementation returns __null__ .

---

#### insertObject

public abstract void __insertObject__ (java.lang.Object _object_)

Implemented by subclasses to insert _object_. EODataSource's implementation merely throws an exception; subclasses shouldn't invoke __super__ 's implementation.

---

#### qualifyWithRelationshipKeyAndObject

public abstract void __qualifyWithRelationshipKey__ (
java.lang.String _key_,
java.lang.Object _sourceObject_)

Implemented by subclasses to qualify the receiver, a detail EODataSource, to display destination objects for the relationship named _key_ belonging to _sourceObject_. _key_ should be the same as the key specified in the message that created the receiver. If _sourceObject_ is __null__ , the receiver qualifies itself to provide no objects. EODataSource's implementation merely throws an exception; subclasses shouldn't invoke __super__ 's implementation.

---

[!](EOCustomObject.md)
[!](EODataSource-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
