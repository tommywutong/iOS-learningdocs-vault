---
title: 'replacing(with:where:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simd4/replacing(with:where:)-3o8ie'
source_url: 'https://developer.apple.com/documentation/swift/simd4/replacing(with:where:)-3o8ie'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd4/replacing%28with%3Awhere%3A%29-3o8ie.json'
content_hash: 'sha256:87e1960688d4e857'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD4](../simd4.md)

# replacing(with:where:)

<sub>Instance Method</sub>

Returns a copy of this vector, with elements `other` in the lanes where `mask` is `true`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacing(with other: Self.Scalar, where mask: SIMDMask<Self.MaskStorage>) -> Self
```

## Discussion

Equivalent to:

```swift
var result = Self()
for i in indices {
  result[i] = mask[i] ? other : self[i]
}
```
