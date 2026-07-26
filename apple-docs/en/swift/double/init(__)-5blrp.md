---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/double/init(_:)-5blrp'
source_url: 'https://developer.apple.com/documentation/swift/double/init(_:)-5blrp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/init%28_%3A%29-5blrp.json'
content_hash: 'sha256:084913cd0f2e4598'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

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

## See Also

### Converting Integers

- [init(_:)](<init(__)-84ohu.md>) — Creates a new value, rounded to the closest possible representation.
