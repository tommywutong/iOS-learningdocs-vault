---
title: date
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatepicker/date
source_url: 'https://developer.apple.com/documentation/uikit/uidatepicker/date'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatepicker/date.json'
content_hash: 'sha256:d31f2c7b7ec9d0c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDatePicker](../uidatepicker.md)

# date

<sub>Instance Property</sub>

The date displayed by the date picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var date: Date { get set }
```

## Discussion

Use this property to get and set the currently selected date. The default value of this property is the date when the [UIDatePicker](../uidatepicker.md) object is created. Setting this property animates the date picker by spinning the wheels to the new date and time; if you don’t want any animation to occur when you set the date, use the [- setDate:animated:](<setdate(__animated_).md>) method, passing [false](../../swift/false.md) for the `animated` parameter. This behavior of this property is undefined when the mode is set to [UIDatePickerModeCountDownTimer](mode/countdowntimer.md); refer instead to the [countDownDuration](countdownduration.md) property.

## See Also

### Managing the date and calendar

- [calendar](calendar.md) — The calendar to use for the date picker.
- [locale](locale.md) — The locale used by the date picker.
- [- setDate:animated:](<setdate(__animated_).md>) — Sets the date to display in the date picker, with an option to animate the setting.
- [timeZone](timezone.md) — The time zone reflected in the date displayed by the date picker.
