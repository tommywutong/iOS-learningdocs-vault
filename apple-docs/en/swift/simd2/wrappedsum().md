---
title: wrappedSum()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/simd2/wrappedsum()
source_url: 'https://developer.apple.com/documentation/swift/simd2/wrappedsum()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd2/wrappedsum%28%29.json'
content_hash: 'sha256:5364f882e7970e50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD2](../simd2.md)

# wrappedSum()

<sub>Instance Method</sub>

Returns the sum of the scalars in the vector, computed with wrapping addition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func wrappedSum() -> Self.Scalar
```

## Discussion

Equivalent to `indices.reduce(into: 0) { $0 &+= self[$1] }`.
