---
title: collapsesLargestUnit
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponentsformatter/collapseslargestunit
source_url: 'https://developer.apple.com/documentation/foundation/datecomponentsformatter/collapseslargestunit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponentsformatter/collapseslargestunit.json'
content_hash: 'sha256:05d30c40d0325a15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponentsFormatter](../datecomponentsformatter.md)

# collapsesLargestUnit

<sub>Instance Property</sub>

A Boolean value indicating whether to collapse the largest unit into smaller units when a certain threshold is met.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var collapsesLargestUnit: Bool { get set }
```

## Discussion

An example of when this property might apply is when expressing 63 seconds worth of time. When this property is set to [true](../../swift/true.md), the formatted value would be “63s”. When the value of this property is [false](../../swift/false.md), the formatted value would be “1m 3s”.

The default value of this property is [false](../../swift/false.md).

## See Also

### Configuring the Formatter Options

- [allowedUnits](allowedunits.md) — The bitmask of calendrical units such as day and month to include in the output string.
- [allowsFractionalUnits](allowsfractionalunits.md) — A Boolean indicating whether non-integer units may be used for values.
- [calendar](calendar.md) — The default calendar to use when formatting date components.
- [includesApproximationPhrase](includesapproximationphrase.md) — A Boolean value indicating whether the resulting phrase reflects an inexact time value.
- [includesTimeRemainingPhrase](includestimeremainingphrase.md) — A Boolean value indicating whether output strings reflect the amount of time remaining.
- [maximumUnitCount](maximumunitcount.md) — The maximum number of time units to include in the output string.
- [unitsStyle](unitsstyle-swift.property.md) — The formatting style for unit names.
- [zeroFormattingBehavior](zeroformattingbehavior-swift.property.md) — The formatting style for units whose value is 0.
