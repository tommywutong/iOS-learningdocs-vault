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
doc_path: '/documentation/swift/unsafebufferpointer/init(_:)-36fvm'
source_url: 'https://developer.apple.com/documentation/swift/unsafebufferpointer/init(_:)-36fvm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafebufferpointer/init%28_%3A%29-36fvm.json'
content_hash: 'sha256:489c27772cc60a76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeBufferPointer](../unsafebufferpointer.md)

# init(_:)

<sub>Initializer</sub>

Creates an immutable typed buffer pointer referencing the same memory as the given mutable buffer pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ other: UnsafeMutableBufferPointer<Element>)
```

## Parameters

- `other` — The mutable buffer pointer to convert.
