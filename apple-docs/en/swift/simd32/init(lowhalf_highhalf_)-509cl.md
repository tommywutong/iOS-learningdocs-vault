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
doc_path: '/documentation/swift/simd32/init(lowhalf:highhalf:)-509cl'
source_url: 'https://developer.apple.com/documentation/swift/simd32/init(lowhalf:highhalf:)-509cl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd32/init%28lowhalf%3Ahighhalf%3A%29-509cl.json'
content_hash: 'sha256:79082bd2d4f70e2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD32](../simd32.md)

# init(lowHalf:highHalf:)

<sub>Initializer</sub>

A vector formed by concatenating lowHalf and highHalf.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(lowHalf: SIMD16<Float>, highHalf: SIMD16<Float>)
```

## Discussion

Equivalent to:

```swift
var result = SIMD32<Float>()
for i in 0..<16 {
  result[i] = lowHalf[i]
  result[16+i] = highHalf[i]
}
```
