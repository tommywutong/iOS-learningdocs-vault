---
title: exponentBitPattern
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/exponentbitpattern
source_url: 'https://developer.apple.com/documentation/swift/float80/exponentbitpattern'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/exponentbitpattern.json'
content_hash: 'sha256:db29ff3013c81fc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# exponentBitPattern

<sub>Instance Property</sub>

The raw encoding of the value’s exponent field.

<sub>macOS</sub>

```swift
var exponentBitPattern: UInt { get }
```

## Discussion

This value is unadjusted by the type’s exponent bias.
