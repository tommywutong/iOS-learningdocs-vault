---
title: 'date(_:matchesComponents:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/date(_:matchescomponents:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/date(_:matchescomponents:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/date%28_%3Amatchescomponents%3A%29.json'
content_hash: 'sha256:ecd07b84b41609a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# date(_:matchesComponents:)

<sub>Instance Method</sub>

Determines if the date has all of the specified date components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func date(_ date: Date, matchesComponents components: DateComponents) -> Bool
```

## Return Value

`true` if the date matches all of the components, otherwise `false`.

## Discussion

It may be useful to test the return value of `nextDate(after:matching:matchingPolicy:behavior:direction:)` to find out if the components were obeyed or if the method had to fudge the result value due to missing time (for example, a daylight saving time transition).

## See Also

### Extracting Components

- [component(_:from:)](<component(__from_).md>) — Returns the value for one component of a date.
- [dateComponents(_:from:)](<datecomponents(__from_).md>) — Returns all the date components of a date, using the calendar time zone.
- [dateComponents(_:from:to:)](<datecomponents(__from_to_)-2kcg.md>) — Returns the difference between two dates.
- [dateComponents(_:from:to:)](<datecomponents(__from_to_)-5g20t.md>) — Returns the difference between two dates specified as `DateComponents`.
- [dateComponents(in:from:)](<datecomponents(in_from_).md>) — Returns all the date components of a date, as if in a given time zone (instead of the `Calendar` time zone).
- [Component](component.md) — An enumeration for the various components of a calendar date.
