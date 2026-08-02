---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOKeyGlobalID.html
archived_at: '2026-07-18T01:28:26.440820Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOKeyComparisonQualifier.md)
[!](EOKeyValueQualifier.md)

---

# EOKeyGlobalID

__Inherits From:__
EOGlobalID : Object (Java Client)
EOGlobalID : NSObject (Yellow Box)

__Implements:__
com.apple.client.foundation.NSCoding (Java Client only)
java.lang.Cloneable (Java Client only)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (WebObjects and Yellow Box)

## Class Description

EOKeyGlobalID is a concrete subclass of EOGlobalID whose instances represent persistent IDs based on EOModel information: an entity and the primary key values for the object being identified. When creating an EOKeyGlobalID, the key values must be supplied following alphabetical order for their attribute names. EOKeyGlobalID defines the __globalIDWithEntityName__ for creating instances, but it's much more convenient to create instances from fetched rows using EOEntity's __globalIDForRow__ method. (EOEntity and EOModel are defined in EOAccess.) Note that you don't use a constructor to create EOKeyGlobalIDs.

## Interfaces Implemented

**NSCoding**

**classForCoder (Java Client only)

**encodeWithCoder (Java Client only)****

## Method Types

**Creating instances**

**+ globalIDWithEntityName**

**Getting the entity name**

**- entityName**

**Getting the key values**

**- keyValues

**- keyCount

**- keyValuesArray******

**Comparison**

**- equals**

## Static Methods

---

#### globalIDWithEntityName

public static EOKeyGlobalID __globalIDWithEntityName__ (
java.lang.String _entityName_,
NSArray _keyValues_)

Returns an EOKeyGlobalID based on _entityName_ and _keyValues_.

EOKeyGlobalIDs are more conveniently created using EOEntity's __globalIDForRow__ method (EOAccess).

## Instance Methods

---

#### entityName

public java.lang.String __entityName__ ()

Returns the name of the entity governing the object identified by the receiver. This is used by EODatabaseContexts (EOAccess) to identify an EOEntity (EOAccess) in methods such as __faultForGlobalID__ .

---

#### equals

public boolean __equals__ (java.lang.Object _anObject_)

Returns __true__ if the receiver and _anObject_ share the same entity name and key values, __false__ if they don't.

__See also:__ - __entityName__ , - __keyValues__

---

#### hashcode

public int __hashCode__ ()

Returns an integer that can be used as a table address in a hash table structure. If two objects are equal (as determined by __equals__ ), they must have the same hash value.

---

#### keyCount

public int __keyCount__ ()

Returns the number of key values in the receiver.

---

#### keyValues

public java.lang.Object[] __keyValues__ ()

Returns the receiver's key values.

---

#### keyValuesArray

public NSArray __keyValuesArray__ ()

Returns the receiver's key values as an NSArray.

---

[!](EOKeyComparisonQualifier.md)
[!](EOKeyValueQualifier.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
