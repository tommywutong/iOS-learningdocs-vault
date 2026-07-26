---
title: unitsStyle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponentsformatter/unitsstyle-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/datecomponentsformatter/unitsstyle-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponentsformatter/unitsstyle-swift.property.json'
content_hash: 'sha256:790bcd39e94609ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponentsFormatter](../datecomponentsformatter.md)

# unitsStyle

<sub>Instance Property</sub>

The formatting style for unit names.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var unitsStyle: DateComponentsFormatter.UnitsStyle { get set }
```

## Discussion

Configures the strings to use (if any) for unit names such as days, hours, minutes, and seconds. Use this property to specify whether you want abbreviated or shortened versions of unit names—for example, `hrs` instead of `hours`.

The default value of this property is [NSDateComponentsFormatterUnitsStylePositional](unitsstyle-swift.enum/positional.md).

## See Also

### Configuring the Formatter Options

- [allowedUnits](allowedunits.md) — The bitmask of calendrical units such as day and month to include in the output string.
- [allowsFractionalUnits](allowsfractionalunits.md) — A Boolean indicating whether non-integer units may be used for values.
- [calendar](calendar.md) — The default calendar to use when formatting date components.
- [collapsesLargestUnit](collapseslargestunit.md) — A Boolean value indicating whether to collapse the largest unit into smaller units when a certain threshold is met.
- [includesApproximationPhrase](includesapproximationphrase.md) — A Boolean value indicating whether the resulting phrase reflects an inexact time value.
- [includesTimeRemainingPhrase](includestimeremainingphrase.md) — A Boolean value indicating whether output strings reflect the amount of time remaining.
- [maximumUnitCount](maximumunitcount.md) — The maximum number of time units to include in the output string.
- [zeroFormattingBehavior](zeroformattingbehavior-swift.property.md) — The formatting style for units whose value is 0.
