---
title: 'init(literalCapacity:interpolationCount:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/defaultstringinterpolation/init(literalcapacity:interpolationcount:)'
source_url: 'https://developer.apple.com/documentation/swift/defaultstringinterpolation/init(literalcapacity:interpolationcount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/defaultstringinterpolation/init%28literalcapacity%3Ainterpolationcount%3A%29.json'
content_hash: 'sha256:c9085785c047732d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DefaultStringInterpolation](../defaultstringinterpolation.md)

# init(literalCapacity:interpolationCount:)

<sub>Initializer</sub>

Creates a string interpolation with storage pre-sized for a literal with the indicated attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(literalCapacity: Int, interpolationCount: Int)
```

## Discussion

You don’t need to call this initializer directly. It’s used by the compiler when interpreting string interpolations.
