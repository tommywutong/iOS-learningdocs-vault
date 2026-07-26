---
title: style
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurement/formatstyle/bytecount/style-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/measurement/formatstyle/bytecount/style-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/formatstyle/bytecount/style-swift.property.json'
content_hash: 'sha256:91be7ee453682fd7'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Measurement](../../../measurement.md) · [FormatStyle](../../formatstyle.md) · [ByteCount](../bytecount.md)

# style

<sub>Instance Property</sub>

The style of byte count to express, such as memory or file system storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var style: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Style
```

## See Also

### Accessing style properties

- [allowedUnits](allowedunits.md) — The units the format style can use to express the byte count.
- [Units](units.md) — The type the measurement format style uses to represent byte-counting units.
- [spellsOutZero](spellsoutzero.md) — A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [includesActualByteCount](includesactualbytecount.md) — A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.
- [Style](style-swift.typealias.md) — The type used to represent the style of the formatted byte count.
- [locale](locale.md) — The locale to use to format the numeric part of the byte count.
