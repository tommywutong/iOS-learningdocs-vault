---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/binaryfloatingpoint/init(_:)-17tah'
source_url: 'https://developer.apple.com/documentation/swift/binaryfloatingpoint/init(_:)-17tah'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryfloatingpoint/init%28_%3A%29-17tah.json'
content_hash: 'sha256:a80a9be79c5f7adf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryFloatingPoint](../binaryfloatingpoint.md)

# init(_:)

<sub>Initializer</sub>

Creates a new instance from the given value, rounded to the closest possible representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Source>(_ value: Source) where Source : BinaryFloatingPoint
```

## Parameters

- `value` — A floating-point value to be converted.

## Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.
