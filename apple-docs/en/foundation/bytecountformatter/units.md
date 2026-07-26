---
title: ByteCountFormatter.Units
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bytecountformatter/units
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatter/units'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatter/units.json'
content_hash: 'sha256:227fec26e4f2f789'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatter](../bytecountformatter.md)

# ByteCountFormatter.Units

<sub>Structure</sub>

Specifies the units appropriate for the formatter to display. Specifying any units explicitly causes just those units to be used in showing the number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Units
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSByteCountFormatterUseBytes](units/usebytes.md) — Displays bytes in the formatter content.
- [NSByteCountFormatterUseKB](units/usekb.md) — Displays kilobytes in the formatter content.
- [NSByteCountFormatterUseMB](units/usemb.md) — Displays megabytes in the formatter content.
- [NSByteCountFormatterUseGB](units/usegb.md) — Displays gigabytes in the formatter content.
- [NSByteCountFormatterUseTB](units/usetb.md) — Displays terabytes in the formatter content.
- [NSByteCountFormatterUsePB](units/usepb.md) — Displays petabyte in the formatter content.
- [NSByteCountFormatterUseEB](units/useeb.md) — Displays exabytes in the formatter content.
- [NSByteCountFormatterUseZB](units/usezb.md) — Displays zettabytes in the formatter content.
- [NSByteCountFormatterUseYBOrHigher](units/useyborhigher.md) — Displays yottabytes in the formatter content.
- [NSByteCountFormatterUseAll](units/useall.md) — Can use any unit in the formatter content.

### Initializers

- [init(rawValue:)](<units/init(rawvalue_).md>)

## See Also

### Constants

- [CountStyle](countstyle-swift.enum.md) — Specifies display of file or storage byte counts. The display style is platform specific.
