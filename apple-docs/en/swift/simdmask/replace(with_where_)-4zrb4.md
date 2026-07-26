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
doc_path: '/documentation/swift/simdmask/replace(with:where:)-4zrb4'
source_url: 'https://developer.apple.com/documentation/swift/simdmask/replace(with:where:)-4zrb4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simdmask/replace%28with%3Awhere%3A%29-4zrb4.json'
content_hash: 'sha256:24b0c1979d97550c'
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
