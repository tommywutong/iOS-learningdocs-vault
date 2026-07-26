---
title: NSMapTable
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmaptable
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptable.json'
content_hash: 'sha256:13e23d150b039b4e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMapTable

<sub>Class</sub>

A collection similar to a dictionary, but with a broader range of available memory semantics.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMapTable<KeyType, ObjectType> where KeyType : AnyObject, ObjectType : AnyObject
```

## Overview

The map table is modeled after [NSDictionary](nsdictionary.md) with the following differences:

- Keys and/or values are optionally held “weakly” such that entries are removed when one of the objects is reclaimed.
- Its keys or values may be copied on input or may use pointer identity for equality and hashing.
- It can contain arbitrary pointers (its contents are not constrained to being objects).

You can configure an [NSMapTable](nsmaptable.md) instance to operate on arbitrary pointers and not just objects, although typically you are encouraged to use the C function API for void * pointers. The object-based API (such as [- setObject:forKey:](<nsmaptable/setobject(__forkey_).md>)) will not work for non-object pointers without type-casting.

When configuring map tables, note that only the options listed in [NSMapTableOptions](nsmaptableoptions.md) guarantee that the rest of the API will work correctly—including copying, archiving, and fast enumeration. While other [NSPointerFunctions](nspointerfunctions.md) options are used for certain configurations, such as to hold arbitrary pointers, not all combinations of the options are valid. With some combinations the map table may not work correctly, or may not even be initialized correctly.

### Subclassing Notes

`NSMapTable` is not suitable for subclassing.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSFastEnumeration](nsfastenumeration.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Creating and Initializing a Map Table

- [- initWithKeyOptions:valueOptions:capacity:](<nsmaptable/init(keyoptions_valueoptions_capacity_).md>) — Returns a map table, initialized with the given options.
- [+ mapTableWithKeyOptions:valueOptions:](<nsmaptable/init(keyoptions_valueoptions_).md>) — Returns a new map table, initialized with the given options
- [- initWithKeyPointerFunctions:valuePointerFunctions:capacity:](<nsmaptable/init(keypointerfunctions_valuepointerfunctions_capacity_).md>) — Returns a map table, initialized with the given functions.
- [+ strongToStrongObjectsMapTable](<nsmaptable/strongtostrongobjects().md>) — Returns a new map table object which has strong references to the keys and values.
- [+ weakToStrongObjectsMapTable](<nsmaptable/weaktostrongobjects().md>) — Returns a new map table object which has weak references to the keys and strong references to the values.
- [+ strongToWeakObjectsMapTable](<nsmaptable/strongtoweakobjects().md>) — Returns a new map table object which has strong references to the keys and weak references to the values.
- [+ weakToWeakObjectsMapTable](<nsmaptable/weaktoweakobjects().md>) — Returns a new map table object which has weak references to the keys and values.
- [NSMapTableOptions](nsmaptableoptions.md) — Constants used as components in a bitfield to specify the behavior of elements (keys and values) in an `NSMapTable` object.

### Accessing Content

- [- objectForKey:](<nsmaptable/object(forkey_).md>) — Returns a the value associated with a given key.
- [- keyEnumerator](<nsmaptable/keyenumerator().md>) — Returns an enumerator object that lets you access each key in the map table.
- [- objectEnumerator](<nsmaptable/objectenumerator().md>) — Returns an enumerator object that lets you access each value in the map table.
- [count](nsmaptable/count.md) — The number of key-value pairs in the map table.

### Manipulating Content

- [- setObject:forKey:](<nsmaptable/setobject(__forkey_).md>) — Adds a given key-value pair to the map table.
- [- removeObjectForKey:](<nsmaptable/removeobject(forkey_).md>) — Removes a given key and its associated value from the map table.
- [- removeAllObjects](<nsmaptable/removeallobjects().md>) — Empties the map table of its entries.

### Creating a Dictionary Representation

- [- dictionaryRepresentation](<nsmaptable/dictionaryrepresentation().md>) — Returns a dictionary representation of the map table.

### Accessing Pointer Functions

- [keyPointerFunctions](nsmaptable/keypointerfunctions.md) — The pointer functions the map table uses to manage keys.
- [valuePointerFunctions](nsmaptable/valuepointerfunctions.md) — The pointer functions the map table uses to manage values.
- [NSPointerFunctions](nspointerfunctions.md) — An instance of `NSPointerFunctions` defines callout functions appropriate for managing a pointer reference held somewhere else.

### Deprecated

- [Legacy Map Table Implementation](legacy-map-table-implementation.md)

### Initializers

- [init(coder:)](<nsmaptable/init(coder_).md>)

## See Also

### Pointer Collections

- [NSPointerArray](nspointerarray.md) — A collection similar to an array, but with a broader range of available memory semantics.
- [NSHashTable](nshashtable.md) — A collection similar to a set, but with broader range of available memory semantics.
