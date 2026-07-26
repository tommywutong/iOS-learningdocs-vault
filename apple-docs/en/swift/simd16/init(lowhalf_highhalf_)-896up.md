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
doc_path: '/documentation/swift/simd16/init(lowhalf:highhalf:)-896up'
source_url: 'https://developer.apple.com/documentation/swift/simd16/init(lowhalf:highhalf:)-896up'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd16/init%28lowhalf%3Ahighhalf%3A%29-896up.json'
content_hash: 'sha256:b83f6e6b0045da80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD16](../simd16.md)

# init(lowHalf:highHalf:)

<sub>Initializer</sub>

A vector formed by concatenating lowHalf and highHalf.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(lowHalf: SIMD8<Int64>, highHalf: SIMD8<Int64>)
```

## Discussion

Equivalent to:

```swift
var result = SIMD16<Int64>()
for i in 0..<8 {
  result[i] = lowHalf[i]
  result[8+i] = highHalf[i]
}
```
