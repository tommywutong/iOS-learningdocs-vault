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
doc_path: '/documentation/swift/unsafemutablepointer/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablepointer/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablepointer/subscript%28_%3A%29.json'
content_hash: 'sha256:ada8abba392d368d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutablePointer](../unsafemutablepointer.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Reads or updates the pointee at the specified offset from this pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(i: Int) -> Pointee { get nonmutating set }
```

## Parameters

- `i` — The offset from this pointer at which to access an instance, measured in strides of the pointer’s `Pointee` type.

## Overview

For a pointer `p`, the memory at `p + i` must be initialized when reading the value by using the subscript. When the subscript is used as the left side of an assignment, the memory at `p + i` is updated. The memory must be initialized or the pointer’s `Pointee` type must be a trivial type.

Uninitialized memory cannot be initialized to a nontrivial type using this subscript. Instead, use an initializing method, such as `initialize(to:)`.
