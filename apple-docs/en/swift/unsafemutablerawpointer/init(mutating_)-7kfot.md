---
title: 'init(mutating:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablerawpointer/init(mutating:)-7kfot'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawpointer/init(mutating:)-7kfot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawpointer/init%28mutating%3A%29-7kfot.json'
content_hash: 'sha256:5288d0e61df5ea75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawPointer](../unsafemutablerawpointer.md)

# init(mutating:)

<sub>Initializer</sub>

Creates a new mutable raw pointer from the given immutable raw pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(mutating other: UnsafeRawPointer)
```

## Parameters

- `other` — The immutable raw pointer to convert.

## Discussion

Use this initializer to explicitly convert `other` to an `UnsafeMutableRawPointer` instance. This initializer creates a new pointer to the same address as `other` and performs no allocation or copying.
