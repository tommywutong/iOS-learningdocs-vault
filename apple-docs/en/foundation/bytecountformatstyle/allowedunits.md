---
title: allowedUnits
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/bytecountformatstyle/allowedunits
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatstyle/allowedunits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatstyle/allowedunits.json'
content_hash: 'sha256:5cd426bf89e4983d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatStyle](../bytecountformatstyle.md)

# allowedUnits

<sub>Instance Property</sub>

The units the format style can use to express the byte count.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowedUnits: ByteCountFormatStyle.Units { get set }
```

## See Also

### Accessing style properties

- [Units](units.md) — The units to use when formatting a byte count, such as kilobytes or gigabytes.
- [spellsOutZero](spellsoutzero.md) — A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [includesActualByteCount](includesactualbytecount.md) — A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.
- [locale](locale.md) — The locale to use to format the numeric part of the byte count.
