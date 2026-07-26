---
title: 'dateComponents(in:from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/datecomponents(in:from:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/datecomponents(in:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/datecomponents%28in%3Afrom%3A%29.json'
content_hash: 'sha256:5cbcede761634ba5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# dateComponents(in:from:)

<sub>Instance Method</sub>

Returns all the date components of a date, as if in a given time zone (instead of the `Calendar` time zone).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dateComponents(in timeZone: TimeZone, from date: Date) -> DateComponents
```

## Parameters

- `timeZone` — The `TimeZone` to use.

- `date` — The `Date` to use.

## Return Value

All components, calculated using the `Calendar` and `TimeZone`.

## Discussion

The time zone overrides the time zone of the `Calendar` for the purposes of this calculation.

> [!note] Note
> If you want “date information in a given time zone” in order to display it, you should use `DateFormatter` to format the date.

## See Also

### Extracting Components

- [date(_:matchesComponents:)](<date(__matchescomponents_).md>) — Determines if the date has all of the specified date components.
- [component(_:from:)](<component(__from_).md>) — Returns the value for one component of a date.
- [dateComponents(_:from:)](<datecomponents(__from_).md>) — Returns all the date components of a date, using the calendar time zone.
- [dateComponents(_:from:to:)](<datecomponents(__from_to_)-2kcg.md>) — Returns the difference between two dates.
- [dateComponents(_:from:to:)](<datecomponents(__from_to_)-5g20t.md>) — Returns the difference between two dates specified as `DateComponents`.
- [Component](component.md) — An enumeration for the various components of a calendar date.
