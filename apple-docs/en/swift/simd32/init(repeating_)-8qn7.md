---
title: 'init(repeating:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simd32/init(repeating:)-8qn7'
source_url: 'https://developer.apple.com/documentation/swift/simd32/init(repeating:)-8qn7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd32/init%28repeating%3A%29-8qn7.json'
content_hash: 'sha256:8d42874e8ca1a1ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD32](../simd32.md)

# init(repeating:)

<sub>Initializer</sub>

A vector with the specified scalar in all lanes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(repeating scalar: UInt64)
```

## Discussion

Equivalent to:

```swift
var result = SIMD32<UInt64>()
for i in result.indices {
  result[i] = scalar
}
```
