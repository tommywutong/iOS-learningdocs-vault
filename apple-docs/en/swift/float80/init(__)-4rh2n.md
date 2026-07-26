---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/init(_:)-4rh2n'
source_url: 'https://developer.apple.com/documentation/swift/float80/init(_:)-4rh2n'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/init%28_%3A%29-4rh2n.json'
content_hash: 'sha256:bf5c89016467e192'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# init(_:)

<sub>Initializer</sub>

Creates a new instance that approximates the given value.

<sub>macOS</sub>

```swift
init(_ other: Double)
```

## Parameters

- `other` — The value to use for the new instance.

## Discussion

The value of `other` is rounded to a representable value, if necessary. A NaN passed as `other` results in another NaN, with a signaling NaN value converted to quiet NaN.

```swift
let x: Double = 21.25
let y = Float80(x)
// y == 21.25

let z = Float80(Double.nan)
// z.isNaN == true
```
