---
title: includesActualByteCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/bytecountformatstyle/includesactualbytecount
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatstyle/includesactualbytecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatstyle/includesactualbytecount.json'
content_hash: 'sha256:8e2a8920e57f3831'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatStyle](../bytecountformatstyle.md)

# includesActualByteCount

<sub>Instance Property</sub>

A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var includesActualByteCount: Bool { get set }
```

## Discussion

When this value is `true`, a format style produces output like `1 kB (1,024 bytes)`.

## See Also

### Accessing style properties

- [allowedUnits](allowedunits.md) — The units the format style can use to express the byte count.
- [Units](units.md) — The units to use when formatting a byte count, such as kilobytes or gigabytes.
- [spellsOutZero](spellsoutzero.md) — A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [locale](locale.md) — The locale to use to format the numeric part of the byte count.
