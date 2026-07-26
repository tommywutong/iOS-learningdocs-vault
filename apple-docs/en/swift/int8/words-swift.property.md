---
title: words
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int8/words-swift.property
source_url: 'https://developer.apple.com/documentation/swift/int8/words-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int8/words-swift.property.json'
content_hash: 'sha256:3f89522c6682c0b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int8](../int8.md)

# words

<sub>Instance Property</sub>

A collection containing the words of this value’s binary representation, in order from the least significant to most significant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var words: Int8.Words { get }
```

## Discussion

Negative values are returned in two’s complement representation, regardless of the type’s underlying implementation.
