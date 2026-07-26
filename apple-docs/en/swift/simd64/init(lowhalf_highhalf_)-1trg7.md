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
doc_path: '/documentation/swift/simd64/init(lowhalf:highhalf:)-1trg7'
source_url: 'https://developer.apple.com/documentation/swift/simd64/init(lowhalf:highhalf:)-1trg7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd64/init%28lowhalf%3Ahighhalf%3A%29-1trg7.json'
content_hash: 'sha256:9687b84cd5227b77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD64](../simd64.md)

# init(lowHalf:highHalf:)

<sub>Initializer</sub>

A vector formed by concatenating lowHalf and highHalf.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(lowHalf: SIMD32<Int>, highHalf: SIMD32<Int>)
```

## Discussion

Equivalent to:

```swift
var result = SIMD64<Int>()
for i in 0..<32 {
  result[i] = lowHalf[i]
  result[32+i] = highHalf[i]
}
```
