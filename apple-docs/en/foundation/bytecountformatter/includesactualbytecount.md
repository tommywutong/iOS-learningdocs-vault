---
title: includesActualByteCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bytecountformatter/includesactualbytecount
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatter/includesactualbytecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatter/includesactualbytecount.json'
content_hash: 'sha256:2095d2e46a956130'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatter](../bytecountformatter.md)

# includesActualByteCount

<sub>Instance Property</sub>

Determines whether to include the number of bytes after the formatted string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var includesActualByteCount: Bool { get set }
```

## Discussion

Setting this value to [true](../../swift/true.md) causes the byte count to be displayed parenthetically (localized as appropriate), for instance `723 KB (722,842 bytes)`.  This will happen only if needed, that is, the first part is already not showing the exact byte count.

If [includesUnit](includesunit.md) or [includesCount](includescount.md) are [false](../../swift/false.md), then this setting has no effect.

Default value is [false](../../swift/false.md).

## See Also

### Setting Formatting Styles

- [formattingContext](formattingcontext.md) — Specify the formatting context for the formatted string.
- [countStyle](countstyle-swift.property.md) — Specify the number of bytes to be used for kilobytes.
- [allowsNonnumericFormatting](allowsnonnumericformatting.md) — Determines whether to allow more natural display of some values.
- [adaptive](isadaptive.md) — Determines the display style of the size representation.
- [allowedUnits](allowedunits.md) — Specify the units that can be used in the output.
- [includesCount](includescount.md) — Determines whether to include the count in the resulting formatted string.
- [includesUnit](includesunit.md) — Determines whether to include the units in the resulting formatted string.
- [zeroPadsFractionDigits](zeropadsfractiondigits.md) — Determines whether to zero pad fraction digits so a consistent number of characters is displayed in a representation.
