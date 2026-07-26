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
doc_path: '/documentation/swift/unsafebufferpointer/subscript(_:)-9vykr'
source_url: 'https://developer.apple.com/documentation/swift/unsafebufferpointer/subscript(_:)-9vykr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafebufferpointer/subscript%28_%3A%29-9vykr.json'
content_hash: 'sha256:0050d53b3ec53ed2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeBufferPointer](../unsafebufferpointer.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(i: Int) -> Element { get }
```

## Parameters

- `i` — The position of the element to access. `i` must be in the range `0..<count`.

## Overview

The following example uses the buffer pointer’s subscript to access every other element of the buffer:

```swift
let numbers = [1, 2, 3, 4, 5]
let sum = numbers.withUnsafeBufferPointer { buffer -> Int in
    var result = 0
    for i in stride(from: buffer.startIndex, to: buffer.endIndex, by: 2) {
        result += buffer[i]
    }
    return result
}
// 'sum' == 9
```

> [!note] Note
> Bounds checks for `i` are performed only in debug mode.
