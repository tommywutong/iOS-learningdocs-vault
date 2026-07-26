---
title: locale
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/bytecountformatstyle/locale
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatstyle/locale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatstyle/locale.json'
content_hash: 'sha256:15354c30da44cc36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatStyle](../bytecountformatstyle.md)

# locale

<sub>Instance Property</sub>

The locale to use to format the numeric part of the byte count.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var locale: Locale { get set }
```

## Discussion

To change the format style’s locale, use [locale(_:)](<../formatstyle/locale(__).md>).

## See Also

### Accessing style properties

- [allowedUnits](allowedunits.md) — The units the format style can use to express the byte count.
- [Units](units.md) — The units to use when formatting a byte count, such as kilobytes or gigabytes.
- [spellsOutZero](spellsoutzero.md) — A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [includesActualByteCount](includesactualbytecount.md) — A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.
