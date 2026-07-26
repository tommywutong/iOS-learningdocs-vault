---
title: allowsNonnumericFormatting
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bytecountformatter/allowsnonnumericformatting
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatter/allowsnonnumericformatting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatter/allowsnonnumericformatting.json'
content_hash: 'sha256:5070b373fd1b76bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatter](../bytecountformatter.md)

# allowsNonnumericFormatting

<sub>Instance Property</sub>

Determines whether to allow more natural display of some values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowsNonnumericFormatting: Bool { get set }
```

## Discussion

Displays a more natural display of some values, such as zero, where it may be displayed as `Zero KB`, ignoring all other flags or options (with the exception of [NSByteCountFormatterUseBytes](units/usebytes.md), which would generate `Zero bytes`).The result is appropriate for standalone output.

Special handling of certain values such as zero is especially important in some languages, so it’s highly recommended that this property be left in its default state.

Default value is [true](../../swift/true.md).

## See Also

### Setting Formatting Styles

- [formattingContext](formattingcontext.md) — Specify the formatting context for the formatted string.
- [countStyle](countstyle-swift.property.md) — Specify the number of bytes to be used for kilobytes.
- [includesActualByteCount](includesactualbytecount.md) — Determines whether to include the number of bytes after the formatted string.
- [adaptive](isadaptive.md) — Determines the display style of the size representation.
- [allowedUnits](allowedunits.md) — Specify the units that can be used in the output.
- [includesCount](includescount.md) — Determines whether to include the count in the resulting formatted string.
- [includesUnit](includesunit.md) — Determines whether to include the units in the resulting formatted string.
- [zeroPadsFractionDigits](zeropadsfractiondigits.md) — Determines whether to zero pad fraction digits so a consistent number of characters is displayed in a representation.
