---
title: zeroPadsFractionDigits
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bytecountformatter/zeropadsfractiondigits
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatter/zeropadsfractiondigits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatter/zeropadsfractiondigits.json'
content_hash: 'sha256:e55604004811f8e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatter](../bytecountformatter.md)

# zeroPadsFractionDigits

<sub>Instance Property</sub>

Determines whether to zero pad fraction digits so a consistent number of characters is displayed in a representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var zeroPadsFractionDigits: Bool { get set }
```

## Discussion

Displaying values using  zero pad fraction digits causes a consistent number of fraction digits are displayed, causing updating displays to remain more stable. For instance, if the [adaptive](isadaptive.md) algorithm is used, this option formats 1.19 and 1.2 GB as `1.19 GB` and `1.20 GB`, respectively, while without the option the latter would be displayed as `1.2 GB`.

The default value is [false](../../swift/false.md).

## See Also

### Setting Formatting Styles

- [formattingContext](formattingcontext.md) — Specify the formatting context for the formatted string.
- [countStyle](countstyle-swift.property.md) — Specify the number of bytes to be used for kilobytes.
- [allowsNonnumericFormatting](allowsnonnumericformatting.md) — Determines whether to allow more natural display of some values.
- [includesActualByteCount](includesactualbytecount.md) — Determines whether to include the number of bytes after the formatted string.
- [adaptive](isadaptive.md) — Determines the display style of the size representation.
- [allowedUnits](allowedunits.md) — Specify the units that can be used in the output.
- [includesCount](includescount.md) — Determines whether to include the count in the resulting formatted string.
- [includesUnit](includesunit.md) — Determines whether to include the units in the resulting formatted string.
