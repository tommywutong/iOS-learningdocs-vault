---
title: NSPointerFunctions
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspointerfunctions
source_url: 'https://developer.apple.com/documentation/foundation/nspointerfunctions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerfunctions.json'
content_hash: 'sha256:e1b80a4afb8ac6bb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSPointerFunctions

<sub>Class</sub>

An instance of `NSPointerFunctions` defines callout functions appropriate for managing a pointer reference held somewhere else.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSPointerFunctions
```

## Overview

The functions specified by an instance of `NSPointerFunctions` are separated into two clusters—those that define “personality” such as “object” or “C-string”, and those that describe memory management issues such as a memory deallocation function. There are constants for common personalities and memory manager selections (see `Memory and Personality Options`).

[NSHashTable](nshashtable.md), [NSMapTable](nsmaptable.md), and [NSPointerArray](nspointerarray.md) use an `NSPointerFunctions` object to define the acquisition and retention behavior for the pointers they manage. Note, however, that not all combinations of personality and memory management behavior are valid for these collections. The pointer collection objects copy the `NSPointerFunctions` object on input and output, so you cannot usefully subclass `NSPointerFunctions`.

### Subclassing Notes

`NSPointerFunctions` is not suitable for subclassing.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating and Initializing an NSPointerFunctions Object

- [- initWithOptions:](<nspointerfunctions/init(options_).md>) — Returns an `NSPointerFunctions` object initialized with the given options.

### Personality Functions

- [hashFunction](nspointerfunctions/hashfunction.md) — The hash function.
- [isEqualFunction](nspointerfunctions/isequalfunction.md) — The function used to compare pointers.
- [sizeFunction](nspointerfunctions/sizefunction.md) — The function used to determine the size of pointers.
- [descriptionFunction](nspointerfunctions/descriptionfunction.md) — The function used to describe elements.

### Memory Configuration

- [acquireFunction](nspointerfunctions/acquirefunction.md) — The function used to acquire memory.
- [relinquishFunction](nspointerfunctions/relinquishfunction.md) — The function used to relinquish memory.
- [usesStrongWriteBarrier](nspointerfunctions/usesstrongwritebarrier.md) — Specifies whether, in a garbage collected environment, pointers should be assigned using a strong write barrier. _(deprecated)_
- [usesWeakReadAndWriteBarriers](nspointerfunctions/usesweakreadandwritebarriers.md) — Specifies whether, in a garbage collected environment, pointers should use weak read and write barriers. _(deprecated)_

### Constants

- [Options](nspointerfunctions/options.md) — Defines the memory and personality options for an `NSPointerFunctions` object.

## See Also

### Accessing Pointer Functions

- [pointerFunctions](nshashtable/pointerfunctions.md) — The pointer functions for the hash table.
