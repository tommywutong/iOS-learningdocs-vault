---
title: 'update(from:count:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablepointer/update(from:count:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablepointer/update(from:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablepointer/update%28from%3Acount%3A%29.json'
content_hash: 'sha256:443ba9d637c0e6de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutablePointer](../unsafemutablepointer.md)

# update(from:count:)

<sub>Instance Method</sub>

Update this pointer’s initialized memory with the specified number of instances, copied from the given pointer’s memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func update(from source: UnsafePointer<Pointee>, count: Int)
```

## Parameters

- `source` — A pointer to at least `count` initialized instances of type `Pointee`. The memory regions referenced by `source` and this pointer may overlap.

- `count` — The number of instances to copy from the memory referenced by `source` to this pointer’s memory. `count` must not be negative.

## Discussion

The region of memory starting at this pointer and covering `count` instances of the pointer’s `Pointee` type must be initialized or `Pointee` must be a trivial type. After calling `update(from:count:)`, the region is initialized.

> [!note] Note
> Returns without performing work if `self` and `source` are equal.
