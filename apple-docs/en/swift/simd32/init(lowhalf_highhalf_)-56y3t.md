---
title: 'init(lowHalf:highHalf:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simd32/init(lowhalf:highhalf:)-56y3t'
source_url: 'https://developer.apple.com/documentation/swift/simd32/init(lowhalf:highhalf:)-56y3t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd32/init%28lowhalf%3Ahighhalf%3A%29-56y3t.json'
content_hash: 'sha256:fa027c90be399f13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD32](../simd32.md)

# init(lowHalf:highHalf:)

<sub>Initializer</sub>

A vector formed by concatenating lowHalf and highHalf.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(lowHalf: SIMD16<Float16>, highHalf: SIMD16<Float16>)
```

## Discussion

Equivalent to:

```swift
var result = SIMD32<Float16>()
for i in 0..<16 {
  result[i] = lowHalf[i]
  result[16+i] = highHalf[i]
}
```
