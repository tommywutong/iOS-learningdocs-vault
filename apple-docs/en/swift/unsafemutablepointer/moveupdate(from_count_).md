---
title: 'moveUpdate(from:count:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablepointer/moveupdate(from:count:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablepointer/moveupdate(from:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablepointer/moveupdate%28from%3Acount%3A%29.json'
content_hash: 'sha256:fee67571b3d1c80c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutablePointer](../unsafemutablepointer.md)

# moveUpdate(from:count:)

<sub>Instance Method</sub>

Update this pointer’s initialized memory by moving the specified number of instances the source pointer’s memory, leaving the source memory uninitialized.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func moveUpdate(from source: UnsafeMutablePointer<Pointee>, count: Int)
```

## Parameters

- `source` — A pointer to the values to be moved. The memory region `source..<(source + count)` must be initialized. The memory regions referenced by `source` and this pointer must not overlap.

- `count` — The number of instances to move from `source` to this pointer’s memory. `count` must not be negative.

## Discussion

The region of memory starting at this pointer and covering `count` instances of the pointer’s `Pointee` type must be initialized or `Pointee` must be a trivial type. After calling `moveUpdate(from:count:)`, the region is initialized and the memory region `source..<(source + count)` is uninitialized.

> [!note] Note
> The source and destination memory regions must not overlap.
