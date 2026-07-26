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
doc_path: '/documentation/swift/simdmask/replacing(with:where:)-7uyp7'
source_url: 'https://developer.apple.com/documentation/swift/simdmask/replacing(with:where:)-7uyp7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simdmask/replacing%28with%3Awhere%3A%29-7uyp7.json'
content_hash: 'sha256:53a3b903c36bcc80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMDMask](../simdmask.md)

# replacing(with:where:)

<sub>Instance Method</sub>

Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacing(with other: SIMDMask<Storage>, where mask: SIMDMask<Storage>) -> SIMDMask<Storage>
```

## Discussion

Equivalent to:

```swift
var result = Self()
for i in indices {
  result[i] = mask[i] ? other[i] : self[i]
}
```
