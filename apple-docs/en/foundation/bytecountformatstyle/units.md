---
title: ByteCountFormatStyle.Units
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/bytecountformatstyle/units
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatstyle/units'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatstyle/units.json'
content_hash: 'sha256:9415e0090a698ad2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatStyle](../bytecountformatstyle.md)

# ByteCountFormatStyle.Units

<sub>Structure</sub>

The units to use when formatting a byte count, such as kilobytes or gigabytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Units
```

## Relationships

- **Conforms To**: [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [Hashable](../../swift/hashable.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Units

- [default](units/default.md) — A value that indicates a format style should use the most appropriate units to express a byte count.
- [all](units/all.md) — A value that allows the use of all byte-count units.
- [bytes](units/bytes.md) — A value that indicates a format style should express byte counts in individual bytes.
- [kb](units/kb.md) — The kilobytes unit.
- [mb](units/mb.md) — The megabytes unit.
- [gb](units/gb.md) — The gigabytes unit.
- [tb](units/tb.md) — The terabytes unit.
- [pb](units/pb.md) — The petabytes unit.
- [eb](units/eb.md) — The exabytes unit.
- [zb](units/zb.md) — The zettabytes unit.
- [ybOrHigher](units/yborhigher.md) — A value that indicates a format style should express byte counts as yottabytes or higher.

## See Also

### Creating a byte count style

- [init(style:allowedUnits:spellsOutZero:includesActualByteCount:locale:)](<init(style_allowedunits_spellsoutzero_includesactualbytecount_locale_).md>) — Initializes a byte count format style.
