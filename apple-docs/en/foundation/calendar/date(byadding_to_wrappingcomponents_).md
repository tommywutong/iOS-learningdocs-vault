---
title: 'date(byAdding:to:wrappingComponents:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/date(byadding:to:wrappingcomponents:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/date(byadding:to:wrappingcomponents:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/date%28byadding%3Ato%3Awrappingcomponents%3A%29.json'
content_hash: 'sha256:78c4b5b365ceb5b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# date(byAdding:to:wrappingComponents:)

<sub>Instance Method</sub>

Returns a new `Date` representing the date calculated by adding components to a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func date(byAdding components: DateComponents, to date: Date, wrappingComponents: Bool = false) -> Date?
```

## Parameters

- `components` — A set of values to add to the date.

- `date` — The starting date.

- `wrappingComponents` — If `true`, the component should be incremented and wrap around to zero/one on overflow, and should not cause higher components to be incremented. The default value is `false`.

## Return Value

A new date, or nil if a date could not be calculated with the given input.

## See Also

### Calculating Dates from Components

- [date(from:)](<date(from_).md>) — Returns a date created from the specified components.
- [date(byAdding:value:to:wrappingComponents:)](<date(byadding_value_to_wrappingcomponents_).md>) — Returns a new `Date` representing the date calculated by adding an amount of a specific component to a given date.
- [date(bySetting:value:of:)](<date(bysetting_value_of_).md>) — Returns a new `Date` representing the date calculated by setting a specific component to a given time, and trying to keep lower components the same.  If the component already has that value, this may result in a date which is the same as the given date.
- [date(bySettingHour:minute:second:of:matchingPolicy:repeatedTimePolicy:direction:)](<date(bysettinghour_minute_second_of_matchingpolicy_repeatedtimepolicy_direction_).md>) — Returns a new `Date` representing the date calculated by setting hour, minute, and second to a given time on a specified `Date`.
