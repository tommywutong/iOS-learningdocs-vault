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
doc_path: '/documentation/swift/simdmask/replace(with:where:)-1apjj'
source_url: 'https://developer.apple.com/documentation/swift/simdmask/replace(with:where:)-1apjj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simdmask/replace%28with%3Awhere%3A%29-1apjj.json'
content_hash: 'sha256:b591a881687ba343'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMDMask](../simdmask.md)

# replace(with:where:)

<sub>Instance Method</sub>

Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replace(with other: SIMDMask<Storage>, where mask: SIMDMask<Storage>)
```

## Discussion

Equivalent to:

```swift
for i in indices {
  if mask[i] { self[i] = other[i] }
}
```
