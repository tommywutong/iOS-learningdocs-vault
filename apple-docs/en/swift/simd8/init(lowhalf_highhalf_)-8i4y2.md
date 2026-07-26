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
doc_path: '/documentation/swift/simd8/init(lowhalf:highhalf:)-8i4y2'
source_url: 'https://developer.apple.com/documentation/swift/simd8/init(lowhalf:highhalf:)-8i4y2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd8/init%28lowhalf%3Ahighhalf%3A%29-8i4y2.json'
content_hash: 'sha256:d112efed9f34a5da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD8](../simd8.md)

# init(lowHalf:highHalf:)

<sub>Initializer</sub>

A vector formed by concatenating lowHalf and highHalf.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(lowHalf: SIMD4<Int>, highHalf: SIMD4<Int>)
```

## Discussion

Equivalent to:

```swift
var result = SIMD8<Int>()
for i in 0..<4 {
  result[i] = lowHalf[i]
  result[4+i] = highHalf[i]
}
```
