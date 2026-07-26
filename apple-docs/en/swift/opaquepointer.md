---
title: OpaquePointer
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/opaquepointer
source_url: 'https://developer.apple.com/documentation/swift/opaquepointer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/opaquepointer.json'
content_hash: 'sha256:ee192427c2d43032'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# OpaquePointer

<sub>Structure</sub>

A wrapper around an opaque C pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct OpaquePointer
```

## Overview

Opaque pointers are used to represent C pointers to types that cannot be represented in Swift, such as incomplete struct types.

## Relationships

- **Conforms To**: [AtomicOptionalRepresentable](../synchronization/atomicoptionalrepresentable.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BitwiseCopyable](bitwisecopyable.md), [CVarArg](cvararg.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [Equatable](equatable.md), [Escapable](escapable.md), [Hashable](hashable.md)

## Topics

### Initializers

- [init(_:)](<opaquepointer/init(__)-3h8av.md>)
- [init(_:)](<opaquepointer/init(__)-4g6sp.md>)
- [init(_:)](<opaquepointer/init(__)-4u1ar.md>) — Converts a typed `UnsafePointer` to an opaque C pointer.
- [init(_:)](<opaquepointer/init(__)-6gmth.md>)
- [init(_:)](<opaquepointer/init(__)-7oa0u.md>) — Converts a typed `UnsafeMutablePointer` to an opaque C pointer.
- [init(_:)](<opaquepointer/init(__)-7zxvo.md>)
- [init(_:)](<opaquepointer/init(__)-b58i.md>) — Converts a typed `UnsafePointer` to an opaque C pointer.
- [init(_:)](<opaquepointer/init(__)-xapj.md>) — Converts a typed `UnsafeMutablePointer` to an opaque C pointer.
- [init(bitPattern:)](<opaquepointer/init(bitpattern_)-26uvs.md>) — Creates a new `OpaquePointer` from the given address, specified as a bit pattern.
- [init(bitPattern:)](<opaquepointer/init(bitpattern_)-7f8tm.md>) — Creates a new `OpaquePointer` from the given address, specified as a bit pattern.

### Instance Properties

- [intendedSpatialExperience](opaquepointer/intendedspatialexperience.md) — The AudioQueue’s intended spatial audio experience.

### Default Implementations

- [AtomicOptionalRepresentable Implementations](opaquepointer/atomicoptionalrepresentable-implementations.md)
- [AtomicRepresentable Implementations](opaquepointer/atomicrepresentable-implementations.md)
- [CustomDebugStringConvertible Implementations](opaquepointer/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](opaquepointer/equatable-implementations.md)
- [Hashable Implementations](opaquepointer/hashable-implementations.md)

## See Also

### C and Objective-C Pointers

- [AutoreleasingUnsafeMutablePointer](autoreleasingunsafemutablepointer.md) — A mutable pointer addressing an Objective-C reference that doesn’t own its target.
