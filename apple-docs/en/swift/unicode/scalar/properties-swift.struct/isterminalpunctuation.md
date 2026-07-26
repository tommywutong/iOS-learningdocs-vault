---
title: isTerminalPunctuation
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/isterminalpunctuation
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isterminalpunctuation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/isterminalpunctuation.json'
content_hash: 'sha256:324a2c55ef67c489'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isTerminalPunctuation

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is a punctuation symbol that typically marks the end of a textual unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isTerminalPunctuation: Bool { get }
```

## Discussion

This property corresponds to the “Terminal_Punctuation” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
