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
doc_path: /documentation/foundation/formatstyle/number-7fxvo
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/number-7fxvo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/number-7fxvo.json'
content_hash: 'sha256:af00b674c8ddb0e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# number

<sub>Type Property</sub>

A style for formatting the Swift default integer type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var number: IntegerFormatStyle<Int> { get }
```

## Discussion

Use this type property when the call point allows the use of [IntegerFormatStyle](../integerformatstyle.md). You typically do this when calling the `formatted` methods of types that conform to [BinaryInteger](../../swift/binaryinteger.md).

## See Also

### Applying numeric styles for integers

- [number](number-4ttgp.md) — A style for formatting the Swift unsigned integer type.
- [number](number-5hzgj.md) — A style for formatting 8-bit signed integers.
- [number](number-1o8fx.md) — A style for formatting 16-bit signed integers.
- [number](number-4cj49.md) — A style for formatting 32-bit signed integers.
- [number](number-3925i.md) — A style for formatting 64-bit signed integers.
- [number](number-8fms6.md) — A style for formatting 8-bit unsigned integers.
- [number](number-fak0.md) — A style for formatting 16-bit unsigned integers.
- [number](number-13mra.md) — A style for formatting 32-bit unsigned integers.
- [number](number-iyry.md) — A style for formatting 64-bit unsigned integers.
- [IntegerFormatStyle](../integerformatstyle.md) — A structure that converts between integer values and their textual representations.
