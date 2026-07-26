---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsaferawpointer/init(_:)-76a4f'
source_url: 'https://developer.apple.com/documentation/swift/unsaferawpointer/init(_:)-76a4f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawpointer/init%28_%3A%29-76a4f.json'
content_hash: 'sha256:88c4d3fba83c3074'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeRawPointer](../unsaferawpointer.md)

# init(_:)

<sub>Initializer</sub>

Creates a new raw pointer from the given typed pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?<T>(_ other: UnsafeMutablePointer<T>?) where T : ~Copyable
```

## Parameters

- `other` — The typed pointer to convert. If `other` is `nil`, the result is `nil`.

## Discussion

Use this initializer to explicitly convert `other` to an `UnsafeRawPointer` instance. This initializer creates a new pointer to the same address as `other` and performs no allocation or copying.
