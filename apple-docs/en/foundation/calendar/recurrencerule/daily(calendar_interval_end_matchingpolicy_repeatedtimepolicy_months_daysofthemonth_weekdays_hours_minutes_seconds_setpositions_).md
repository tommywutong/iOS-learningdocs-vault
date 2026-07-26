---
title: 'daily(calendar:interval:end:matchingPolicy:repeatedTimePolicy:months:daysOfTheMonth:weekdays:hours:minutes:seconds:setPositions:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/recurrencerule/daily(calendar:interval:end:matchingpolicy:repeatedtimepolicy:months:daysofthemonth:weekdays:hours:minutes:seconds:setpositions:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/recurrencerule/daily(calendar:interval:end:matchingpolicy:repeatedtimepolicy:months:daysofthemonth:weekdays:hours:minutes:seconds:setpositions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/recurrencerule/daily%28calendar%3Ainterval%3Aend%3Amatchingpolicy%3Arepeatedtimepolicy%3Amonths%3Adaysofthemonth%3Aweekdays%3Ahours%3Aminutes%3Aseconds%3Asetpositions%3A%29.json'
content_hash: 'sha256:b5a00ac115d70f97'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Calendar](../../calendar.md) · [RecurrenceRule](../recurrencerule.md)

# daily(calendar:interval:end:matchingPolicy:repeatedTimePolicy:months:daysOfTheMonth:weekdays:hours:minutes:seconds:setPositions:)

<sub>Type Method</sub>

A recurrence that repeats every `interval` days

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func daily(calendar: Calendar, interval: Int = 1, end: Calendar.RecurrenceRule.End = .never, matchingPolicy: Calendar.MatchingPolicy = .nextTimePreservingSmallerComponents, repeatedTimePolicy: Calendar.RepeatedTimePolicy = .first, months: [Calendar.RecurrenceRule.Month] = [], daysOfTheMonth: [Int] = [], weekdays: [Calendar.RecurrenceRule.Weekday] = [], hours: [Int] = [], minutes: [Int] = [], seconds: [Int] = [], setPositions: [Int] = []) -> Calendar.RecurrenceRule
```
