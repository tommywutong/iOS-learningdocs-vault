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
doc_path: '/documentation/swift/simd32/init(lowhalf:highhalf:)-9kbcj'
source_url: 'https://developer.apple.com/documentation/swift/simd32/init(lowhalf:highhalf:)-9kbcj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd32/init%28lowhalf%3Ahighhalf%3A%29-9kbcj.json'
content_hash: 'sha256:0d5709cd206984b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD32](../simd32.md)

# init(lowHalf:highHalf:)

<sub>Initializer</sub>

A vector formed by concatenating lowHalf and highHalf.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(lowHalf: SIMD16<Double>, highHalf: SIMD16<Double>)
```

## Discussion

Equivalent to:

```swift
var result = SIMD32<Double>()
for i in 0..<16 {
  result[i] = lowHalf[i]
  result[16+i] = highHalf[i]
}
```
