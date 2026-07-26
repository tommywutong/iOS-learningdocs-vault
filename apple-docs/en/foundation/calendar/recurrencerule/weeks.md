---
title: weeks
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/recurrencerule/weeks
source_url: 'https://developer.apple.com/documentation/foundation/calendar/recurrencerule/weeks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/recurrencerule/weeks.json'
content_hash: 'sha256:4de558bbe3052a38'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Calendar](../../calendar.md) · [RecurrenceRule](../recurrencerule.md)

# weeks

<sub>Instance Property</sub>

On which weeks of the year the event should occur.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var weeks: [Int]
```

## Discussion

- 1 is the first week of the year. `calendar.minimumDaysInFirstWeek` defines which week is considered first.
- Negative values refer to weeks if counting backwards from the last week of the year. -1 is the last week of the year. This field is unused when `frequency` is other than `.yearly`.
