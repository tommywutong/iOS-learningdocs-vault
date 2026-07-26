---
title: NSHashTable
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nshashtable
source_url: 'https://developer.apple.com/documentation/foundation/nshashtable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtable.json'
content_hash: 'sha256:2bc25ffdf9f0d4d4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSHashTable

<sub>Class</sub>

A collection similar to a set, but with broader range of available memory semantics.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSHashTable<ObjectType> where ObjectType : AnyObject
```

## Overview

The hash table is modeled after [NSSet](nsset.md) with the following differences:

- It can hold weak references to its members.
- Its members may be copied on input or may use pointer identity for equality and hashing.
- It can contain arbitrary pointers (its members are not constrained to being objects).

You can configure an [NSHashTable](nshashtable.md) instance to operate on arbitrary pointers and not just objects, although typically you are encouraged to use the C function API for void * pointers. The object-based API (such as [- addObject:](<nshashtable/add(__).md>)) will not work for non-object pointers without type-casting.

Because of its options, `NSHashTable` is not a set because it can behave differently (for example, if pointer equality is specified two `isEqual:` strings will both be entered).

When configuring hash tables, note that only the options listed in [NSHashTableOptions](nshashtableoptions.md) guarantee that the rest of the API will work correctly—including copying, archiving, and fast enumeration. While other [NSPointerFunctions](nspointerfunctions.md) options are used for certain configurations, such as to hold arbitrary pointers, not all combinations of the options are valid. With some combinations the hash table may not work correctly, or may not even be initialized correctly.

### Subclassing Notes

`NSHashTable` is not suitable for subclassing.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSFastEnumeration](nsfastenumeration.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Initialization

- [- initWithOptions:capacity:](<nshashtable/init(options_capacity_).md>) — Returns a hash table initialized with the given attributes.
- [- initWithPointerFunctions:capacity:](<nshashtable/init(pointerfunctions_capacity_).md>) — Returns a hash table initialized with the given functions and capacity.

### Convenience Constructors

- [+ weakObjectsHashTable](<nshashtable/weakobjects().md>) — Returns a new hash table for storing weak references to its contents.
- [+ hashTableWithOptions:](<nshashtable/init(options_).md>) — Returns a hash table with given pointer functions options.

### Accessing Content

- [anyObject](nshashtable/anyobject.md) — One of the objects in the hash table.
- [allObjects](nshashtable/allobjects.md) — The hash table’s members.
- [setRepresentation](nshashtable/setrepresentation.md) — A set that contains the hash table’s members.
- [count](nshashtable/count.md) — The number of elements in the hash table.
- [- containsObject:](<nshashtable/contains(__).md>) — Returns a Boolean value that indicates whether the hash table contains a given object.
- [- member:](<nshashtable/member(__).md>) — Determines whether the hash table contains a given object, and returns that object if it is present
- [- objectEnumerator](<nshashtable/objectenumerator().md>) — Returns an enumerator object that lets you access each object in the hash table.

### Manipulating Membership

- [- addObject:](<nshashtable/add(__).md>) — Adds a given object to the hash table.
- [- removeObject:](<nshashtable/remove(__).md>) — Removes a given object from the hash table.
- [- removeAllObjects](<nshashtable/removeallobjects().md>) — Removes all objects from the hash table.

### Comparing Hash Tables

- [- intersectHashTable:](<nshashtable/intersect(__).md>) — Removes from the receiving hash table each element that isn’t a member of another given hash table.
- [- intersectsHashTable:](<nshashtable/intersects(__).md>) — Returns a Boolean value that indicates whether a given hash table intersects with the receiving hash table.
- [- isSubsetOfHashTable:](<nshashtable/issubset(of_).md>) — Returns a Boolean value that indicates whether every element in the receiving hash table is also present in another given hash table.
- [- isEqualToHashTable:](<nshashtable/isequal(to_).md>) — Returns a Boolean value that indicates whether a given hash table is equal to the receiving hash table.

### Set Functions

- [- minusHashTable:](<nshashtable/minus(__).md>) — Removes each element in another given hash table from the receiving hash table, if present.
- [- unionHashTable:](<nshashtable/union(__).md>) — Adds each element in another given hash table to the receiving hash table, if not present.

### Accessing Pointer Functions

- [pointerFunctions](nshashtable/pointerfunctions.md) — The pointer functions for the hash table.
- [NSPointerFunctions](nspointerfunctions.md) — An instance of `NSPointerFunctions` defines callout functions appropriate for managing a pointer reference held somewhere else.

### Constants

- [NSHashTableOptions](nshashtableoptions.md) — Components in a bit-field to specify the behavior of elements in an [NSHashTable](nshashtable.md) object.

### Deprecated

- [Legacy Hash Table Implementation](legacy-hash-table-implementation.md)

### Initializers

- [init(coder:)](<nshashtable/init(coder_).md>)

## See Also

### Pointer Collections

- [NSPointerArray](nspointerarray.md) — A collection similar to an array, but with a broader range of available memory semantics.
- [NSMapTable](nsmaptable.md) — A collection similar to a dictionary, but with a broader range of available memory semantics.
