---
title: Legacy Hash Table Implementation
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/legacy-hash-table-implementation
source_url: 'https://developer.apple.com/documentation/foundation/legacy-hash-table-implementation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/legacy-hash-table-implementation.json'
content_hash: 'sha256:40dcf14cd80c0039'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Collections](collections.md) · [NSHashTable](nshashtable.md)

# Legacy Hash Table Implementation

<sub>API Collection</sub>

## Topics

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
- [NSNextHashEnumeratorItem](<nsnexthashenumeratoritem(__).md>) — Returns the next hash-table element in the enumeration.
- [NSResetHashTable](<nsresethashtable(__).md>) — Deletes the elements of the specified hash table.
- [NSStringFromHashTable](<nsstringfromhashtable(__).md>) — Returns a string describing the hash table’s contents.

### Data Types

- [NSHashEnumerator](nshashenumerator.md) — Allows successive elements of a hash table to be returned each time this structure is passed to [NSNextHashEnumeratorItem](<nsnexthashenumeratoritem(__).md>).
- [NSHashTableCallBacks](nshashtablecallbacks.md) — Defines a structure that contains the function pointers used to configure behavior of `NSHashTable` with respect to elements within a hash table.
- [NSHashTableOptions](nshashtableoptions.md) — Components in a bit-field to specify the behavior of elements in an [NSHashTable](nshashtable.md) object.

### Constants

- [NSIntegerHashCallBacks](nsintegerhashcallbacks.md) — For sets of `NSInteger`-sized quantities or smaller (for example, `int`, `long`, or `unichar`).
- [NSNonOwnedPointerHashCallBacks](nsnonownedpointerhashcallbacks.md) — For sets of pointers, hashed by address.
- [NSNonRetainedObjectHashCallBacks](nsnonretainedobjecthashcallbacks.md) — For sets of objects, but without retaining/releasing.
- [NSObjectHashCallBacks](nsobjecthashcallbacks.md) — For sets of objects (similar to `NSSet`).
- [NSOwnedObjectIdentityHashCallBacks](nsownedobjectidentityhashcallbacks.md) — For sets of objects, with transfer of ownership upon insertion, using pointer equality.
- [NSOwnedPointerHashCallBacks](nsownedpointerhashcallbacks.md) — For sets of pointers, with transfer of ownership upon insertion.
- [NSPointerToStructHashCallBacks](nspointertostructhashcallbacks.md) — For sets of pointers to structs, when the first field of the struct is `int`-sized.

## See Also

### Deprecated
