---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOKeyGlobalID.html
archived_at: '2026-07-15T08:11:37.713864Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOKeyGlobalID

> **__Inherits
> from:__**
> : [(com.apple.client.eocontrol) EOGlobalID](EOGlobalID.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuo3dpmjqwyske) : Object
> (com.apple.yellow.eocontrol) EOGlobalID : NSObject

> **__Implements:__**
> : (com.apple.client.eocontrol only) NSCoding
> : (com.apple.client.eocontrol only) Cloneable

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Class Description

---

EOKeyGlobalID is a concrete subclass of EOGlobalID whose instances
represent persistent IDs based on EOModel information: an entity
and the primary key values for the object being identified. When creating
an EOKeyGlobalID, the key values must be supplied following alphabetical
order for their attribute names. EOKeyGlobalID defines the [globalIDWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpfdwy33cmfwesrbpm5wg6ytbnreuiv3joruek3tunf2hsttbnvsq) for creating
instances, but it's much more convenient to create instances from
fetched rows using EOEntity's `globalIDForRow` method. (EOEntity
and EOModel are defined in EOAccess.) Note that you don't use
a constructor to create EOKeyGlobalIDs.

## Interfaces Implemented

---

> NSCoding (com.apple.client.eocontrol only): `classForCoder`
> : `encodeWithCoder`

## Method Types

---

> **Creating instances**
> : [globalIDWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpfdwy33cmfwesrbpm5wg6ytbnreuiv3joruek3tunf2hsttbnvsq)
>
> **Getting the entity name**
> : [entityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsr3mn5rgc3cjiqxwk3tunf2hsttbnvsq)
>
> **Getting the key values**
> : [keyValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsr3mn5rgc3cjiqxwwzlzkzqwy5lfom)
> : [keyCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsr3mn5rgc3cjiqxwwzlzinxxk3tu)
> : [keyValuesArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsr3mn5rgc3cjiqxwwzlzkzqwy5lfonaxe4tbpe)
>
> **Comparison**
> : [equals](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsr3mn5rgc3cjiqxwk4lvmfwhg)

## Static Methods

---

### globalIDWithEntityName

`public static EOKeyGlobalID globalIDWithEntityName(
String entityName,
NSArray keyValues)`

Returns an EOKeyGlobalID based on _entityName_ and _keyValues._

EOKeyGlobalIDs
are more conveniently created using EOEntity's `globalIDForRow` method
(EOAccess).

---

## Instance Methods

---

### entityName

`public String entityName()`

Returns the name of the entity governing the
object identified by the receiver. This is used by EODatabaseContexts
(EOAccess) to identify an EOEntity (EOAccess) in methods such as `faultForGlobalID`.

---

### equals

`public boolean equals(Object anObject)`

Returns `true` if the
receiver and _anObject_ share the same
entity name and key values, `false` if they
don't.

__See Also:__  [entityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsr3mn5rgc3cjiqxwk3tunf2hsttbnvsq), [keyValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsr3mn5rgc3cjiqxwwzlzkzqwy5lfom)

---

### hashCode

`public int hashCode()`

Returns an integer that can be used as a table
address in a hash table structure. If two objects are equal (as
determined by [isEqual:](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsr3mn5rgc3cjiqxwk4lvmfwhg)),
they must have the same hash value.

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

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
