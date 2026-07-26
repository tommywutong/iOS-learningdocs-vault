---
title: ByteCountFormatStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/bytecountformatstyle
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatstyle.json'
content_hash: 'sha256:37af6001776ad3d2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# ByteCountFormatStyle

<sub>Structure</sub>

A format style that provides string representations of byte counts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ByteCountFormatStyle
```

## Overview

The following example creates an `Int` representing 1,024 bytes, and then formats it as an expression of memory storage, with the default byte count format style.

```swift
let count: Int64 = 1024
let formatted = count.formatted(.byteCount(style: .memory)) // "1 kB"
```

You can also customize a byte count format style, and use this to format one or more [Int64](../swift/int64.md) instances. The following example creates a format style to only use kilobyte units, and to spell out the exact byte count of the measurement.

```swift
let style = ByteCountFormatStyle(style: .memory,                                 
                                 allowedUnits: [.kb],
                                 spellsOutZero: true,
                                 includesActualByteCount: false,
                                 locale: Locale(identifier: "en_US"))
let counts: [Int64] = [0, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
let formatted = counts.map ( {style.format($0) } ) // ["Zero kB", "1 kB", "2 kB", "4 kB", "8 kB", "16 kB", "32 kB", "64 kB"]
```

## Relationships

- **Conforms To**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [FormatStyle](formatstyle.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a byte count style

- [init(style:allowedUnits:spellsOutZero:includesActualByteCount:locale:)](<bytecountformatstyle/init(style_allowedunits_spellsoutzero_includesactualbytecount_locale_).md>) — Initializes a byte count format style.
- [Units](bytecountformatstyle/units.md) — The units to use when formatting a byte count, such as kilobytes or gigabytes.

### Formatting byte count values

- [format(_:)](<bytecountformatstyle/format(__).md>) — Formats a numeric byte count, using this style.

### Customizing style behavior

- [style](bytecountformatstyle/style-swift.property.md) — The semantic style the format style uses to represent a byte count value.
- [Style](bytecountformatstyle/style-swift.enum.md) — The semantic style to use when formatting a byte count value.

### Accessing style properties

- [allowedUnits](bytecountformatstyle/allowedunits.md) — The units the format style can use to express the byte count.
- [Units](bytecountformatstyle/units.md) — The units to use when formatting a byte count, such as kilobytes or gigabytes.
- [spellsOutZero](bytecountformatstyle/spellsoutzero.md) — A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [includesActualByteCount](bytecountformatstyle/includesactualbytecount.md) — A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.
- [locale](bytecountformatstyle/locale.md) — The locale to use to format the numeric part of the byte count.

### Modifying style locale

- [locale(_:)](<bytecountformatstyle/locale(__).md>) — Modifies the format style to use the specified locale.

### Creating attributed strings

- [attributed](bytecountformatstyle/attributed-swift.property.md) — An attributed format style based on the byte count format style.
- [Attributed](bytecountformatstyle/attributed-swift.struct.md) — A format style that converts byte counts into attributed strings.

## See Also

### Applying byte-count styles

- [byteCount(style:allowedUnits:spellsOutZero:includesActualByteCount:)](<formatstyle/bytecount(style_allowedunits_spellsoutzero_includesactualbytecount_)-59ep0.md>) — Returns a format style to format a data storage value.
- [byteCount(style:allowedUnits:spellsOutZero:includesActualByteCount:)](<formatstyle/bytecount(style_allowedunits_spellsoutzero_includesactualbytecount_)-ev0u.md>) — Returns a format style to format a data storage value represented with Foundation’s measurement type.
- [ByteCount](measurement/formatstyle/bytecount.md) — A format style that provides string representations of byte counts, expressed as measurements of information storage.
