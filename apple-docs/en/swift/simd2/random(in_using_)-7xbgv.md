---
title: 'random(in:using:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simd2/random(in:using:)-7xbgv'
source_url: 'https://developer.apple.com/documentation/swift/simd2/random(in:using:)-7xbgv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd2/random%28in%3Ausing%3A%29-7xbgv.json'
content_hash: 'sha256:d0b029240690b17b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD2](../simd2.md)

# random(in:using:)

<sub>Type Method</sub>

Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func random<T>(in range: Range<Self.Scalar>, using generator: inout T) -> Self where T : RandomNumberGenerator
```
