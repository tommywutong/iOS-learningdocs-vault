---
title: AutoreleasingUnsafeMutablePointer
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/autoreleasingunsafemutablepointer
source_url: 'https://developer.apple.com/documentation/swift/autoreleasingunsafemutablepointer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/autoreleasingunsafemutablepointer.json'
content_hash: 'sha256:54bc0bae50fc402a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AutoreleasingUnsafeMutablePointer

<sub>Structure</sub>

A mutable pointer addressing an Objective-C reference that doesn’t own its target.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct AutoreleasingUnsafeMutablePointer<Pointee>
```

## Overview

`Pointee` must be a class type or `Optional<C>` where `C` is a class.

This type has implicit conversions to allow passing any of the following to a C or ObjC API:

- `nil`, which gets passed as a null pointer,
- an inout argument of the referenced type, which gets passed as a pointer to a writeback temporary with autoreleasing ownership semantics,
- an `UnsafeMutablePointer<Pointee>`, which is passed as-is.

Passing pointers to mutable arrays of ObjC class pointers is not directly supported. Unlike `UnsafeMutablePointer<Pointee>`, `AutoreleasingUnsafeMutablePointer<Pointee>` must reference storage that does not own a reference count to the referenced value. UnsafeMutablePointer’s operations, by contrast, assume that the referenced storage owns values loaded from or stored to it.

This type does not carry an owner pointer unlike the other C*Pointer types because it only needs to reference the results of inout conversions, which already have writeback-scoped lifetime.

## Relationships

- **Conforms To**: [BitwiseCopyable](bitwisecopyable.md), [CVarArg](cvararg.md), [Comparable](comparable.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [CustomReflectable](customreflectable.md), [Equatable](equatable.md), [Escapable](escapable.md), [Hashable](hashable.md), [Strideable](strideable.md)

## Topics

### Converting Pointers

- [init(_:)](<autoreleasingunsafemutablepointer/init(__)-7rndr.md>) — Explicit construction from an UnsafeMutablePointer.
- [init(_:)](<autoreleasingunsafemutablepointer/init(__)-4mrz1.md>) — Explicit construction from an UnsafeMutablePointer.

### Accessing a Pointer’s Memory

- [pointee](autoreleasingunsafemutablepointer/pointee.md) — Retrieve or set the `Pointee` instance referenced by `self`.
- [subscript(_:)](<autoreleasingunsafemutablepointer/subscript(__).md>) — Access the `i`th element of the raw array pointed to by `self`.

### Comparing Pointers

- [==(_:_:)](<autoreleasingunsafemutablepointer/==(____)-4wfti.md>) — Returns a Boolean value indicating whether two values are equal.

### Instance Properties

- [hashValue](autoreleasingunsafemutablepointer/hashvalue.md) — The hash value.

### Type Aliases

- [Stride](autoreleasingunsafemutablepointer/stride.md) — A type that represents the distance between two values.

### Default Implementations

- [Comparable Implementations](autoreleasingunsafemutablepointer/comparable-implementations.md)
- [CustomReflectable Implementations](autoreleasingunsafemutablepointer/customreflectable-implementations.md)
- [Equatable Implementations](autoreleasingunsafemutablepointer/equatable-implementations.md)
- [Hashable Implementations](autoreleasingunsafemutablepointer/hashable-implementations.md)
- [Strideable Implementations](autoreleasingunsafemutablepointer/strideable-implementations.md)

## See Also

### C and Objective-C Pointers

- [OpaquePointer](opaquepointer.md) — A wrapper around an opaque C pointer.
