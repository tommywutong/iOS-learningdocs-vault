---
title: 'initialize(from:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablepointer/initialize(from:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablepointer/initialize(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablepointer/initialize%28from%3A%29.json'
content_hash: 'sha256:4071f3b59467cdee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutablePointer](../unsafemutablepointer.md)

# initialize(from:)

<sub>Instance Method</sub>

Initializes memory starting at this pointer’s address with the elements of the given collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func initialize<C>(from source: C) where Pointee == C.Element, C : Collection
```

## Parameters

- `source` — A collection of elements of the pointer’s `Pointee` type.

## Discussion

The region of memory starting at this pointer and covering `source.count` instances of the pointer’s `Pointee` type must be uninitialized or `Pointee` must be a trivial type. After calling `initialize(from:)`, the region is initialized.
