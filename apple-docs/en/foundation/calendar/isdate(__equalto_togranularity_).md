---
title: 'isDate(_:equalTo:toGranularity:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/isdate(_:equalto:togranularity:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/isdate(_:equalto:togranularity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/isdate%28_%3Aequalto%3Atogranularity%3A%29.json'
content_hash: 'sha256:0d2c7ade6724a2f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# isDate(_:equalTo:toGranularity:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether two dates are equal down to the specified component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isDate(_ date1: Date, equalTo date2: Date, toGranularity component: Calendar.Component) -> Bool
```

## Parameters

- `date1` — A date to compare.

- `date2` — A date to compare.

- `component` — A granularity to compare. For example, pass `.hour` to check if two dates are in the same hour.

## Return Value

`true` if the two dates are equal in the given component and all larger components; otherwise, `false`.

## See Also

### Comparing Dates

- [compare(_:to:toGranularity:)](<compare(__to_togranularity_).md>) — Compares two dates down to the specified component.
- [isDate(_:inSameDayAs:)](<isdate(__insamedayas_).md>) — Returns a Boolean value indicating whether a date is within the same day as another date.
- [isDateInToday(_:)](<isdateintoday(__).md>) — Returns a Boolean value indicating whether the given date is within today.
- [isDateInTomorrow(_:)](<isdateintomorrow(__).md>) — Returns a Boolean value indicating whether the given date is within tomorrow.
- [isDateInYesterday(_:)](<isdateinyesterday(__).md>) — Returns a Boolean value indicating whether the given date is within yesterday.
- [isDateInWeekend(_:)](<isdateinweekend(__).md>) — Returns a Boolean value indicating whether the given date is within a weekend period.
