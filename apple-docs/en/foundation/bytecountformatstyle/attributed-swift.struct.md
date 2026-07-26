---
title: ByteCountFormatStyle.Attributed
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/bytecountformatstyle/attributed-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatstyle/attributed-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatstyle/attributed-swift.struct.json'
content_hash: 'sha256:7fdc0b8322fed82c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatStyle](../bytecountformatstyle.md)

# ByteCountFormatStyle.Attributed

<sub>Structure</sub>

A format style that converts byte counts into attributed strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Attributed
```

## Overview

Use the [attributed](attributed-swift.property.md) modifier on a [ByteCountFormatStyle](../bytecountformatstyle.md) to create a format style of this type.

The attributed strings that this fomat style creates contain attributes from the [NumberFormatAttributes](../attributescopes/foundationattributes/numberformatattributes.md) attribute scope. Use these attributes to determine which runs of the attributed string represent different parts of the formatted value.

## Relationships

- **Conforms To**: [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [FormatStyle](../formatstyle.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Formatting a byte count

- [format(_:)](<attributed-swift.struct/format(__).md>) — Formats a numeric byte count, using this style.

### Customizing style behavior

- [style](attributed-swift.struct/style.md) — The semantic style the format style uses to represent a byte count value.
- [Style](style-swift.enum.md) — The semantic style to use when formatting a byte count value.

### Accessing style properties

- [allowedUnits](attributed-swift.struct/allowedunits.md) — The units the format style can use to express the byte count.
- [spellsOutZero](attributed-swift.struct/spellsoutzero.md) — A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [includesActualByteCount](attributed-swift.struct/includesactualbytecount.md) — A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.
- [locale](attributed-swift.struct/locale.md) — The locale to use to format the numeric part of the byte count.

### Modifying style locale

- [locale(_:)](<attributed-swift.struct/locale(__).md>) — Modifies the format style to use the specified locale.

## See Also

### Creating attributed strings

- [attributed](attributed-swift.property.md) — An attributed format style based on the byte count format style.
