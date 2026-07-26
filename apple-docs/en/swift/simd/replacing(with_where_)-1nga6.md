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
doc_path: '/documentation/swift/simd/replacing(with:where:)-1nga6'
source_url: 'https://developer.apple.com/documentation/swift/simd/replacing(with:where:)-1nga6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd/replacing%28with%3Awhere%3A%29-1nga6.json'
content_hash: 'sha256:de2e4cbb005ac1ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD](../simd.md)

# replacing(with:where:)

<sub>Instance Method</sub>

Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacing(with other: Self, where mask: SIMDMask<Self.MaskStorage>) -> Self
```

## Discussion

Equivalent to:

```swift
var result = Self()
for i in indices {
  result[i] = mask[i] ? other[i] : self[i]
}
```
