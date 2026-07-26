---
title: NSPointerArray
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspointerarray
source_url: 'https://developer.apple.com/documentation/foundation/nspointerarray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerarray.json'
content_hash: 'sha256:c5271e11113a194d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSPointerArray

<sub>Class</sub>

A collection similar to an array, but with a broader range of available memory semantics.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSPointerArray
```

## Overview

The pointer array class is modeled after [NSArray](nsarray.md), but can also hold `nil` values. You can insert or remove `nil` values which contribute to the array’s [count](nspointerarray/count.md).

A pointer array can be initialized to maintain strong or weak references to objects, or according to any of the memory or personality options defined by [Options](nspointerfunctions/options.md).

The [NSCopying](nscopying.md) and [NSCoding](nscoding.md) protocols are applicable only when a pointer array is initialized to maintain strong or weak references to objects.

When enumerating a pointer array with [NSFastEnumeration](nsfastenumeration.md) using `for...in`, the loop will yield any `nil` values present in the array. See [Fast Enumeration Makes It Easy to Enumerate a Collection](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/FoundationTypesandCollections/FoundationTypesandCollections.html#//apple_ref/doc/uid/TP40011210-CH7-SW30) in [Programming with Objective-C](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011210) for more information.

### Subclassing Notes

`NSPointerArray` is not suitable for subclassing.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSFastEnumeration](nsfastenumeration.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Creating and Initializing a New Pointer Array

- [- initWithOptions:](<nspointerarray/init(options_).md>) — Initializes the receiver to use the given options.
- [- initWithPointerFunctions:](<nspointerarray/init(pointerfunctions_).md>) — Initializes the receiver to use the given functions.
- [+ strongObjectsPointerArray](<nspointerarray/strongobjects().md>) — Returns a new pointer array that maintains strong references to its elements.
- [+ weakObjectsPointerArray](<nspointerarray/weakobjects().md>) — Returns a new pointer array that maintains weak references to its elements.

### Managing the Collection

- [count](nspointerarray/count.md) — The number of elements in the receiver.
- [allObjects](nspointerarray/allobjects.md) — All the objects in the receiver.
- [- pointerAtIndex:](<nspointerarray/pointer(at_).md>) — Returns the pointer at a given index.
- [- addPointer:](<nspointerarray/addpointer(__).md>) — Adds a given pointer to the receiver.
- [- removePointerAtIndex:](<nspointerarray/removepointer(at_).md>) — Removes the pointer at a given index.
- [- insertPointer:atIndex:](<nspointerarray/insertpointer(__at_).md>) — Inserts a pointer at a given index.
- [- replacePointerAtIndex:withPointer:](<nspointerarray/replacepointer(at_withpointer_).md>) — Replaces the pointer at a given index.
- [- compact](<nspointerarray/compact().md>) — Removes `NULL` values from the receiver.

### Getting the Pointer Functions

- [pointerFunctions](nspointerarray/pointerfunctions.md) — The functions in use by the receiver.
- [NSPointerFunctions](nspointerfunctions.md) — An instance of `NSPointerFunctions` defines callout functions appropriate for managing a pointer reference held somewhere else.

### Initializers

- [init(coder:)](<nspointerarray/init(coder_).md>)

## See Also

### Pointer Collections

- [NSMapTable](nsmaptable.md) — A collection similar to a dictionary, but with a broader range of available memory semantics.
- [NSHashTable](nshashtable.md) — A collection similar to a set, but with broader range of available memory semantics.
