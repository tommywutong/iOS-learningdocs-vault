---
title: Legacy Map Table Implementation
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/legacy-map-table-implementation
source_url: 'https://developer.apple.com/documentation/foundation/legacy-map-table-implementation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/legacy-map-table-implementation.json'
content_hash: 'sha256:cb7daee4a7520aeb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Collections](collections.md) · [NSMapTable](nsmaptable.md)

# Legacy Map Table Implementation

<sub>API Collection</sub>

## Topics

### Functions

- [NSAllMapTableKeys](<nsallmaptablekeys(__).md>) — Returns all of the keys in the specified map table.
- [NSAllMapTableValues](<nsallmaptablevalues(__).md>) — Returns all of the values in the specified table.
- [NSCompareMapTables](<nscomparemaptables(____).md>) — Compares the elements of two map tables for equality.
- [NSCopyMapTableWithZone](<nscopymaptablewithzone(____).md>) — Performs a shallow copy of the specified map table.
- [NSCountMapTable](<nscountmaptable(__).md>) — Returns the number of elements in a map table.
- [NSCreateMapTable](<nscreatemaptable(______).md>) — Creates a new map table in the default zone.
- [NSCreateMapTableWithZone](<nscreatemaptablewithzone(________).md>) — Creates a new map table in the specified zone.
- [NSEndMapTableEnumeration](<nsendmaptableenumeration(__).md>) — Used when finished with an enumerator.
- [NSEnumerateMapTable](<nsenumeratemaptable(__).md>) — Creates an enumerator for the specified map table.
- [NSFreeMapTable](<nsfreemaptable(__).md>) — Deletes the specified map table.
- [NSMapGet](<nsmapget(____).md>) — Returns a map table value for the specified key.
- [NSMapInsert](<nsmapinsert(______).md>) — Inserts a key-value pair into the specified table.
- [NSMapInsertIfAbsent](<nsmapinsertifabsent(______).md>) — Inserts a key-value pair into the specified table.
- [NSMapInsertKnownAbsent](<nsmapinsertknownabsent(______).md>) — Inserts a key-value pair into the specified table if the pair had not been previously added.
- [NSMapMember](<nsmapmember(________).md>) — Indicates whether a given table contains a given key.
- [NSMapRemove](<nsmapremove(____).md>) — Removes a key and corresponding value from the specified table.
- [NSNextMapEnumeratorPair](<nsnextmapenumeratorpair(______).md>) — Returns a Boolean value that indicates whether the next map-table pair in the enumeration are set.
- [NSResetMapTable](<nsresetmaptable(__).md>) — Deletes the elements of the specified map table.
- [NSStringFromMapTable](<nsstringfrommaptable(__).md>) — Returns a string describing the map table’s contents.

### Data Types

- [NSMapEnumerator](nsmapenumerator.md) — Allows successive elements of a map table to be returned each time this structure is passed to [NSNextMapEnumeratorPair](<nsnextmapenumeratorpair(______).md>).
- [NSMapTable](legacy-nsmaptable.md) — The opaque data type used by the functions described in Managing Map Tables.
- [NSMapTableKeyCallBacks](nsmaptablekeycallbacks.md) — The function pointers used to configure behavior of `NSMapTable` with respect to key elements within a map table.
- [NSMapTableOptions](nsmaptableoptions.md) — Constants used as components in a bitfield to specify the behavior of elements (keys and values) in an `NSMapTable` object.
- [NSMapTableValueCallBacks](nsmaptablevaluecallbacks.md) — The function pointers used to configure behavior of `NSMapTable` with respect to value elements within a map table.

### Constants

- [NSIntegerMapKeyCallBacks](nsintegermapkeycallbacks.md) — For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`).
- [NSIntMapKeyCallBacks](nsintmapkeycallbacks.md) — For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`). _(deprecated)_
- [NSNonOwnedPointerMapKeyCallBacks](nsnonownedpointermapkeycallbacks.md) — For keys that are pointers not freed.
- [NSNonOwnedPointerOrNullMapKeyCallBacks](nsnonownedpointerornullmapkeycallbacks.md) — For keys that are pointers not freed, or `NULL`.
- [NSNonRetainedObjectMapKeyCallBacks](nsnonretainedobjectmapkeycallbacks.md) — For sets of objects, but without retaining/releasing.
- [NSObjectMapKeyCallBacks](nsobjectmapkeycallbacks.md) — For keys that are objects.
- [NSOwnedPointerMapKeyCallBacks](nsownedpointermapkeycallbacks.md) — For keys that are pointers, with transfer of ownership upon insertion.

### Constants

- [NSIntegerMapValueCallBacks](nsintegermapvaluecallbacks.md) — For values that are pointer-sized quantities, (for example, `int`, `long`, or `unichar`).
- [NSIntMapValueCallBacks](nsintmapvaluecallbacks.md) — For values that are pointer-sized quantities, (for example, `int`, `long`, or `unichar`). _(deprecated)_
- [NSNonOwnedPointerMapValueCallBacks](nsnonownedpointermapvaluecallbacks.md) — For values that are not owned pointers.
- [NSOwnedPointerMapValueCallBacks](nsownedpointermapvaluecallbacks.md) — For values that are owned pointers.
- [NSNonRetainedObjectMapValueCallBacks](nsnonretainedobjectmapvaluecallbacks.md) — For sets of objects, but without retaining/releasing.
- [NSObjectMapValueCallBacks](nsobjectmapvaluecallbacks.md) — For values that are objects.

## See Also

### Deprecated
