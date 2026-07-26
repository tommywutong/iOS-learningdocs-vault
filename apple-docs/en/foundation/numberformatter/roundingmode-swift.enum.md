---
title: NumberFormatter.RoundingMode
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/roundingmode-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/roundingmode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/roundingmode-swift.enum.json'
content_hash: 'sha256:878f9f201b6c5921'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# NumberFormatter.RoundingMode

<sub>Enumeration</sub>

These constants are used to specify how numbers should be rounded. These constants are used by the [roundingMode](roundingmode-swift.property.md) property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum RoundingMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSNumberFormatterRoundCeiling](roundingmode-swift.enum/ceiling.md) — Round towards positive infinity.
- [NSNumberFormatterRoundFloor](roundingmode-swift.enum/floor.md) — Round towards negative infinity.
- [NSNumberFormatterRoundDown](roundingmode-swift.enum/down.md) — Round towards zero.
- [NSNumberFormatterRoundUp](roundingmode-swift.enum/up.md) — Round away from zero.
- [NSNumberFormatterRoundHalfEven](roundingmode-swift.enum/halfeven.md) — Round towards the nearest integer, or towards an even number if equidistant.
- [NSNumberFormatterRoundHalfDown](roundingmode-swift.enum/halfdown.md) — Round towards the nearest integer, or towards zero if equidistant.
- [NSNumberFormatterRoundHalfUp](roundingmode-swift.enum/halfup.md) — Round towards the nearest integer, or away from zero if equidistant.

### Initializers

- [init(rawValue:)](<roundingmode-swift.enum/init(rawvalue_).md>)

## See Also

### Constants

- [Style](style.md) — The predefined number format styles used by the [numberStyle](numberstyle.md) property.
- [Behavior](behavior.md) — These constants specify the behavior of a number formatter. These constants are returned by the [+ defaultFormatterBehavior](<defaultformatterbehavior().md>) class method and the [formatterBehavior](formatterbehavior.md) property.
- [PadPosition](padposition.md) — These constants are used to specify how numbers should be padded. These constants are used by the [paddingPosition](paddingposition.md) property.
