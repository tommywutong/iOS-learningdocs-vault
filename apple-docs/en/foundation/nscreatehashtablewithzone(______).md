---
title: 'NSCreateHashTableWithZone(_:_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscreatehashtablewithzone(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscreatehashtablewithzone(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscreatehashtablewithzone%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:d513551162d45346'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCreateHashTableWithZone(_:_:_:)

<sub>Function</sub>

Creates a new hash table in a given zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSCreateHashTableWithZone(_ callBacks: NSHashTableCallBacks, _ capacity: Int, _ zone: NSZone?) -> NSHashTable<AnyObject>
```

## Return Value

A pointer to a new hash table created in the specified zone. If `zone` is `NULL`, the hash table is created in the default zone.

## Discussion

The table’s size is dependent on (but generally not equal to) `capacity`. If `capacity` is 0, a small hash table is created. The [NSHashTableCallBacks](nshashtablecallbacks.md) structure `callBacks` has five pointers to functions, with the following defaults: pointer hashing, if `hash` is `NULL`; pointer equality, if `isEqual` is `NULL`; no callback upon adding an element, if `retain` is `NULL`; no callback upon removing an element, if `release` is `NULL`; and a function returning a pointer’s hexadecimal value as a string, if `describe` is `NULL`. The hashing function must be defined such that if two data elements are equal, as defined by the comparison function, the values produced by hashing on these elements must also be equal. Also, data elements must remain invariant if the value of the hashing function depends on them; for example, if the hashing function operates directly on the characters of a string, that string can’t change.

## See Also

### Related Documentation

- [NSCreateHashTable](<nscreatehashtable(____).md>) — Creates and returns a new hash table.

### Functions

- [NSAllHashTableObjects](<nsallhashtableobjects(__).md>) — Returns all of the elements in the specified hash table.
- [NSCompareHashTables](<nscomparehashtables(____).md>) — Returns a Boolean value that indicates whether the elements of two hash tables are equal.
- [NSCopyHashTableWithZone](<nscopyhashtablewithzone(____).md>) — Performs a shallow copy of the specified hash table.
- [NSCountHashTable](<nscounthashtable(__).md>) — Returns the number of elements in a hash table.
- [NSCreateHashTable](<nscreatehashtable(____).md>) — Creates and returns a new hash table.
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
