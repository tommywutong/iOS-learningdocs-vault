---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EODetailDataSource.html
archived_at: '2026-07-18T01:28:25.670862Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EODelayedObserverQueue-2.md)
[!](EOEditingContext.md)

---

# EODetailDataSource

__Inherits From:__
[EODataSource](EODataSource.md) : Object (Java Client)
[EODataSource](EODataSource.md) : NSObject (Yellow Box)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (WebObjects and Yellow Box)

## Class Description

EODetailDataSource defines a data source for use in master-detail configurations, where operations in the detail data source are applied directly to properties of a master object. EODetailDataSource implements the standard __fetchObjects__ , __insertObject__ , and __deleteObject__ methods to operate on a relationship property of its master object, so it works for any concrete subclass of EODataSource, including another EODetailDataSource (for a chain of three master and detail data sources).

To set up an EODetailDataSource programmatically, you typically create it by sending a [__dataSourceQualifiedByKey__](EODataSource.md)message to the master data source, then establish the master object with a __qualifyWithRelationshipKey__ message. The latter method records the name of a relationship for a particular object to resolve in __fetchObjects__ and to modify in __insertObject__ , and __deleteObject__ . These three methods then manipulate the relationship property of the master object to perform the operations requested. See the individual method descriptions for more information.

## Method Types

**Constructors**

**EODetailDataSource**

**Qualifying instances**

**- qualifyWithRelationshipKey**

**Examining instances**

**- masterDataSource

**- detailKey

**- masterObject******

**Accessing the master class description**

**- masterClassDescription

**- setMasterClassDescription (Yellow Box only)****

**Accessing the objects**

**- fetchObjects**

**Inserting and deleting objects**

**- insertObject

**- deleteObject****

**Accessing the master editing context**

**- editingContext**

## Constructors

---

#### EODetailDataSource

public __EODetailDataSource__ (
EOClassDescription _masterClassDescription_,
java.lang.String _relationshipKey_)

Creates and returns a new EODetailDataSource object. The new data source's __masterObject__ is associated with _masterClassDescription_, and _relationshipKey_ is assigned to the new data source's __detailKey__ . The constructor invokes __qualifyWithRelationshipKey__ specifying _relationshipKey_ as the relationship key and `null` as the object.

public __EODetailDataSource__ (
EODataSource _masterDataSource_,
java.lang.String _relationshipKey_)

Creates and returns a new EODetailDataSource object. The new data source provides destination objects for the relationship named by _relationshipKey_ from a __masterObject__ in _masterDataSource_.

__See also:__ - __masterClassDescription__ , - __masterDataSource__

## Instance Methods

---

#### deleteObject

public void __deleteObject__ (java.lang.Object _anObject_)

Sends a [__removeObjectFromPropertyWithKey__](EORelationshipManipulation.md)message (defined in the [EORelationshipManipulation](EORelationshipManipulation.md) interface) to the master object with _anObject_ and the receiver's detail key as the arguments. Throws an exception if there's no master object or no detail key set.

---

#### detailKey

public java.lang.String __detailKey__ ()

Returns the name of the relationship for which the receiver provides objects, as provided to the constructor when the receiver was created or as set in __qualifyWithRelationshipKey__ . If none has been set yet, returns __null__ .

__See also:__ "Constructors"

---

#### editingContext

public EOEditingContext __editingContext__ ()

Returns the EOEditingContext of the master object, or `null` if there isn't one.

---

#### fetchObjects

public NSArray __fetchObjects__ ()

Sends [__valueForKey__](EOKeyValueCoding.md)(defined in the [EOKeyValueCoding](EOKeyValueCoding.md) interface) to the master object with the receiver's detail key as the argument, constructs an array for the returned object or objects, and returns it. Returns an empty array if there's no master object, or returns an array containing the master object itself if no detail key is set.

---

#### insertObject

public void __insertObject__ (java.lang.Object _anObject_)

Sends an [__addObjectToBothSidesOfRelationshipWithKey__](EORelationshipManipulation.md)message (defined in the [EORelationshipManipulation](EORelationshipManipulation.md)] interface) to the master object with _anObject_ and the receiver's detail key as the arguments. Throws an exception if there's no master object or no detail key set.

---

#### masterClassDescription

public EOClassDescription __masterClassDescription__ ()

Returns the EOClassDescription of the receiver's master object.

__See also:__ - __setMasterClassDescription__ , "Constructors"

---

#### masterDataSource

public EODataSource __masterDataSource__ ()

Returns the receiver's master data source.

__See also:__ - __detailKey__ , "Constructors"

---

#### masterObject

public java.lang.Object __masterObject__ ()

Returns the object in the master data source for which the receiver provides objects. You can change this with a __qualifyWithRelationshipKey__ message.

__See also:__ - __detailKey__

---

#### qualifyWithRelationshipKey

public void __qualifyWithRelationshipKey__ (
java.lang.String _relationshipKey_,
java.lang.Object _masterObject_)

Configures the receiver to provide objects based on the relationship of _masterObject_ named by _relationshipKey_. _relationshipKey_ can be different from the one provided to the constructor, which changes the relationship the receiver operates on. If _masterObject_ is __null__ , this method causes the receiver to return an empty array when sent a __fetchObjects__ message.

__See also:__ - __detailKey__

---

#### setMasterClassDescription

public void __setMasterClassDescription__ (EOClassDescription _anEOClassDescription_)

Assigns _classDescription_ as the EOClassDescription for the receiver's master object.

__See also:__ - __masterClassDescription__

---

[!](EODelayedObserverQueue-2.md)
[!](EOEditingContext.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
