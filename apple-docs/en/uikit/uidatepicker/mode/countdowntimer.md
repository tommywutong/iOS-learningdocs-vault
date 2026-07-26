---
title: UIDatePicker.Mode.countDownTimer
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatepicker/mode/countdowntimer
source_url: 'https://developer.apple.com/documentation/uikit/uidatepicker/mode/countdowntimer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatepicker/mode/countdowntimer.json'
content_hash: 'sha256:8ffc29fcd17cfadd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIDatePicker](../../uidatepicker.md) · [Mode](../mode.md)

# UIDatePicker.Mode.countDownTimer

<sub>Case</sub>

A mode that displays hour and minute values, for example, “1 | 53”. The application must set a timer to fire at the proper interval and set the date picker as the seconds tick down.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case countDownTimer
```

## See Also

### Constants

- [UIDatePickerModeTime](time.md) — A mode that displays the date in hours, minutes, and (optionally) an AM/PM designation. The exact items shown and their order depend upon the locale set. An example of this mode is “6 | 53 | PM”.
- [UIDatePickerModeDate](date.md) — A mode that displays the date in months, days of the month, and years. The exact order of these items depends on the locale setting. An example of this mode is “November | 15 | 2007 “.
- [UIDatePickerModeDateAndTime](dateandtime.md) — A mode that displays the date as unified day of the week, month, and day of the month values, plus hours, minutes, and (optionally) an AM/PM designation. The exact order and format of these items depends on the locale set. An example of this mode is “Wed Nov 15 | 6 | 53 | PM”.
- [UIDatePickerModeYearAndMonth](yearandmonth.md) — A mode that displays the date in months and years.
