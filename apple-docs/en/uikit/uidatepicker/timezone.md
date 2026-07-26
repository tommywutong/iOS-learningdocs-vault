---
title: timeZone
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatepicker/timezone
source_url: 'https://developer.apple.com/documentation/uikit/uidatepicker/timezone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatepicker/timezone.json'
content_hash: 'sha256:8aa499f71b8dd759'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDatePicker](../uidatepicker.md)

# timeZone

<sub>Instance Property</sub>

The time zone reflected in the date displayed by the date picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var timeZone: TimeZone? { get set }
```

## Discussion

The default value is `nil`, which tells the date picker to use the current time zone as returned by [local](../../foundation/nstimezone/local.md) ([NSTimeZone](../../foundation/nstimezone.md)) or the time zone used by the date picker’s calendar.

## See Also

### Managing the date and calendar

- [calendar](calendar.md) — The calendar to use for the date picker.
- [date](date.md) — The date displayed by the date picker.
- [locale](locale.md) — The locale used by the date picker.
- [- setDate:animated:](<setdate(__animated_).md>) — Sets the date to display in the date picker, with an option to animate the setting.
