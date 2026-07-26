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
doc_path: '/documentation/swift/simd4/init(repeating:)-gu1y'
source_url: 'https://developer.apple.com/documentation/swift/simd4/init(repeating:)-gu1y'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd4/init%28repeating%3A%29-gu1y.json'
content_hash: 'sha256:e737c100b091e10e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD4](../simd4.md)

# init(repeating:)

<sub>Initializer</sub>

A vector with the specified scalar in all lanes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(repeating scalar: Double)
```

## Discussion

Equivalent to:

```swift
var result = SIMD4<Double>()
for i in result.indices {
  result[i] = scalar
}
```
