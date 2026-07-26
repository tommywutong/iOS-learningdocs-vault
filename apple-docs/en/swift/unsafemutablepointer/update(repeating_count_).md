---
title: 'update(repeating:count:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablepointer/update(repeating:count:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablepointer/update(repeating:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablepointer/update%28repeating%3Acount%3A%29.json'
content_hash: 'sha256:6fabda9f2b587646'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutablePointer](../unsafemutablepointer.md)

# update(repeating:count:)

<sub>Instance Method</sub>

Update this pointer’s initialized memory with the specified number of consecutive copies of the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func update(repeating repeatedValue: Pointee, count: Int)
```

## Parameters

- `repeatedValue` — The value used when updating this pointer’s memory.

- `count` — The number of consecutive elements to update. `count` must not be negative.

## Discussion

The region of memory starting at this pointer and covering `count` instances of the pointer’s `Pointee` type must be initialized or `Pointee` must be a trivial type. After calling `update(repeating:count:)`, the region is initialized.
