---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float16/init(_:)-77b3g'
source_url: 'https://developer.apple.com/documentation/swift/float16/init(_:)-77b3g'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/init%28_%3A%29-77b3g.json'
content_hash: 'sha256:4ed93adcaf8d2064'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# init(_:)

<sub>Initializer</sub>

Creates a new instance initialized to the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ other: Float16)
```

## Parameters

- `other` — The value to use for the new instance.

## Discussion

The value of `other` is represented exactly by the new instance. A NaN passed as `other` results in another NaN, with a signaling NaN value converted to quiet NaN.

```swift
let x: Float16 = 21.25
let y = Float16(x)
// y == 21.25

let z = Float16(Float16.nan)
// z.isNaN == true
```
