---
title: NumberFormatStyleConfiguration.SignDisplayStrategy
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatstyleconfiguration/signdisplaystrategy
source_url: 'https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/signdisplaystrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatstyleconfiguration/signdisplaystrategy.json'
content_hash: 'sha256:c21afd3d5e3422ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatStyleConfiguration](../numberformatstyleconfiguration.md)

# NumberFormatStyleConfiguration.SignDisplayStrategy

<sub>Structure</sub>

A structure that an integer format style uses to configure a sign display strategy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SignDisplayStrategy
```

## Relationships

- **Conforms To**: [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Sign display strategies

- [automatic](signdisplaystrategy/automatic.md) — A strategy to automatically configure locale-appropriate sign display behavior.
- [always(includingZero:)](<signdisplaystrategy/always(includingzero_).md>) — A strategy to always display sign symbols.
- [never](signdisplaystrategy/never.md) — A strategy to never display sign symbols.

## See Also

### Specifying Configuration

- [DecimalSeparatorDisplayStrategy](decimalseparatordisplaystrategy.md) — A structure that an integer format style uses to configure a decimal separator display strategy.
- [Grouping](grouping.md) — A structure that an integer format style uses to configure grouping.
- [Precision](precision.md) — A structure that an integer format style uses to configure precision.
- [RoundingRule](roundingrule.md) — The type used for rounding rule values.
- [Notation](notation.md) — A structure that an integer format style uses to configure notation.
