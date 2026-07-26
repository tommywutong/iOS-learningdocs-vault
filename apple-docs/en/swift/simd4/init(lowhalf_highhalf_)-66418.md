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
doc_path: '/documentation/swift/simd4/init(lowhalf:highhalf:)-66418'
source_url: 'https://developer.apple.com/documentation/swift/simd4/init(lowhalf:highhalf:)-66418'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd4/init%28lowhalf%3Ahighhalf%3A%29-66418.json'
content_hash: 'sha256:ac1ebae0346e2399'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD4](../simd4.md)

# init(lowHalf:highHalf:)

<sub>Initializer</sub>

A vector formed by concatenating lowHalf and highHalf.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(lowHalf: SIMD2<Double>, highHalf: SIMD2<Double>)
```

## Discussion

Equivalent to:

```swift
var result = SIMD4<Double>()
for i in 0..<2 {
  result[i] = lowHalf[i]
  result[2+i] = highHalf[i]
}
```
