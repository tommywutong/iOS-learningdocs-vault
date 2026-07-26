---
title: words
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int128/words-swift.property
source_url: 'https://developer.apple.com/documentation/swift/int128/words-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/words-swift.property.json'
content_hash: 'sha256:49ed47e7d7ec29c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int128](../int128.md)

# words

<sub>Instance Property</sub>

A collection containing the words of this value’s binary representation, in order from the least significant to most significant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var words: UInt128.Words { get }
```

## Discussion

Negative values are returned in two’s complement representation, regardless of the type’s underlying implementation.
