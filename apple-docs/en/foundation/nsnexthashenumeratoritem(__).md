---
title: 'NSNextHashEnumeratorItem(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsnexthashenumeratoritem(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsnexthashenumeratoritem(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnexthashenumeratoritem%28_%3A%29.json'
content_hash: 'sha256:faad02a017dabefc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSNextHashEnumeratorItem(_:)

<sub>Function</sub>

Returns the next hash-table element in the enumeration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSNextHashEnumeratorItem(_ enumerator: UnsafeMutablePointer<NSHashEnumerator>) -> UnsafeMutableRawPointer?
```

## Return Value

The next element in the table that `enumerator` is associated with, or `NULL` if `enumerator` has already iterated over all the elements.

## See Also

### Related Documentation

- [NSEnumerateHashTable](<nsenumeratehashtable(__).md>) — Creates an enumerator for the specified hash table.

### Functions

- [NSAllHashTableObjects](<nsallhashtableobjects(__).md>) — Returns all of the elements in the specified hash table.
- [NSCompareHashTables](<nscomparehashtables(____).md>) — Returns a Boolean value that indicates whether the elements of two hash tables are equal.
- [NSCopyHashTableWithZone](<nscopyhashtablewithzone(____).md>) — Performs a shallow copy of the specified hash table.
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
- [NSResetHashTable](<nsresethashtable(__).md>) — Deletes the elements of the specified hash table.
