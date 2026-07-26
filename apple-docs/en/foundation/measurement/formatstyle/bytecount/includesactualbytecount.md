---
title: includesActualByteCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurement/formatstyle/bytecount/includesactualbytecount
source_url: 'https://developer.apple.com/documentation/foundation/measurement/formatstyle/bytecount/includesactualbytecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/formatstyle/bytecount/includesactualbytecount.json'
content_hash: 'sha256:151d4ba3fcb3727b'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Measurement](../../../measurement.md) · [FormatStyle](../../formatstyle.md) · [ByteCount](../bytecount.md)

# includesActualByteCount

<sub>Instance Property</sub>

A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var includesActualByteCount: Bool
```

## Discussion

When this value is `true`, a format style produces output like `1 kB (1,024 bytes)`.

## See Also

### Accessing style properties

- [allowedUnits](allowedunits.md) — The units the format style can use to express the byte count.
- [Units](units.md) — The type the measurement format style uses to represent byte-counting units.
- [spellsOutZero](spellsoutzero.md) — A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [style](style-swift.property.md) — The style of byte count to express, such as memory or file system storage.
- [Style](style-swift.typealias.md) — The type used to represent the style of the formatted byte count.
- [locale](locale.md) — The locale to use to format the numeric part of the byte count.
