---
title: 'deinitialize(count:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablepointer/deinitialize(count:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablepointer/deinitialize(count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablepointer/deinitialize%28count%3A%29.json'
content_hash: 'sha256:cf0f1de0ab019c15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutablePointer](../unsafemutablepointer.md)

# deinitialize(count:)

<sub>Instance Method</sub>

Deinitializes the specified number of values starting at this pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func deinitialize(count: Int) -> UnsafeMutableRawPointer
```

## Parameters

- `count` — The number of instances to deinitialize. `count` must not be negative.

## Return Value

A raw pointer to the same address as this pointer. The memory referenced by the returned raw pointer is still bound to `Pointee`.

## Discussion

The region of memory starting at this pointer and covering `count` instances of the pointer’s `Pointee` type must be initialized. After calling `deinitialize(count:)`, the memory is uninitialized, but still bound to the `Pointee` type.
