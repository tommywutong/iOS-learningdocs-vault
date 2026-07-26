---
title: Measurement.FormatStyle.ByteCount
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurement/formatstyle/bytecount
source_url: 'https://developer.apple.com/documentation/foundation/measurement/formatstyle/bytecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/formatstyle/bytecount.json'
content_hash: 'sha256:0b769b7cfc2f83c2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Measurement](../../measurement.md) · [FormatStyle](../formatstyle.md)

# Measurement.FormatStyle.ByteCount

<sub>Structure</sub>

A format style that provides string representations of byte counts, expressed as measurements of information storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ByteCount
```

## Overview

Use this style with a [Measurement](../../measurement.md) whose unit type is [UnitInformationStorage](../../unitinformationstorage.md) to format byte counts according to locale conventions.

The following example creates a measurement of 1,024 bytes, and then formats it as an expression of memory storage, with the default byte count format style:

```swift
let count = Measurement(value: 1024, unit: UnitInformationStorage.bytes)
let formatted = count.formatted(.byteCount(style: .memory)) // "1 kB"
```

You can also customize a byte count format style, and use this to format one or more [Measurement](../../measurement.md) instances. The following example creates a format style to only use kilobyte units, and to spell out the exact byte count of the measurement.

```swift
let count = Measurement(value: 1024, unit: UnitInformationStorage.bytes)
let style = Measurement.FormatStyle.ByteCount(style: .memory,
                                              allowedUnits: .kb,
                                              spellsOutZero: true,
                                              includesActualByteCount: true,
                                              locale: Locale(identifier: "en_US"))
let customFormatted = style.format(count) // "1 kB (1,024 bytes)"
```

## Relationships

- **Conforms To**: [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [FormatStyle](../../formatstyle.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating a byte count style

- [init(style:allowedUnits:spellsOutZero:includesActualByteCount:locale:)](<bytecount/init(style_allowedunits_spellsoutzero_includesactualbytecount_locale_).md>) — Initializes a byte count format style.

### Formatting byte count measurements

- [format(_:)](<bytecount/format(__).md>) — Formats a byte count measurment, using this style.

### Accessing style properties

- [allowedUnits](bytecount/allowedunits.md) — The units the format style can use to express the byte count.
- [Units](bytecount/units.md) — The type the measurement format style uses to represent byte-counting units.
- [spellsOutZero](bytecount/spellsoutzero.md) — A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [includesActualByteCount](bytecount/includesactualbytecount.md) — A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.
- [style](bytecount/style-swift.property.md) — The style of byte count to express, such as memory or file system storage.
- [Style](bytecount/style-swift.typealias.md) — The type used to represent the style of the formatted byte count.
- [locale](bytecount/locale.md) — The locale to use to format the numeric part of the byte count.

### Modifying style locale

- [locale(_:)](<bytecount/locale(__).md>) — Modifies the format style to use the specified locale.

### Creating attributed strings

- [attributed](bytecount/attributed.md) — An attributed format style based on the byte count format style.
- [ByteCount](../attributedstyle/bytecount.md) — A format style that converts byte counts into attributed strings.

## See Also

### Applying byte-count styles

- [byteCount(style:allowedUnits:spellsOutZero:includesActualByteCount:)](<../../formatstyle/bytecount(style_allowedunits_spellsoutzero_includesactualbytecount_)-59ep0.md>) — Returns a format style to format a data storage value.
- [ByteCountFormatStyle](../../bytecountformatstyle.md) — A format style that provides string representations of byte counts.
- [byteCount(style:allowedUnits:spellsOutZero:includesActualByteCount:)](<../../formatstyle/bytecount(style_allowedunits_spellsoutzero_includesactualbytecount_)-ev0u.md>) — Returns a format style to format a data storage value represented with Foundation’s measurement type.
