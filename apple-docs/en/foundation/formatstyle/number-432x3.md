---
title: number
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/formatstyle/number-432x3
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/number-432x3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/number-432x3.json'
content_hash: 'sha256:3b0c9df18eea2d46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# number

<sub>Type Property</sub>

A style for formatting the Swift standard single-precision floating-point type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var number: FloatingPointFormatStyle<Float> { get }
```

## Discussion

Use this type property when the call point allows the use of [FloatingPointFormatStyle](../floatingpointformatstyle.md). You typically do this when calling the `formatted` methods of types that conform to [BinaryFloatingPoint](../../swift/binaryfloatingpoint.md).

## See Also

### Applying numeric styles for floating-point values

- [number](number-8c8rj.md) — A style for formatting the Swift standard double-precision floating-point type.
- [number](number-3qe2o.md) — A style for formatting 16-bit floating-point values.
- [FloatingPointFormatStyle](../floatingpointformatstyle.md) — A structure that converts between floating-point values and their textual representations.
