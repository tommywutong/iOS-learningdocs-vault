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
doc_path: '/documentation/swift/simd16/replacing(with:where:)-ng2a'
source_url: 'https://developer.apple.com/documentation/swift/simd16/replacing(with:where:)-ng2a'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd16/replacing%28with%3Awhere%3A%29-ng2a.json'
content_hash: 'sha256:da8cd70daaf2af95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD16](../simd16.md)

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
