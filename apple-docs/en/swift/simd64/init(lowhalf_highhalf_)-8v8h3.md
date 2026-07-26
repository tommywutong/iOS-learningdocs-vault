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
doc_path: '/documentation/swift/simd64/init(lowhalf:highhalf:)-8v8h3'
source_url: 'https://developer.apple.com/documentation/swift/simd64/init(lowhalf:highhalf:)-8v8h3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd64/init%28lowhalf%3Ahighhalf%3A%29-8v8h3.json'
content_hash: 'sha256:e49e9032955f00eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD64](../simd64.md)

# init(lowHalf:highHalf:)

<sub>Initializer</sub>

A vector formed by concatenating lowHalf and highHalf.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(lowHalf: SIMD32<UInt16>, highHalf: SIMD32<UInt16>)
```

## Discussion

Equivalent to:

```swift
var result = SIMD64<UInt16>()
for i in 0..<32 {
  result[i] = lowHalf[i]
  result[32+i] = highHalf[i]
}
```
