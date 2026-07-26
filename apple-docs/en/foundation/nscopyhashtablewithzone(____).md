---
title: 'NSCopyHashTableWithZone(_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscopyhashtablewithzone(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscopyhashtablewithzone(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscopyhashtablewithzone%28_%3A_%3A%29.json'
content_hash: 'sha256:35334e41b209d6f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCopyHashTableWithZone(_:_:)

<sub>Function</sub>

Performs a shallow copy of the specified hash table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSCopyHashTableWithZone(_ table: NSHashTable<AnyObject>, _ zone: NSZone?) -> NSHashTable<AnyObject>
```

## Return Value

A pointer to a new copy of `table`, created in `zone` and containing pointers to the data elements of `table`.

## Discussion

If `zone` is `NULL`, the new table is created in the default zone.

The new table adopts the callback functions of `table` and calls the `hash` and `retain` callback functions as appropriate when inserting elements into the new table.

## See Also

### Related Documentation

- [NSCreateHashTableWithZone](<nscreatehashtablewithzone(______).md>) — Creates a new hash table in a given zone.
- [NSCreateHashTable](<nscreatehashtable(____).md>) — Creates and returns a new hash table.
- [NSHashTableCallBacks](nshashtablecallbacks.md) — Defines a structure that contains the function pointers used to configure behavior of `NSHashTable` with respect to elements within a hash table.

### Functions

- [NSAllHashTableObjects](<nsallhashtableobjects(__).md>) — Returns all of the elements in the specified hash table.
- [NSCompareHashTables](<nscomparehashtables(____).md>) — Returns a Boolean value that indicates whether the elements of two hash tables are equal.
- [NSCountHashTable](<nscounthashtable(__).md>) — Returns the number of elements in a hash table.
- [NSCreateHashTable](<nscreatehashtable(____).md>) — Creates and returns a new hash table.
- [NSCreateHashTableWithZone](<nscreatehashtablewithzone(______).md>) — Creates a new hash table in a given zone.
- [NSEndHashTableEnumeration](<nsendhashtableenumeration(__).md>) — Used when finished with an enumerator.
- [NSEnumerateHashTable](<nsenumeratehashtable(__).md>) — Creates an enumerator for the specified hash table.
- [NSFreeHashTable](<nsfreehashtable(__).md>) — Deletes the specified hash table.
- [NSHashGet](<nshashget(____).md>) — Returns an element of the hash table.
- [NSHashInsert](<nshashinsert(____).md>) — Adds an element to the specified hash table.
- [NSHashInsertIfAbsent](<nshashinsertifabsent(____).md>) — Adds an element to the specified hash table only if the table does not already contain the element.
- [NSHashInsertKnownAbsent](<nshashinsertknownabsent(____).md>) — Adds an element to the specified hash table.
- [NSHashRemove](<nshashremove(____).md>) — Removes an element from the specified hash table.
- [NSNextHashEnumeratorItem](<nsnexthashenumeratoritem(__).md>) — Returns the next hash-table element in the enumeration.
- [NSResetHashTable](<nsresethashtable(__).md>) — Deletes the elements of the specified hash table.
