---
title: 'init(style:allowedUnits:spellsOutZero:includesActualByteCount:locale:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bytecountformatstyle/init(style:allowedunits:spellsoutzero:includesactualbytecount:locale:)'
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatstyle/init(style:allowedunits:spellsoutzero:includesactualbytecount:locale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatstyle/init%28style%3Aallowedunits%3Aspellsoutzero%3Aincludesactualbytecount%3Alocale%3A%29.json'
content_hash: 'sha256:4cd2af4d958a845a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatStyle](../bytecountformatstyle.md)

# init(style:allowedUnits:spellsOutZero:includesActualByteCount:locale:)

<sub>Initializer</sub>

Initializes a byte count format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(style: ByteCountFormatStyle.Style = .file, allowedUnits: ByteCountFormatStyle.Units = .all, spellsOutZero: Bool = true, includesActualByteCount: Bool = false, locale: Locale = .autoupdatingCurrent)
```

## Parameters

- `style` — The style of byte count to express, such as memory or file system storage.

- `allowedUnits` — The units the format style can use to express the byte count.

- `spellsOutZero` — A Boolean value that indicates whether the format style should spell out zero-byte values as text, like `Zero kB`.

- `includesActualByteCount` — A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units. For example, `1 kB (1,024 bytes)`.

- `locale` — The locale to use to format the numeric part of the byte count.

## Discussion

In situations that can infer the [ByteCountFormatStyle](../bytecountformatstyle.md) type, you can call [byteCount(style:allowedUnits:spellsOutZero:includesActualByteCount:)](<../formatstyle/bytecount(style_allowedunits_spellsoutzero_includesactualbytecount_)-59ep0.md>) instead of explicitly using this initializer. This is the case when you call [formatted(_:)](<../../swift/binaryinteger/formatted(__)-4qd73.md>) on a [BinaryInteger](../../swift/binaryinteger.md).

## See Also

### Creating a byte count style

- [Units](units.md) — The units to use when formatting a byte count, such as kilobytes or gigabytes.
