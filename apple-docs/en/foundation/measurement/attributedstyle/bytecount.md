---
title: Measurement.AttributedStyle.ByteCount
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurement/attributedstyle/bytecount
source_url: 'https://developer.apple.com/documentation/foundation/measurement/attributedstyle/bytecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/attributedstyle/bytecount.json'
content_hash: 'sha256:6ea55887ba11d4f2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Measurement](../../measurement.md) · [AttributedStyle](../attributedstyle.md)

# Measurement.AttributedStyle.ByteCount

<sub>Structure</sub>

A format style that converts byte counts into attributed strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ByteCount
```

## Overview

Use the [attributed](../formatstyle/bytecount/attributed.md) modifier on a [ByteCount](../formatstyle/bytecount.md) instance to create a format style of this type.

The attributed strings that this fomat style creates contain attributes from the [NumberFormatAttributes](../../attributescopes/foundationattributes/numberformatattributes.md) attribute scope. Use these attributes to determine which runs of the attributed string represent different parts of the formatted value.

## Relationships

- **Conforms To**: [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [FormatStyle](../../formatstyle.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating an attributed byte count format style

- [init(style:allowedUnits:spellsOutZero:includesActualByteCount:locale:)](<bytecount/init(style_allowedunits_spellsoutzero_includesactualbytecount_locale_).md>) — Initializes an attributed byte count format style.

### Formatting a byte count

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

## See Also

### Creating attributed strings

- [attributed](../formatstyle/bytecount/attributed.md) — An attributed format style based on the byte count format style.
