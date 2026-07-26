---
title: 'NSMapInsertKnownAbsent(_:_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmapinsertknownabsent(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmapinsertknownabsent(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmapinsertknownabsent%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:046a2d1249c5da42'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMapInsertKnownAbsent(_:_:_:)

<sub>Function</sub>

Inserts a key-value pair into the specified table if the pair had not been previously added.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSMapInsertKnownAbsent(_ table: NSMapTable<AnyObject, AnyObject>, _ key: UnsafeRawPointer?, _ value: UnsafeRawPointer?)
```

## Discussion

Inserts `key` (which must not be `notAKeyMarker`) and `value` into `table`. Unlike `NSMapInsert`, this function raises `NSInvalidArgumentException` if `table` already includes a key that matches `key`.

`key` is compared with `notAKeyMarker` using pointer comparison; if `key` is identical to `notAKeyMarker`, raises `NSInvalidArgumentException`.

## See Also

### Related Documentation

- [NSMapInsertIfAbsent](<nsmapinsertifabsent(______).md>) — Inserts a key-value pair into the specified table.
- [NSMapRemove](<nsmapremove(____).md>) — Removes a key and corresponding value from the specified table.
- [NSMapInsert](<nsmapinsert(______).md>) — Inserts a key-value pair into the specified table.

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
- [NSMapMember](<nsmapmember(________).md>) — Indicates whether a given table contains a given key.
- [NSMapRemove](<nsmapremove(____).md>) — Removes a key and corresponding value from the specified table.
