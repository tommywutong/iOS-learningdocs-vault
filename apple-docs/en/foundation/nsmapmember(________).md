---
title: 'NSMapMember(_:_:_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmapmember(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmapmember(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmapmember%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:e755113caa377c16'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMapMember(_:_:_:_:)

<sub>Function</sub>

Indicates whether a given table contains a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSMapMember(_ table: NSMapTable<AnyObject, AnyObject>, _ key: UnsafeRawPointer, _ originalKey: UnsafeMutablePointer<UnsafeMutableRawPointer?>?, _ value: UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> Bool
```

## Return Value

[true](../swift/true.md) if `table` contains a key equal to `key`, otherwise [false](../swift/false.md).

## Discussion

If `table` contains a key equal to `key`, `originalKey` is set to `key`, and `value` is set to the value that `table` maps to `key`.

## See Also

### Related Documentation

- [NSNextMapEnumeratorPair](<nsnextmapenumeratorpair(______).md>) — Returns a Boolean value that indicates whether the next map-table pair in the enumeration are set.
- [NSAllMapTableValues](<nsallmaptablevalues(__).md>) — Returns all of the values in the specified table.
- [NSMapGet](<nsmapget(____).md>) — Returns a map table value for the specified key.
- [NSEnumerateMapTable](<nsenumeratemaptable(__).md>) — Creates an enumerator for the specified map table.
- [NSAllMapTableKeys](<nsallmaptablekeys(__).md>) — Returns all of the keys in the specified map table.

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
- [NSMapRemove](<nsmapremove(____).md>) — Removes a key and corresponding value from the specified table.
