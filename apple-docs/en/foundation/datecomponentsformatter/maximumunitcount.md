---
title: maximumUnitCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponentsformatter/maximumunitcount
source_url: 'https://developer.apple.com/documentation/foundation/datecomponentsformatter/maximumunitcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponentsformatter/maximumunitcount.json'
content_hash: 'sha256:09f4883a084dc3ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponentsFormatter](../datecomponentsformatter.md)

# maximumUnitCount

<sub>Instance Property</sub>

The maximum number of time units to include in the output string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var maximumUnitCount: Int { get set }
```

## Discussion

Use this property to limit the number of units displayed in the resulting string. For example, with this property set to 2, instead of “1h 10m, 30s”, the resulting string would be “1h 10m”. Use this property when you are constrained for space or want to round up values to the nearest large unit.

The default value of this property is `0`, which does not cause the elimination of any units.

## See Also

### Configuring the Formatter Options

- [allowedUnits](allowedunits.md) — The bitmask of calendrical units such as day and month to include in the output string.
- [allowsFractionalUnits](allowsfractionalunits.md) — A Boolean indicating whether non-integer units may be used for values.
- [calendar](calendar.md) — The default calendar to use when formatting date components.
- [collapsesLargestUnit](collapseslargestunit.md) — A Boolean value indicating whether to collapse the largest unit into smaller units when a certain threshold is met.
- [includesApproximationPhrase](includesapproximationphrase.md) — A Boolean value indicating whether the resulting phrase reflects an inexact time value.
- [includesTimeRemainingPhrase](includestimeremainingphrase.md) — A Boolean value indicating whether output strings reflect the amount of time remaining.
- [unitsStyle](unitsstyle-swift.property.md) — The formatting style for unit names.
- [zeroFormattingBehavior](zeroformattingbehavior-swift.property.md) — The formatting style for units whose value is 0.
