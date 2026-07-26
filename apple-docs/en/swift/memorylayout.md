---
title: MemoryLayout
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/memorylayout
source_url: 'https://developer.apple.com/documentation/swift/memorylayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/memorylayout.json'
content_hash: 'sha256:e1e94f72f50f9026'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# MemoryLayout

<sub>Enumeration</sub>

The memory layout of a type, describing its size, stride, and alignment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum MemoryLayout<T> where T : ~Copyable, T : ~Escapable
```

## Overview

You can use `MemoryLayout` as a source of information about a type when allocating or binding memory using raw pointers. The following example declares a `Point` type with `x` and `y` coordinates and a Boolean `isFilled` property.

```swift
struct Point {
    let x: Double
    let y: Double
    let isFilled: Bool
}
```

The size, stride, and alignment of the `Point` type are accessible as static properties of `MemoryLayout<Point>`.

```swift
// MemoryLayout<Point>.size == 17
// MemoryLayout<Point>.stride == 24
// MemoryLayout<Point>.alignment == 8
```

Always use a multiple of a type’s `stride` instead of its `size` when allocating memory or accounting for the distance between instances in memory. This example allocates uninitialized raw memory with space for four instances of `Point`.

```swift
let count = 4
let pointPointer = UnsafeMutableRawPointer.allocate(
        byteCount: count * MemoryLayout<Point>.stride,
        alignment: MemoryLayout<Point>.alignment)
```

## Relationships

- **Conforms To**: [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Accessing the Layout of a Type

- [size](memorylayout/size.md) — The contiguous memory footprint of `T`, in bytes.
- [alignment](memorylayout/alignment.md) — The default memory alignment of `T`, in bytes.
- [stride](memorylayout/stride.md) — The number of bytes from the start of one instance of `T` to the start of the next when stored in contiguous memory or in an `Array<T>`.

### Accessing the Layout of a Value

- [stride(ofValue:)](<memorylayout/stride(ofvalue_).md>) — Returns the number of bytes from the start of one instance of `T` to the start of the next when stored in contiguous memory or in an `Array<T>`.
- [size(ofValue:)](<memorylayout/size(ofvalue_).md>) — Returns the contiguous memory footprint of the given instance.
- [alignment(ofValue:)](<memorylayout/alignment(ofvalue_).md>) — Returns the default memory alignment of `T`.

### Querying Type Properties

- [offset(of:)](<memorylayout/offset(of_).md>) — Returns the offset of an inline stored property within a type’s in-memory representation.
