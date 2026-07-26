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
doc_path: '/documentation/swift/unsafemutablebufferpointer/subscript(_:)-2vl82'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/subscript(_:)-2vl82'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/subscript%28_%3A%29-2vl82.json'
content_hash: 'sha256:8f1c6ee5b4b60194'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(i: Int) -> Element { get nonmutating set }
```

## Parameters

- `i` — The position of the element to access. `i` must be in the range `0..<count`.

## Overview

The following example uses the buffer pointer’s subscript to access and modify the elements of a mutable buffer pointing to the contiguous contents of an array:

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.withUnsafeMutableBufferPointer { buffer in
    for i in stride(from: buffer.startIndex, to: buffer.endIndex - 1, by: 2) {
        let x = buffer[i]
        buffer[i + 1] = buffer[i]
        buffer[i] = x
    }
}
print(numbers)
// Prints "[2, 1, 4, 3, 5]"
```

Uninitialized memory cannot be initialized to a nontrivial type using this subscript. Instead, use an initializing method, such as `initializeElement(at:to:)`

> [!note] Note
> Bounds checks for `i` are performed only in debug mode.
