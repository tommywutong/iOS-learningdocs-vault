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
doc_path: '/documentation/swift/simd4/init(repeating:)-4xdm7'
source_url: 'https://developer.apple.com/documentation/swift/simd4/init(repeating:)-4xdm7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd4/init%28repeating%3A%29-4xdm7.json'
content_hash: 'sha256:e09757248c339e09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD4](../simd4.md)

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
var result = SIMD4<Float16>()
for i in result.indices {
  result[i] = scalar
}
```
