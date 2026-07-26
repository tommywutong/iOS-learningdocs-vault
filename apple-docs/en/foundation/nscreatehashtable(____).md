---
title: 'NSCreateHashTable(_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscreatehashtable(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscreatehashtable(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscreatehashtable%28_%3A_%3A%29.json'
content_hash: 'sha256:ecb491e22294cc24'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCreateHashTable(_:_:)

<sub>Function</sub>

Creates and returns a new hash table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSCreateHashTable(_ callBacks: NSHashTableCallBacks, _ capacity: Int) -> NSHashTable<AnyObject>
```

## Return Value

A pointer to an NSHashTable created in the default zone.

## Discussion

The table’s size is dependent on (but generally not equal to) `capacity`. If `capacity` is 0, a small hash table is created. The [NSHashTableCallBacks](nshashtablecallbacks.md) structure `callBacks` has five pointers to functions, with the following defaults: pointer hashing, if `hash` is `NULL`; pointer equality, if `isEqual` is `NULL`; no callback upon adding an element, if `retain` is `NULL`; no callback upon removing an element, if `release` is `NULL`; and a function returning a pointer’s hexadecimal value as a string, if `describe` is `NULL`. The hashing function must be defined such that if two data elements are equal, as defined by the comparison function, the values produced by hashing on these elements must also be equal. Also, data elements must remain invariant if the value of the hashing function depends on them; for example, if the hashing function operates directly on the characters of a string, that string can’t change.

## See Also

### Related Documentation

- [NSCreateHashTableWithZone](<nscreatehashtablewithzone(______).md>) — Creates a new hash table in a given zone.
- [NSCopyHashTableWithZone](<nscopyhashtablewithzone(____).md>) — Performs a shallow copy of the specified hash table.

### Functions

- [NSAllHashTableObjects](<nsallhashtableobjects(__).md>) — Returns all of the elements in the specified hash table.
- [NSCompareHashTables](<nscomparehashtables(____).md>) — Returns a Boolean value that indicates whether the elements of two hash tables are equal.
- [NSCopyHashTableWithZone](<nscopyhashtablewithzone(____).md>) — Performs a shallow copy of the specified hash table.
- [NSCountHashTable](<nscounthashtable(__).md>) — Returns the number of elements in a hash table.
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
