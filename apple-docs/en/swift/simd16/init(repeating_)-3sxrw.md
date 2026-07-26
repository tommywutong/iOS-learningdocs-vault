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
doc_path: '/documentation/swift/simd16/init(repeating:)-3sxrw'
source_url: 'https://developer.apple.com/documentation/swift/simd16/init(repeating:)-3sxrw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd16/init%28repeating%3A%29-3sxrw.json'
content_hash: 'sha256:c553886b07ff4862'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD16](../simd16.md)

# init(repeating:)

<sub>Initializer</sub>

A vector with the specified scalar in all lanes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(repeating scalar: UInt8)
```

## Discussion

Equivalent to:

```swift
var result = SIMD16<UInt8>()
for i in result.indices {
  result[i] = scalar
}
```
