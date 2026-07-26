---
title: includesApproximationPhrase
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponentsformatter/includesapproximationphrase
source_url: 'https://developer.apple.com/documentation/foundation/datecomponentsformatter/includesapproximationphrase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponentsformatter/includesapproximationphrase.json'
content_hash: 'sha256:4cf4c14d225ee976'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponentsFormatter](../datecomponentsformatter.md)

# includesApproximationPhrase

<sub>Instance Property</sub>

A Boolean value indicating whether the resulting phrase reflects an inexact time value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var includesApproximationPhrase: Bool { get set }
```

## Discussion

Setting the value of this property to [true](../../swift/true.md) adds phrasing to output strings to reflect that the given time value is approximate and not exact. Using this property yields more correct phrasing than simply prepending the string “About” to an output string.

The default value of this property is [false](../../swift/false.md).

## See Also

### Configuring the Formatter Options

- [allowedUnits](allowedunits.md) — The bitmask of calendrical units such as day and month to include in the output string.
- [allowsFractionalUnits](allowsfractionalunits.md) — A Boolean indicating whether non-integer units may be used for values.
- [calendar](calendar.md) — The default calendar to use when formatting date components.
- [collapsesLargestUnit](collapseslargestunit.md) — A Boolean value indicating whether to collapse the largest unit into smaller units when a certain threshold is met.
- [includesTimeRemainingPhrase](includestimeremainingphrase.md) — A Boolean value indicating whether output strings reflect the amount of time remaining.
- [maximumUnitCount](maximumunitcount.md) — The maximum number of time units to include in the output string.
- [unitsStyle](unitsstyle-swift.property.md) — The formatting style for unit names.
- [zeroFormattingBehavior](zeroformattingbehavior-swift.property.md) — The formatting style for units whose value is 0.
