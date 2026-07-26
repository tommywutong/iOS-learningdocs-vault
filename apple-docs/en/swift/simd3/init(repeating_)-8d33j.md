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
doc_path: '/documentation/swift/simd3/init(repeating:)-8d33j'
source_url: 'https://developer.apple.com/documentation/swift/simd3/init(repeating:)-8d33j'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd3/init%28repeating%3A%29-8d33j.json'
content_hash: 'sha256:96cc08c2f0a0c50a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD3](../simd3.md)

# init(repeating:)

<sub>Initializer</sub>

A vector with the specified scalar in all lanes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(repeating scalar: Int8)
```

## Discussion

Equivalent to:

```swift
var result = SIMD3<Int8>()
for i in result.indices {
  result[i] = scalar
}
```
