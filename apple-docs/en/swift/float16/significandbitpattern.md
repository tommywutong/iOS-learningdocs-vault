---
title: significandBitPattern
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/significandbitpattern
source_url: 'https://developer.apple.com/documentation/swift/float16/significandbitpattern'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/significandbitpattern.json'
content_hash: 'sha256:55687ef407e1ccdc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# significandBitPattern

<sub>Instance Property</sub>

The raw encoding of the value’s significand field.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var significandBitPattern: UInt16 { get }
```

## Discussion

The `significandBitPattern` property does not include the leading integral bit of the significand, even for types like `Float80` that store it explicitly.
