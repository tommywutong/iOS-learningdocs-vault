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
doc_path: '/documentation/swift/unsafemutablebufferpointer/init(mutating:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/init(mutating:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/init%28mutating%3A%29.json'
content_hash: 'sha256:bd7edcb20e98ea78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# init(mutating:)

<sub>Initializer</sub>

Creates a mutable typed buffer pointer referencing the same memory as the given immutable buffer pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(mutating other: UnsafeBufferPointer<Element>)
```

## Parameters

- `other` — The immutable buffer pointer to convert.
