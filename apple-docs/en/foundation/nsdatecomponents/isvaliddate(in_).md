---
title: 'isValidDate(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdatecomponents/isvaliddate(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdatecomponents/isvaliddate(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdatecomponents/isvaliddate%28in%3A%29.json'
content_hash: 'sha256:d5d2030c05d1444d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDateComponents](../nsdatecomponents.md)

# isValidDate(in:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the current combination of properties represents a date which exists in the specified calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isValidDate(in calendar: Calendar) -> Bool
```

## Parameters

- `calendar` — The calendar for which to use in the calculation.

## Return Value

[true](../../swift/true.md) if the date corresponding to the receiver’s values is valid and exists in the given calendar, otherwise [false](../../swift/false.md).

## Discussion

If the [timeZone](timezone.md) property is set on the receiver, the time zone property value is used.

This property should not be used for [NSDateComponents](../nsdatecomponents.md) objects that represent relative quantities of calendar components. To find the the next or previous date that matches a particular set of date components, use the [NSCalendar](../nscalendar.md) instance method [- nextDateAfterDate:matchingUnit:value:options:](<../nscalendar/nextdate(after_matching_value_options_).md>) instead.

## See Also

### Validating a Date

- [validDate](isvaliddate.md) — A Boolean value that indicates whether the current combination of properties represents a date which exists in the current calendar.
- [date](date.md) — The date calculated from the current components using the stored calendar.
- [Undefined Components](../1430344-undefined-components.md) — Constants that denote that the value of a date component is undefined.
