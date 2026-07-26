---
title: Elements
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazysequenceprotocol/elements-swift.associatedtype
source_url: 'https://developer.apple.com/documentation/swift/lazysequenceprotocol/elements-swift.associatedtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazysequenceprotocol/elements-swift.associatedtype.json'
content_hash: 'sha256:5fb7dd09530b304e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazySequenceProtocol](../lazysequenceprotocol.md)

# Elements

<sub>Associated Type</sub>

A `Sequence` that can contain the same elements as this one, possibly with a simpler type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Elements : Sequence = Self where Self.Element == Self.Elements.Element
```

## Discussion

- See also: `elements`
