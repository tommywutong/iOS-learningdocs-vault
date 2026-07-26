---
title: isAdaptive
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bytecountformatter/isadaptive
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatter/isadaptive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatter/isadaptive.json'
content_hash: 'sha256:079b2e4c88d8bea0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatter](../bytecountformatter.md)

# isAdaptive

<sub>Instance Property</sub>

Determines the display style of the size representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isAdaptive: Bool { get set }
```

## Discussion

The “adaptive” algorithm is platform specific and uses a different number of fraction digits based on the magnitude (in OS X v10.8: 0 fraction digits for bytes and KB; 1 fraction digits for MB; 2 for GB and above). Otherwise the result always tries to show at least three significant digits, introducing fraction digits as necessary.

Default is [true](../../swift/true.md).

## See Also

### Setting Formatting Styles

- [formattingContext](formattingcontext.md) — Specify the formatting context for the formatted string.
- [countStyle](countstyle-swift.property.md) — Specify the number of bytes to be used for kilobytes.
- [allowsNonnumericFormatting](allowsnonnumericformatting.md) — Determines whether to allow more natural display of some values.
- [includesActualByteCount](includesactualbytecount.md) — Determines whether to include the number of bytes after the formatted string.
- [allowedUnits](allowedunits.md) — Specify the units that can be used in the output.
- [includesCount](includescount.md) — Determines whether to include the count in the resulting formatted string.
- [includesUnit](includesunit.md) — Determines whether to include the units in the resulting formatted string.
- [zeroPadsFractionDigits](zeropadsfractiondigits.md) — Determines whether to zero pad fraction digits so a consistent number of characters is displayed in a representation.
