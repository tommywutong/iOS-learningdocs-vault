---
title: era
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponents/era
source_url: 'https://developer.apple.com/documentation/foundation/datecomponents/era'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponents/era.json'
content_hash: 'sha256:b11e09b051f60f9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponents](../datecomponents.md)

# era

<sub>Instance Property</sub>

An era or count of eras.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var era: Int? { get set }
```

## Discussion

> [!note] Note
> This value is interpreted in the context of the calendar in which it is used.

## See Also

### Accessing Months and Years

- [year](year.md) — A year or count of years.
- [yearForWeekOfYear](yearforweekofyear.md) — The year corresponding to a week-counting week.
- [quarter](quarter.md) — A quarter or count of quarters.
- [month](month.md) — A month or count of months.
- [isLeapMonth](isleapmonth.md) — Set to true if these components represent a leap month.
