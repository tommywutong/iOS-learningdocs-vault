---
title: 'replace(with:where:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simd4/replace(with:where:)-7e4sy'
source_url: 'https://developer.apple.com/documentation/swift/simd4/replace(with:where:)-7e4sy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd4/replace%28with%3Awhere%3A%29-7e4sy.json'
content_hash: 'sha256:6305c053c69a2d62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD4](../simd4.md)

# replace(with:where:)

<sub>Instance Method</sub>

Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replace(with other: Self, where mask: SIMDMask<Self.MaskStorage>)
```

## Discussion

Equivalent to:

```swift
for i in indices {
  if mask[i] { self[i] = other[i] }
}
```
