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
doc_path: '/documentation/swift/float80/init(_:)-5yold'
source_url: 'https://developer.apple.com/documentation/swift/float80/init(_:)-5yold'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/init%28_%3A%29-5yold.json'
content_hash: 'sha256:352884e386ae62cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# init(_:)

<sub>Initializer</sub>

Creates a new instance from the given value, rounded to the closest possible representation.

<sub>macOS</sub>

```swift
init<Source>(_ value: Source) where Source : BinaryFloatingPoint
```

## Parameters

- `value` — A floating-point value to be converted.

## Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.
