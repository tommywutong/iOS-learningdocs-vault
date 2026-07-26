---
title: 'init(fromSplitComplex:scale:count:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/init(fromsplitcomplex:scale:count:)-5eirc'
source_url: 'https://developer.apple.com/documentation/swift/array/init(fromsplitcomplex:scale:count:)-5eirc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/init%28fromsplitcomplex%3Ascale%3Acount%3A%29-5eirc.json'
content_hash: 'sha256:75751fc126df8eeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# init(fromSplitComplex:scale:count:)

<sub>Initializer</sub>

Creates a new array of single-precision values from a `DSPSplitComplex` structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(fromSplitComplex splitComplex: DSPSplitComplex, scale: Float, count: Int)
```

## Parameters

- `scale` — A multiplier to apply during conversion.

- `count` — The length of the required resulting array (typically half the count of either the real or imaginary parts of the `DSPSplitComplex`.
