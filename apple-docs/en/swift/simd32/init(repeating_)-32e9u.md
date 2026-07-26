---
title: 'init(repeating:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simd32/init(repeating:)-32e9u'
source_url: 'https://developer.apple.com/documentation/swift/simd32/init(repeating:)-32e9u'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd32/init%28repeating%3A%29-32e9u.json'
content_hash: 'sha256:8391fefe9b12da25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD32](../simd32.md)

# init(repeating:)

<sub>Initializer</sub>

A vector with the specified scalar in all lanes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(repeating scalar: Float16)
```

## Discussion

Equivalent to:

```swift
var result = SIMD32<Float16>()
for i in result.indices {
  result[i] = scalar
}
```
