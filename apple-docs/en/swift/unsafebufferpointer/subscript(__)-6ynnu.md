---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafebufferpointer/subscript(_:)-6ynnu'
source_url: 'https://developer.apple.com/documentation/swift/unsafebufferpointer/subscript(_:)-6ynnu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafebufferpointer/subscript%28_%3A%29-6ynnu.json'
content_hash: 'sha256:f876faa65a4b7247'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeBufferPointer](../unsafebufferpointer.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses a contiguous subrange of the buffer’s elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(bounds: Range<Int>) -> Slice<UnsafeBufferPointer<Element>> { get }
```

## Parameters

- `bounds` — A range of the buffer’s indices. The bounds of the range must be valid indices of the buffer.

## Overview

The accessed slice uses the same indices for the same elements as the original buffer uses. Always use the slice’s `startIndex` property instead of assuming that its indices start at a particular value.

This example demonstrates getting a slice from a buffer of strings, finding the index of one of the strings in the slice, and then using that index in the original buffer.

```swift
let streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
streets.withUnsafeBufferPointer { buffer in
    let streetSlice = buffer[2..<buffer.endIndex]
    print(Array(streetSlice))
    // Prints "["Channing", "Douglas", "Evarts"]"
    let index = streetSlice.firstIndex(of: "Evarts")    // 4
    print(buffer[index!])
    // Prints "Evarts"
}
```

> [!note] Note
> Bounds checks for `bounds` are performed only in debug mode.
