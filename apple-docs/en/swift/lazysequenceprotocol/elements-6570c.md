---
title: elements
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazysequenceprotocol/elements-6570c
source_url: 'https://developer.apple.com/documentation/swift/lazysequenceprotocol/elements-6570c'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazysequenceprotocol/elements-6570c.json'
content_hash: 'sha256:a9e67ef60e87e485'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazySequenceProtocol](../lazysequenceprotocol.md)

# elements

<sub>Instance Property</sub>

A sequence containing the same elements as this one, possibly with a simpler type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var elements: Self.Elements { get }
```

## Discussion

When implementing lazy operations, wrapping `elements` instead of `self` can prevent result types from growing an extra `LazySequence` layer.

Note: this property need not be implemented by conforming types, it has a default implementation in a protocol extension that just returns `self`.

## Default Implementations

### LazySequenceProtocol Implementations

- [elements](elements-3xrx.md) — Identical to `self`.
