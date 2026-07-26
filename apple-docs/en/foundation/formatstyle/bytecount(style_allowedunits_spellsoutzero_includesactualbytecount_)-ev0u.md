---
title: 'byteCount(style:allowedUnits:spellsOutZero:includesActualByteCount:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatstyle/bytecount(style:allowedunits:spellsoutzero:includesactualbytecount:)-ev0u'
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/bytecount(style:allowedunits:spellsoutzero:includesactualbytecount:)-ev0u'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/bytecount%28style%3Aallowedunits%3Aspellsoutzero%3Aincludesactualbytecount%3A%29-ev0u.json'
content_hash: 'sha256:2e315563faa54e57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# byteCount(style:allowedUnits:spellsOutZero:includesActualByteCount:)

<sub>Type Method</sub>

Returns a format style to format a data storage value represented with Foundation’s measurement type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func byteCount(style: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Style, allowedUnits: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Units = .all, spellsOutZero: Bool = true, includesActualByteCount: Bool = false) -> Self
```

## Parameters

- `style` — The style of byte count to express, such as memory or file system storage.

- `allowedUnits` — The units the format style can use to express the byte count.

- `spellsOutZero` — A Boolean value that indicates whether the format style should spell out zero-byte values as text, like `Zero kB`.

- `includesActualByteCount` — A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units. For example, `1 kB (1,024 bytes)`.

## Return Value

A format style for formatting a measurement of data storage, customized with the provided behaviors.

## Discussion

Use this type method when the call point allows the use of [ByteCount](../measurement/formatstyle/bytecount.md). You typically do this when calling the [formatted()](<../measurement/formatted().md>) on a [Measurement](../measurement.md) whose unit type is [UnitInformationStorage](../unitinformationstorage.md), as seen in the following example.

```swift
let count = Measurement(value: 1024, unit: UnitInformationStorage.bytes)
let formatted = count.formatted(.byteCount(style: .memory)) // "1 kB"
```

## See Also

### Applying byte-count styles

- [byteCount(style:allowedUnits:spellsOutZero:includesActualByteCount:)](<bytecount(style_allowedunits_spellsoutzero_includesactualbytecount_)-59ep0.md>) — Returns a format style to format a data storage value.
- [ByteCountFormatStyle](../bytecountformatstyle.md) — A format style that provides string representations of byte counts.
- [ByteCount](../measurement/formatstyle/bytecount.md) — A format style that provides string representations of byte counts, expressed as measurements of information storage.
