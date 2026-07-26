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
doc_path: '/documentation/swift/float16/init(_:)-67cee'
source_url: 'https://developer.apple.com/documentation/swift/float16/init(_:)-67cee'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/init%28_%3A%29-67cee.json'
content_hash: 'sha256:a64031c58c781ba3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# init(_:)

<sub>Initializer</sub>

Creates a new value, rounded to the closest possible representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Source>(_ value: Source) where Source : BinaryInteger
```

## Parameters

- `value` — The integer to convert to a floating-point value.

## Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.
