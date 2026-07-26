---
title: exponentBitPattern
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/exponentbitpattern
source_url: 'https://developer.apple.com/documentation/swift/float16/exponentbitpattern'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/exponentbitpattern.json'
content_hash: 'sha256:2f1781a2f0c23fa6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# exponentBitPattern

<sub>Instance Property</sub>

The raw encoding of the value’s exponent field.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var exponentBitPattern: UInt { get }
```

## Discussion

This value is unadjusted by the type’s exponent bias.
