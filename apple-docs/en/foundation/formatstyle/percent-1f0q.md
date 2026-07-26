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
doc_path: /documentation/foundation/formatstyle/percent-1f0q
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/percent-1f0q'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/percent-1f0q.json'
content_hash: 'sha256:a29fca20aca9c723'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# percent

<sub>Type Property</sub>

A style for formatting 32-bit signed integers as a percent representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var percent: IntegerFormatStyle<Int32>.Percent { get }
```

## Discussion

Use this type property when the call point allows the use of [IntegerFormatStyle](../integerformatstyle.md). You typically do this when calling the `formatted` methods of types that conform to [BinaryInteger](../../swift/binaryinteger.md).

## See Also

### Applying percentage styles for integers

- [percent](percent-cl9k.md) — A style for formatting signed integer types in Swift as a percent representation.
- [percent](percent-9pj79.md) — A style for formatting signed integer types in Swift as a percent representation.
- [percent](percent-7r4rl.md) — A style for formatting 8-bit signed integers as a percent representation.
- [percent](percent-3qjzh.md) — A style for formatting 16-bit signed integers as a percent representation.
- [percent](percent-934se.md) — A style for formatting 64-bit signed integers as a percent representation.
- [percent](percent-8izzv.md) — A style for formatting 8-bit unsigned integers as a percent representation.
- [percent](percent-4kdme.md) — A style for formatting 16-bit unsigned integers as a percent representation.
- [percent](percent-2f11j.md) — A style for formatting 32-bit unsigned integers as a percent representation.
- [percent](percent-8bxla.md) — A style for formatting 64-bit unsigned integers as a percent representation.
- [Percent](../integerformatstyle/percent.md) — A format style that converts between integer percentage values and their textual representations.
