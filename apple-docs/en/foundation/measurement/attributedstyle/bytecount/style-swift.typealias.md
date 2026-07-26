---
title: Measurement.AttributedStyle.ByteCount.Style
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurement/attributedstyle/bytecount/style-swift.typealias
source_url: 'https://developer.apple.com/documentation/foundation/measurement/attributedstyle/bytecount/style-swift.typealias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/attributedstyle/bytecount/style-swift.typealias.json'
content_hash: 'sha256:4bec6732283be319'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Measurement](../../../measurement.md) · [AttributedStyle](../../attributedstyle.md) · [ByteCount](../bytecount.md)

# Measurement.AttributedStyle.ByteCount.Style

<sub>Type Alias</sub>

The type used to represent the style of the formatted byte count.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Style = ByteCountFormatStyle.Style
```

## Discussion

This format style uses the [Style](../../../bytecountformatstyle/style-swift.enum.md) type to represent the byte-count style.

## See Also

### Accessing style properties

- [allowedUnits](allowedunits.md) — The units the format style can use to express the byte count.
- [Units](units.md) — The type the measurement format style uses to represent byte-counting units.
- [spellsOutZero](spellsoutzero.md) — A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [includesActualByteCount](includesactualbytecount.md) — A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.
- [style](style-swift.property.md) — The style of byte count to express, such as memory or file system storage.
- [locale](locale.md) — The locale to use to format the numeric part of the byte count.
