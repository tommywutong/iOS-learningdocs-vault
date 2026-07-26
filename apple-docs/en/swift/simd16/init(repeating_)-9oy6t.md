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
doc_path: '/documentation/swift/simd16/init(repeating:)-9oy6t'
source_url: 'https://developer.apple.com/documentation/swift/simd16/init(repeating:)-9oy6t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd16/init%28repeating%3A%29-9oy6t.json'
content_hash: 'sha256:de862a3a1b70f9b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD16](../simd16.md)

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
var result = SIMD16<Int16>()
for i in result.indices {
  result[i] = scalar
}
```
