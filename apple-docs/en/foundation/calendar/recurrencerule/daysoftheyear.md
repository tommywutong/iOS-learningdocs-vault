---
title: daysOfTheYear
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/recurrencerule/daysoftheyear
source_url: 'https://developer.apple.com/documentation/foundation/calendar/recurrencerule/daysoftheyear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/recurrencerule/daysoftheyear.json'
content_hash: 'sha256:75305fa8db93de83'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Calendar](../../calendar.md) · [RecurrenceRule](../recurrencerule.md)

# daysOfTheYear

<sub>Instance Property</sub>

On which days of the year the event may occur.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var daysOfTheYear: [Int]
```

## Discussion

- 1 signifies the first day of the year.
- Negative values point to a day counted backwards from the last day of the year This field is unused when `frequency` is any of `.daily`, `.weekly`, or `.monthly`.
