---
title: NumberFormatter.PadPosition
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/padposition
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/padposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/padposition.json'
content_hash: 'sha256:260d3912c1f7cfc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# NumberFormatter.PadPosition

<sub>Enumeration</sub>

These constants are used to specify how numbers should be padded. These constants are used by the [paddingPosition](paddingposition.md) property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum PadPosition
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSNumberFormatterPadBeforePrefix](padposition/beforeprefix.md) — Specifies that the padding should occur before the prefix.
- [NSNumberFormatterPadAfterPrefix](padposition/afterprefix.md) — Specifies that the padding should occur after the prefix.
- [NSNumberFormatterPadBeforeSuffix](padposition/beforesuffix.md) — Specifies that the padding should occur before the suffix.
- [NSNumberFormatterPadAfterSuffix](padposition/aftersuffix.md) — Specifies that the padding should occur after the suffix.

### Initializers

- [init(rawValue:)](<padposition/init(rawvalue_).md>)

## See Also

### Constants

- [Style](style.md) — The predefined number format styles used by the [numberStyle](numberstyle.md) property.
- [Behavior](behavior.md) — These constants specify the behavior of a number formatter. These constants are returned by the [+ defaultFormatterBehavior](<defaultformatterbehavior().md>) class method and the [formatterBehavior](formatterbehavior.md) property.
- [RoundingMode](roundingmode-swift.enum.md) — These constants are used to specify how numbers should be rounded. These constants are used by the [roundingMode](roundingmode-swift.property.md) property.
