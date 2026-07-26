---
title: 'applying(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/simd3/applying(_:)'
source_url: 'https://developer.apple.com/documentation/swift/simd3/applying(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd3/applying%28_%3A%29.json'
content_hash: 'sha256:1cfece7635a81f66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD3](../simd3.md)

# applying(_:)

<sub>Instance Method</sub>

Returns a simd vector that’s transformed by the specified projective transform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func applying(_ transform: ProjectiveTransform3DFloat) -> simd_float3
```

## Parameters

- `transform` — The projective transform.

## Discussion

- Returns The transformed ray.

This function applies the transform to the simd vector.
