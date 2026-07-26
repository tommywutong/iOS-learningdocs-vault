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
doc_path: '/documentation/swift/float80/init(_:)-33oy4'
source_url: 'https://developer.apple.com/documentation/swift/float80/init(_:)-33oy4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/init%28_%3A%29-33oy4.json'
content_hash: 'sha256:08ceaa3daaa33332'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# init(_:)

<sub>Initializer</sub>

Creates a new value, rounded to the closest possible representation.

<sub>macOS</sub>

```swift
init<Source>(_ value: Source) where Source : BinaryInteger
```

## Parameters

- `value` — The integer to convert to a floating-point value.

## Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.
