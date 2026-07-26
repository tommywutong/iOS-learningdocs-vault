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
doc_path: '/documentation/swift/simd16/init(repeating:)-cisq'
source_url: 'https://developer.apple.com/documentation/swift/simd16/init(repeating:)-cisq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd16/init%28repeating%3A%29-cisq.json'
content_hash: 'sha256:1738ea9ed20fc150'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD16](../simd16.md)

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
var result = SIMD16<Float16>()
for i in result.indices {
  result[i] = scalar
}
```
