---
title: includesCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bytecountformatter/includescount
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatter/includescount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatter/includescount.json'
content_hash: 'sha256:4dbdf4e2a73cb9ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatter](../bytecountformatter.md)

# includesCount

<sub>Instance Property</sub>

Determines whether to include the count in the resulting formatted string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var includesCount: Bool { get set }
```

## Discussion

If set to [true](../../swift/true.md) and [includesUnit](includesunit.md) is set to [false](../../swift/false.md), no unit is displayed. For example, a value of 723 KB is formatted as `723`.

You can get the set this property to [true](../../swift/true.md) and the [includesUnit](includesunit.md) to [true](../../swift/true.md) individually to get both parts, separately. Note that putting them together yourself via string concatenation may be incorrect for some locales.

The default value is [true](../../swift/true.md).

> [!note] Note
> Setting this value to [false](../../swift/false.md) and [allowedUnits](allowedunits.md) to [false](../../swift/false.md) results in an empty string.

## See Also

### Setting Formatting Styles

- [formattingContext](formattingcontext.md) — Specify the formatting context for the formatted string.
- [countStyle](countstyle-swift.property.md) — Specify the number of bytes to be used for kilobytes.
- [allowsNonnumericFormatting](allowsnonnumericformatting.md) — Determines whether to allow more natural display of some values.
- [includesActualByteCount](includesactualbytecount.md) — Determines whether to include the number of bytes after the formatted string.
- [adaptive](isadaptive.md) — Determines the display style of the size representation.
- [allowedUnits](allowedunits.md) — Specify the units that can be used in the output.
- [includesUnit](includesunit.md) — Determines whether to include the units in the resulting formatted string.
- [zeroPadsFractionDigits](zeropadsfractiondigits.md) — Determines whether to zero pad fraction digits so a consistent number of characters is displayed in a representation.
