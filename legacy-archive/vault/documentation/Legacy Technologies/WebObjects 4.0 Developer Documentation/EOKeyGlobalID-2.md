---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOKeyGlobalID.html
archived_at: '2026-07-18T01:28:36.422574Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOKeyComparisonQualifier-2.md)
[!](EOKeyValueQualifier-2.md)

---

# EOKeyGlobalID

__Inherits From:__
NSObject

__Conforms To:__ NSCoding
NSCopying (EOGlobalID)
NSObject (NSObject)

__Declared in:__ EOAccess/EOKeyGlobalID.h

EOKeyGlobalID is a concrete subclass of EOGlobalID whose instances represent persistent IDs based on EOModel information: an entity and the primary key values for the object being identified. When creating an EOKeyGlobalID, the key values must be supplied following alphabetical order for their attribute names. EOKeyGlobalID defines the __globalIDWithEntityName:keys:keyCount:zone:__ for creating instances, but it's much more convenient to create instances from fetched rows using EOEntity's __globalIDForRow:__ method. (EOEntity and EOModel are defined in EOAccess.)

---

## Adopted Protocols

**NSCoding**

**- encodeWithCoder:

**- initWithCoder:****

**Creating instances**

**+ globalIDWithEntityName:keys:keyCount:zone:**

**Getting the entity name**

**- entityName**

**Getting the key values**

**- keyValues

**- keyCount

**- keyValuesArray******

**Comparison**

**- isEqual:**

---

#### globalIDWithEntityName:keys:keyCount:zone:

+ (id)__globalIDWithEntityName:__ (NSString \*)_entityName___keys:__ (id \*)_keyValues___keyCount:__ (unsigned int)_count___zone:__ (NSZone \*)_zone_

Returns an EOKeyGlobalID based on _entityName_ and _keyValues_. For performance reasons, the key values are given as a C array of __id__ ; _count_ indicates how many key values there are. The object returned is allocated from _zone_.

EOKeyGlobalIDs are more conveniently created using EOEntity's __globalIDForRow:__ method (EOAccess).

---

#### entityName

- (NSString \*)__entityName__

Returns the name of the entity governing the object identified by the receiver. This is used by EODatabaseContexts (EOAccess) to identify an EOEntity (EOAccess) in methods such as __faultForGlobalID:editingContext:__ .

`hash`- (unsigned int)__hash__

Returns an integer that can be used as a table address in a hash table structure. If two objects are equal (as determined by __isEqual:__ ), they must have the same hash value. For more information, see the descriptions of this method in the NSObject class and protocol specifications of the Foundation Framework.

---

#### isEqual:

@protocol NSObject

- (BOOL)__isEqual:__ (id)_anObject_

Returns YES if the receiver and _anObject_ share the same entity name and key values, NO if they don't. For more information, see the descriptions of this method in the NSObject class and protocol specifications of the Foundation Framework.

__See also:__ - __entityName__ , - __keyValues__

---

#### keyCount

- (unsigned int)__keyCount__

Returns the number of key values in the receiver.

---

#### keyValues

- (id \*)__keyValues__

Returns the receiver's key values as a C array of __id__ (for performance reasons).

---

#### keyValuesArray

- (NSArray \*)__keyValuesArray__

Returns the receiver's key values as an NSArray.

---

[!](EOKeyComparisonQualifier-2.md)
[!](EOKeyValueQualifier-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
