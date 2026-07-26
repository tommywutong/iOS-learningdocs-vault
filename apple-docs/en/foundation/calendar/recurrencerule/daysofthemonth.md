---
title: daysOfTheMonth
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/recurrencerule/daysofthemonth
source_url: 'https://developer.apple.com/documentation/foundation/calendar/recurrencerule/daysofthemonth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/recurrencerule/daysofthemonth.json'
content_hash: 'sha256:aa5fad0db755267b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Calendar](../../calendar.md) · [RecurrenceRule](../recurrencerule.md)

# daysOfTheMonth

<sub>Instance Property</sub>

On which days in the month the event should occur

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var daysOfTheMonth: [Int]
```

## Discussion

- 1 signifies the first day of the month.
- Negative values point to a day counted backwards from the last day of the month This field is unused when `frequency` is `.weekly`.
