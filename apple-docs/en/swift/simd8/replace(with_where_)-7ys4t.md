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
doc_path: '/documentation/swift/simd8/replace(with:where:)-7ys4t'
source_url: 'https://developer.apple.com/documentation/swift/simd8/replace(with:where:)-7ys4t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd8/replace%28with%3Awhere%3A%29-7ys4t.json'
content_hash: 'sha256:cbc3f8406e94a18a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD8](../simd8.md)

# replace(with:where:)

<sub>Instance Method</sub>

Replaces elements of this vector with `other` in the lanes where `mask` is `true`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replace(with other: Self.Scalar, where mask: SIMDMask<Self.MaskStorage>)
```

## Discussion

Equivalent to:

```swift
for i in indices {
  if mask[i] { self[i] = other }
}
```
