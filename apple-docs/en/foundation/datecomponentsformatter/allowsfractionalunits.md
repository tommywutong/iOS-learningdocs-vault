---
title: allowsFractionalUnits
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponentsformatter/allowsfractionalunits
source_url: 'https://developer.apple.com/documentation/foundation/datecomponentsformatter/allowsfractionalunits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponentsformatter/allowsfractionalunits.json'
content_hash: 'sha256:07fc7ecc0db34386'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponentsFormatter](../datecomponentsformatter.md)

# allowsFractionalUnits

<sub>Instance Property</sub>

A Boolean indicating whether non-integer units may be used for values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowsFractionalUnits: Bool { get set }
```

## Discussion

Fractional units may be used when a value cannot be exactly represented using the available units. For example, if minutes are not allowed, the value “1h 30m” could be formatted as “1.5h”.

The default value of this property is [false](../../swift/false.md).

## See Also

### Configuring the Formatter Options

- [allowedUnits](allowedunits.md) — The bitmask of calendrical units such as day and month to include in the output string.
- [calendar](calendar.md) — The default calendar to use when formatting date components.
- [collapsesLargestUnit](collapseslargestunit.md) — A Boolean value indicating whether to collapse the largest unit into smaller units when a certain threshold is met.
- [includesApproximationPhrase](includesapproximationphrase.md) — A Boolean value indicating whether the resulting phrase reflects an inexact time value.
- [includesTimeRemainingPhrase](includestimeremainingphrase.md) — A Boolean value indicating whether output strings reflect the amount of time remaining.
- [maximumUnitCount](maximumunitcount.md) — The maximum number of time units to include in the output string.
- [unitsStyle](unitsstyle-swift.property.md) — The formatting style for unit names.
- [zeroFormattingBehavior](zeroformattingbehavior-swift.property.md) — The formatting style for units whose value is 0.
