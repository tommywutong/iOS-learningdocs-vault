---
title: 'init(style:allowedUnits:spellsOutZero:includesActualByteCount:locale:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/measurement/attributedstyle/bytecount/init(style:allowedunits:spellsoutzero:includesactualbytecount:locale:)'
source_url: 'https://developer.apple.com/documentation/foundation/measurement/attributedstyle/bytecount/init(style:allowedunits:spellsoutzero:includesactualbytecount:locale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/attributedstyle/bytecount/init%28style%3Aallowedunits%3Aspellsoutzero%3Aincludesactualbytecount%3Alocale%3A%29.json'
content_hash: 'sha256:d1b34033f8d86ff2'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Measurement](../../../measurement.md) · [AttributedStyle](../../attributedstyle.md) · [ByteCount](../bytecount.md)

# init(style:allowedUnits:spellsOutZero:includesActualByteCount:locale:)

<sub>Initializer</sub>

Initializes an attributed byte count format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(style: Measurement<UnitType>.AttributedStyle.ByteCount.Style, allowedUnits: Measurement<UnitType>.AttributedStyle.ByteCount.Units, spellsOutZero: Bool, includesActualByteCount: Bool, locale: Locale)
```

## Parameters

- `style` — The style of byte count to express, such as memory or file system storage.

- `allowedUnits` — The units the format style can use to express the byte count.

- `spellsOutZero` — A Boolean value that indicates whether the format style should spell out zero-byte values as text, like `Zero kB`.

- `includesActualByteCount` — A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units. For example, `1 kB (1,024 bytes)`.

- `locale` — The locale to use to format the numeric part of the byte count.
