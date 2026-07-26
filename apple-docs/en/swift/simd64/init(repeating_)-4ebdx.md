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
doc_path: '/documentation/swift/simd64/init(repeating:)-4ebdx'
source_url: 'https://developer.apple.com/documentation/swift/simd64/init(repeating:)-4ebdx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd64/init%28repeating%3A%29-4ebdx.json'
content_hash: 'sha256:612665883ac93270'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD64](../simd64.md)

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
var result = SIMD64<Float16>()
for i in result.indices {
  result[i] = scalar
}
```
