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
doc_path: '/documentation/swift/simd3/init(repeating:)-7sm3'
source_url: 'https://developer.apple.com/documentation/swift/simd3/init(repeating:)-7sm3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd3/init%28repeating%3A%29-7sm3.json'
content_hash: 'sha256:01287b614ef084ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD3](../simd3.md)

# init(repeating:)

<sub>Initializer</sub>

A vector with the specified scalar in all lanes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(repeating scalar: Float)
```

## Discussion

Equivalent to:

```swift
var result = SIMD3<Float>()
for i in result.indices {
  result[i] = scalar
}
```
