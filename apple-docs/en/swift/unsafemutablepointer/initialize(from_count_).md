---
title: 'initialize(from:count:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablepointer/initialize(from:count:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablepointer/initialize(from:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablepointer/initialize%28from%3Acount%3A%29.json'
content_hash: 'sha256:d411649a1a146dce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutablePointer](../unsafemutablepointer.md)

# initialize(from:count:)

<sub>Instance Method</sub>

Initializes the memory referenced by this pointer with the values starting at the given pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func initialize(from source: UnsafePointer<Pointee>, count: Int)
```

## Parameters

- `source` — A pointer to the values to copy. The memory region `source..<(source + count)` must be initialized. The memory regions referenced by `source` and this pointer must not overlap.

- `count` — The number of instances to move from `source` to this pointer’s memory. `count` must not be negative.

## Discussion

The region of memory starting at this pointer and covering `count` instances of the pointer’s `Pointee` type must be uninitialized or `Pointee` must be a trivial type. After calling `initialize(from:count:)`, the region is initialized.

> [!note] Note
> The source and destination memory regions must not overlap.
