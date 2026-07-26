---
title: percent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/formatstyle/percent-2gva1
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/percent-2gva1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/percent-2gva1.json'
content_hash: 'sha256:6dea3862779ad006'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# percent

<sub>Type Property</sub>

A style for formatting the Swift standard single-precision floating-point type as a percent representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var percent: FloatingPointFormatStyle<Float>.Percent { get }
```

## Discussion

Use this type property when the call point allows the use of [FloatingPointFormatStyle](../floatingpointformatstyle.md). You typically do this when calling the `formatted` methods of types that conform to [BinaryFloatingPoint](../../swift/binaryfloatingpoint.md).

## See Also

### Applying percentage styles for floating-point values

- [percent](percent-6cwuv.md) — A style for formatting the Swift standard single-precision floating-point type as a percent representation.
- [percent](percent-grss.md) — A style for formatting 16-bit floating-point values as a percent representation.
- [Percent](../floatingpointformatstyle/percent.md) — A format style that converts between floating-point percentage values and their textual representations.
