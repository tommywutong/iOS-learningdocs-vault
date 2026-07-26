---
title: zeroFormattingBehavior
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponentsformatter/zeroformattingbehavior-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/datecomponentsformatter/zeroformattingbehavior-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponentsformatter/zeroformattingbehavior-swift.property.json'
content_hash: 'sha256:d132068ddaa295fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponentsFormatter](../datecomponentsformatter.md)

# zeroFormattingBehavior

<sub>Instance Property</sub>

The formatting style for units whose value is 0.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var zeroFormattingBehavior: DateComponentsFormatter.ZeroFormattingBehavior { get set }
```

## Discussion

When the value for a particular unit is 0, the zero formatting behavior determines whether that value is retained or omitted from any resulting strings. For example, when the formatting behavior is [NSDateComponentsFormatterZeroFormattingBehaviorDropTrailing](zeroformattingbehavior-swift.struct/droptrailing.md), the value of one hour, ten minutes, and zero seconds would omit the mention of seconds.

The default value of this property is [NSDateComponentsFormatterZeroFormattingBehaviorDefault](zeroformattingbehavior-swift.struct/default.md).

## See Also

### Configuring the Formatter Options

- [allowedUnits](allowedunits.md) — The bitmask of calendrical units such as day and month to include in the output string.
- [allowsFractionalUnits](allowsfractionalunits.md) — A Boolean indicating whether non-integer units may be used for values.
- [calendar](calendar.md) — The default calendar to use when formatting date components.
- [collapsesLargestUnit](collapseslargestunit.md) — A Boolean value indicating whether to collapse the largest unit into smaller units when a certain threshold is met.
- [includesApproximationPhrase](includesapproximationphrase.md) — A Boolean value indicating whether the resulting phrase reflects an inexact time value.
- [includesTimeRemainingPhrase](includestimeremainingphrase.md) — A Boolean value indicating whether output strings reflect the amount of time remaining.
- [maximumUnitCount](maximumunitcount.md) — The maximum number of time units to include in the output string.
- [unitsStyle](unitsstyle-swift.property.md) — The formatting style for unit names.
