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
doc_path: '/documentation/swift/simd32/init(repeating:)-5l6wp'
source_url: 'https://developer.apple.com/documentation/swift/simd32/init(repeating:)-5l6wp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd32/init%28repeating%3A%29-5l6wp.json'
content_hash: 'sha256:185447042624a10a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD32](../simd32.md)

# init(repeating:)

<sub>Initializer</sub>

A vector with the specified scalar in all lanes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(repeating scalar: Int16)
```

## Discussion

Equivalent to:

```swift
var result = SIMD32<Int16>()
for i in result.indices {
  result[i] = scalar
}
```
