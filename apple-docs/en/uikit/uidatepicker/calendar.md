---
title: calendar
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatepicker/calendar
source_url: 'https://developer.apple.com/documentation/uikit/uidatepicker/calendar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatepicker/calendar.json'
content_hash: 'sha256:8bff2647f316444b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDatePicker](../uidatepicker.md)

# calendar

<sub>Instance Property</sub>

The calendar to use for the date picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var calendar: Calendar! { get set }
```

## Discussion

The default value of this property corresponds to the user’s current calendar as configured in Settings. This is equivalent to the value returned by calling the [NSCalendar](../../foundation/nscalendar.md) class method [current](../../foundation/nscalendar/current.md). Setting this property to `nil` is equivalent to setting it to its default value.

Calendars specify the details of cultural systems used for reckoning time; they identify the beginning, length, and divisions of a year.

## See Also

### Managing the date and calendar

- [date](date.md) — The date displayed by the date picker.
- [locale](locale.md) — The locale used by the date picker.
- [- setDate:animated:](<setdate(__animated_).md>) — Sets the date to display in the date picker, with an option to animate the setting.
- [timeZone](timezone.md) — The time zone reflected in the date displayed by the date picker.
