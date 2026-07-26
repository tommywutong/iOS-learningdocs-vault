---
title: 'isDateInYesterday(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/isdateinyesterday(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/isdateinyesterday(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/isdateinyesterday%28_%3A%29.json'
content_hash: 'sha256:22dc4b855fae68e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# isDateInYesterday(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the given date is within yesterday.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isDateInYesterday(_ date: Date) -> Bool
```

## Parameters

- `date` — The specified date.

## Return Value

`true` if the given date is within yesterday, as defined by the calendar and calendar’s locale; otherwise, `false`.

## See Also

### Comparing Dates

- [compare(_:to:toGranularity:)](<compare(__to_togranularity_).md>) — Compares two dates down to the specified component.
- [isDate(_:equalTo:toGranularity:)](<isdate(__equalto_togranularity_).md>) — Returns a Boolean value indicating whether two dates are equal down to the specified component.
- [isDate(_:inSameDayAs:)](<isdate(__insamedayas_).md>) — Returns a Boolean value indicating whether a date is within the same day as another date.
- [isDateInToday(_:)](<isdateintoday(__).md>) — Returns a Boolean value indicating whether the given date is within today.
- [isDateInTomorrow(_:)](<isdateintomorrow(__).md>) — Returns a Boolean value indicating whether the given date is within tomorrow.
- [isDateInWeekend(_:)](<isdateinweekend(__).md>) — Returns a Boolean value indicating whether the given date is within a weekend period.
