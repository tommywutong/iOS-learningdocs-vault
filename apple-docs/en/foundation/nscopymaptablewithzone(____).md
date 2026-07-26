---
title: 'NSCopyMapTableWithZone(_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscopymaptablewithzone(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscopymaptablewithzone(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscopymaptablewithzone%28_%3A_%3A%29.json'
content_hash: 'sha256:bf8bc9c3655f15bb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCopyMapTableWithZone(_:_:)

<sub>Function</sub>

Performs a shallow copy of the specified map table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSCopyMapTableWithZone(_ table: NSMapTable<AnyObject, AnyObject>, _ zone: NSZone?) -> NSMapTable<AnyObject, AnyObject>
```

## Return Value

A pointer to a new copy of `table`, created in `zone` and containing pointers to the keys and values of `table`.

## Discussion

If `zone` is `NULL`, the new table is created in the default zone.

The new table adopts the callback functions of `table` and calls the `hash` and `retain` callback functions as appropriate when inserting elements into the new table.

## See Also

### Related Documentation

- [NSCreateMapTableWithZone](<nscreatemaptablewithzone(________).md>) — Creates a new map table in the specified zone.
- [NSCreateMapTable](<nscreatemaptable(______).md>) — Creates a new map table in the default zone.
- [NSMapTableValueCallBacks](nsmaptablevaluecallbacks.md) — The function pointers used to configure behavior of `NSMapTable` with respect to value elements within a map table.
- [NSMapTableKeyCallBacks](nsmaptablekeycallbacks.md) — The function pointers used to configure behavior of `NSMapTable` with respect to key elements within a map table.

### Functions

- [NSAllMapTableKeys](<nsallmaptablekeys(__).md>) — Returns all of the keys in the specified map table.
- [NSAllMapTableValues](<nsallmaptablevalues(__).md>) — Returns all of the values in the specified table.
- [NSCompareMapTables](<nscomparemaptables(____).md>) — Compares the elements of two map tables for equality.
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
