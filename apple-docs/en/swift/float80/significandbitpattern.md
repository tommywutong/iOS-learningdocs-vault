---
title: significandBitPattern
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/significandbitpattern
source_url: 'https://developer.apple.com/documentation/swift/float80/significandbitpattern'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/significandbitpattern.json'
content_hash: 'sha256:c0ba1c9c78bf013c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# significandBitPattern

<sub>Instance Property</sub>

The raw encoding of the value’s significand field.

<sub>macOS</sub>

```swift
var significandBitPattern: UInt64 { get }
```

## Discussion

The `significandBitPattern` property does not include the leading integral bit of the significand, even for types like `Float80` that store it explicitly.
