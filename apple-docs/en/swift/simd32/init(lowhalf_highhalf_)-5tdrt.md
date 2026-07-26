---
title: 'init(lowHalf:highHalf:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simd32/init(lowhalf:highhalf:)-5tdrt'
source_url: 'https://developer.apple.com/documentation/swift/simd32/init(lowhalf:highhalf:)-5tdrt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd32/init%28lowhalf%3Ahighhalf%3A%29-5tdrt.json'
content_hash: 'sha256:f88af2d3f64eaeb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD32](../simd32.md)

# init(lowHalf:highHalf:)

<sub>Initializer</sub>

A vector formed by concatenating lowHalf and highHalf.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(lowHalf: SIMD16<Scalar>, highHalf: SIMD16<Scalar>)
```

## Discussion

Equivalent to:

```swift
var result = SIMD32<Scalar>()
for i in 0..<16 {
  result[i] = lowHalf[i]
  result[16+i] = highHalf[i]
}
```
