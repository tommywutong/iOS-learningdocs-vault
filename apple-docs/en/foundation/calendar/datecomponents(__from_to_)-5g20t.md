---
title: 'dateComponents(_:from:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/datecomponents(_:from:to:)-5g20t'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/datecomponents(_:from:to:)-5g20t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/datecomponents%28_%3Afrom%3Ato%3A%29-5g20t.json'
content_hash: 'sha256:4789699f8b70f9ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# dateComponents(_:from:to:)

<sub>Instance Method</sub>

Returns the difference between two dates specified as `DateComponents`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dateComponents(_ components: Set<Calendar.Component>, from start: DateComponents, to end: DateComponents) -> DateComponents
```

## Parameters

- `components` — Which components to compare.

- `start` — The starting date components.

- `end` — The ending date components.

## Return Value

The result of calculating the difference from start to end.

## Discussion

For components which are not specified in each `DateComponents`, but required to specify an absolute date, the base value of the component is assumed.  For example, for an `DateComponents` with just a `year` and a `month` specified, a `day` of 1, and an `hour`, `minute`, `second`, and `nanosecond` of 0 are assumed. Calendrical calculations with unspecified `year` or `year` value prior to the start of a calendar are not advised. For each `DateComponents`, if its `timeZone` property is set, that time zone is used for it. If the `calendar` property is set, that is used rather than the receiving calendar, and if both the `calendar` and `timeZone` are set, the `timeZone` property value overrides the time zone of the `calendar` property.

## See Also

### Extracting Components

- [date(_:matchesComponents:)](<date(__matchescomponents_).md>) — Determines if the date has all of the specified date components.
- [component(_:from:)](<component(__from_).md>) — Returns the value for one component of a date.
- [dateComponents(_:from:)](<datecomponents(__from_).md>) — Returns all the date components of a date, using the calendar time zone.
- [dateComponents(_:from:to:)](<datecomponents(__from_to_)-2kcg.md>) — Returns the difference between two dates.
- [dateComponents(in:from:)](<datecomponents(in_from_).md>) — Returns all the date components of a date, as if in a given time zone (instead of the `Calendar` time zone).
- [Component](component.md) — An enumeration for the various components of a calendar date.
