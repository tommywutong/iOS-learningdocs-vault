---
title: 'Calendar.RecurrenceRule.Weekday.nth(_:_:)'
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/recurrencerule/weekday/nth(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/recurrencerule/weekday/nth(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/recurrencerule/weekday/nth%28_%3A_%3A%29.json'
content_hash: 'sha256:77122287d583e3da'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Calendar](../../../calendar.md) · [RecurrenceRule](../../recurrencerule.md) · [Weekday](../weekday.md)

# Calendar.RecurrenceRule.Weekday.nth(_:_:)

<sub>Case</sub>

Repeat on the n-th instance of the specified weekday in a month, if the recurrence has a monthly frequency. If the recurrence has a yearly frequency, repeat on the n-th week of the year.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case nth(Int, Locale.Weekday)
```

## Discussion

If n is negative, repeat on the n-to-last of the given weekday.
