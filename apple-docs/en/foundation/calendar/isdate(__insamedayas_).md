---
title: 'isDate(_:inSameDayAs:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/isdate(_:insamedayas:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/isdate(_:insamedayas:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/isdate%28_%3Ainsamedayas%3A%29.json'
content_hash: 'sha256:1b5cbd1351da47c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# isDate(_:inSameDayAs:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether a date is within the same day as another date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isDate(_ date1: Date, inSameDayAs date2: Date) -> Bool
```

## Parameters

- `date1` — A date to check for containment.

- `date2` — A date to check for containment.

## Return Value

`true` if `date1` and `date2` are in the same day, as defined by the calendar and calendar’s locale; otherwise, `false`.

## See Also

### Comparing Dates

- [compare(_:to:toGranularity:)](<compare(__to_togranularity_).md>) — Compares two dates down to the specified component.
- [isDate(_:equalTo:toGranularity:)](<isdate(__equalto_togranularity_).md>) — Returns a Boolean value indicating whether two dates are equal down to the specified component.
- [isDateInToday(_:)](<isdateintoday(__).md>) — Returns a Boolean value indicating whether the given date is within today.
- [isDateInTomorrow(_:)](<isdateintomorrow(__).md>) — Returns a Boolean value indicating whether the given date is within tomorrow.
- [isDateInYesterday(_:)](<isdateinyesterday(__).md>) — Returns a Boolean value indicating whether the given date is within yesterday.
- [isDateInWeekend(_:)](<isdateinweekend(__).md>) — Returns a Boolean value indicating whether the given date is within a weekend period.
