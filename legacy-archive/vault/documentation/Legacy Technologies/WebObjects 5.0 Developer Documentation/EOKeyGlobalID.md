---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOKeyGlobalID.html
archived_at: '2026-07-15T08:13:47.006822Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOKeyGlobalID

> **__Inherits from:__**
> : [EOGlobalID](EOGlobalID.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuo3dpmjqwyske)

> **__Implements:__**
> : NSCoding: Cloneable

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

EOKeyGlobalID is a concrete subclass of EOGlobalID whose instances represent persistent IDs based on EOModel information: an entity and the primary key values for the object being identified. When creating an EOKeyGlobalID, the key values must be supplied following alphabetical order for their attribute names. EOKeyGlobalID defines the [globalIDWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpfdwy33cmfwesrbpm5wg6ytbnreuiv3joruek3tunf2hsttbnvsq) for creating instances, but it's much more convenient to create instances from fetched rows using EOEntity's __globalIDForRow:__ method. (EOEntity and EOModel are defined in EOAccess.) Note that you don't use a constructor to create EOKeyGlobalIDs.

## Interfaces Implemented

---

> : NSCoding: [classForCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsr3mn5rgc3cjiqxwg3dbonzum33sinxwizls): [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpfdwy33cmfwesrbpmrswg33emvhwe2tfmn2a): [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsr3mn5rgc3cjiqxwk3tdn5sgkv3jorueg33emvza):

## Method Types

---

> **Creating instances**
> : [globalIDWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpfdwy33cmfwesrbpm5wg6ytbnreuiv3joruek3tunf2hsttbnvsq)
>
> **Getting the entity name**
> : [entityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsr3mn5rgc3cjiqxwk3tunf2hsttbnvsq)
>
> **Getting the key values**
> : [keyValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsr3mn5rgc3cjiqxwwzlzkzqwy5lfom): [keyCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsr3mn5rgc3cjiqxwwzlzinxxk3tu): [keyValuesArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsr3mn5rgc3cjiqxwwzlzkzqwy5lfonaxe4tbpe)
>
> **Comparison**
> : [equals](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsr3mn5rgc3cjiqxwk4lvmfwhg)

## Constructors

---

### EOKeyGlobalID

`protected EOKeyGlobalID (String entityName, int hashCode)`

Description forthcoming.

---

## Static Methods

---

### decodeObject

`public static Object decodeObject(NSCoder coder)`

Conformance to NSCoding.

---

### globalIDWithEntityName

`public static EOKeyGlobalID globalIDWithEntityName( String entityName, Object[] keyValues)`

Returns an EOKeyGlobalID based on _entityName_ and _keyValues_.

EOKeyGlobalIDs are more conveniently created using EOEntity's __globalIDForRow:__ method (EOAccess).

---

## Instance Methods

---

### classForCoder

`public Class classForCoder()`

Conformance to NSCoding.

---

### encodeWithCoder

`public void encodeWithCoder(NSCoder coder)`

Conformance to NSCoding.

---

### entityName

`public String entityName()`

Returns the name of the entity governing the object identified by the receiver. This is used by EODatabaseContexts (EOAccess) to identify an EOEntity (EOAccess) in methods such as __faultForGlobalID__.

---

### equals

`public boolean equals(Object anObject)`

Returns __true__ if the receiver and _anObject_ share the same entity name and key values, __false__ if they don't.

__See Also:__ [entityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsr3mn5rgc3cjiqxwk3tunf2hsttbnvsq), [keyValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsr3mn5rgc3cjiqxwwzlzkzqwy5lfom)

---

### hashCode

`public int hashCode()`

Returns an integer that can be used as a table address in a hash table structure. If two objects are equal (as determined by [equals](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsr3mn5rgc3cjiqxwk4lvmfwhg)), they must have the same hash value.

---

### keyCount

`public int keyCount()`

Returns the number of key values in the receiver.

---

### keyValues

`public Object[] keyValues()`

Returns the receiver's key values.

---

### keyValuesArray

`public NSArray keyValuesArray()`

Returns the receiver's key values as an NSArray.

---

### __toString__

`public String toString()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
