---
title: Measurement.AttributedStyle.ByteCount.Units
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurement/attributedstyle/bytecount/units
source_url: 'https://developer.apple.com/documentation/foundation/measurement/attributedstyle/bytecount/units'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/attributedstyle/bytecount/units.json'
content_hash: 'sha256:17775cc011732778'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Measurement](../../../measurement.md) · [AttributedStyle](../../attributedstyle.md) · [ByteCount](../bytecount.md)

# Measurement.AttributedStyle.ByteCount.Units

<sub>Type Alias</sub>

The type the measurement format style uses to represent byte-counting units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Units = ByteCountFormatStyle.Units
```

## Discussion

This format style uses the [Units](../../../bytecountformatstyle/units.md) structure to represent the available units.

## See Also

### Accessing style properties

- [allowedUnits](allowedunits.md) — The units the format style can use to express the byte count.
- [spellsOutZero](spellsoutzero.md) — A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [includesActualByteCount](includesactualbytecount.md) — A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.
- [style](style-swift.property.md) — The style of byte count to express, such as memory or file system storage.
- [Style](style-swift.typealias.md) — The type used to represent the style of the formatted byte count.
- [locale](locale.md) — The locale to use to format the numeric part of the byte count.
