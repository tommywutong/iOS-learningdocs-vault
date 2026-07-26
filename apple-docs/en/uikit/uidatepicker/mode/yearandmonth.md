---
title: UIDatePicker.Mode.yearAndMonth
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatepicker/mode/yearandmonth
source_url: 'https://developer.apple.com/documentation/uikit/uidatepicker/mode/yearandmonth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatepicker/mode/yearandmonth.json'
content_hash: 'sha256:c3460c3bcdfa10da'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIDatePicker](../../uidatepicker.md) · [Mode](../mode.md)

# UIDatePicker.Mode.yearAndMonth

<sub>Case</sub>

A mode that displays the date in months and years.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case yearAndMonth
```

## Discussion

The exact order of these items depends on the locale setting. An example of this mode is “November | 2007”.

> [!important] Important
> You can only use this mode with the date picker style [UIDatePickerStyleWheels](../../uidatepickerstyle/wheels.md), and can’t use it on Mac Catalyst with the [UIUserInterfaceIdiomMac](../../uiuserinterfaceidiom/mac.md) user interface idiom; otherwise, [UIDatePicker](../../uidatepicker.md) throws an exception.

## See Also

### Constants

- [UIDatePickerModeTime](time.md) — A mode that displays the date in hours, minutes, and (optionally) an AM/PM designation. The exact items shown and their order depend upon the locale set. An example of this mode is “6 | 53 | PM”.
- [UIDatePickerModeDate](date.md) — A mode that displays the date in months, days of the month, and years. The exact order of these items depends on the locale setting. An example of this mode is “November | 15 | 2007 “.
- [UIDatePickerModeDateAndTime](dateandtime.md) — A mode that displays the date as unified day of the week, month, and day of the month values, plus hours, minutes, and (optionally) an AM/PM designation. The exact order and format of these items depends on the locale set. An example of this mode is “Wed Nov 15 | 6 | 53 | PM”.
- [UIDatePickerModeCountDownTimer](countdowntimer.md) — A mode that displays hour and minute values, for example, “1 | 53”. The application must set a timer to fire at the proper interval and set the date picker as the seconds tick down.
