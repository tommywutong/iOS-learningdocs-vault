---
title: formattingContext
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bytecountformatter/formattingcontext
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatter/formattingcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatter/formattingcontext.json'
content_hash: 'sha256:6869e04ad66e8131'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatter](../bytecountformatter.md)

# formattingContext

<sub>Instance Property</sub>

Specify the formatting context for the formatted string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var formattingContext: Formatter.Context { get set }
```

## Discussion

The default value is `NSFormattingContextUnknown`. See [Formatter](../formatter.md) for possible values.

## See Also

### Setting Formatting Styles

- [countStyle](countstyle-swift.property.md) — Specify the number of bytes to be used for kilobytes.
- [allowsNonnumericFormatting](allowsnonnumericformatting.md) — Determines whether to allow more natural display of some values.
- [includesActualByteCount](includesactualbytecount.md) — Determines whether to include the number of bytes after the formatted string.
- [adaptive](isadaptive.md) — Determines the display style of the size representation.
- [allowedUnits](allowedunits.md) — Specify the units that can be used in the output.
- [includesCount](includescount.md) — Determines whether to include the count in the resulting formatted string.
- [includesUnit](includesunit.md) — Determines whether to include the units in the resulting formatted string.
- [zeroPadsFractionDigits](zeropadsfractiondigits.md) — Determines whether to zero pad fraction digits so a consistent number of characters is displayed in a representation.
