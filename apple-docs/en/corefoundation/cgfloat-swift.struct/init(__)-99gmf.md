---
title: 'init(_:)'
framework: Core Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS, watchOS 2.0+, Swift（4.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cgfloat-swift.struct/init(_:)-99gmf'
source_url: 'https://developer.apple.com/documentation/corefoundation/cgfloat-swift.struct/init(_:)-99gmf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cgfloat-swift.struct/init%28_%3A%29-99gmf.json'
content_hash: 'sha256:0aacddbe0612a306'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CGFloat](../cgfloat-swift.struct.md)

# init(_:)

<sub>Initializer</sub>

Creates a new value, rounded to the closest possible representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ number: NSNumber)
```

## Parameters

- `number` — The number to convert to a floating-point value.

## Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.
