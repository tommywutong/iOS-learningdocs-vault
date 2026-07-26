---
title: UIDatePicker.Mode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatepicker/mode
source_url: 'https://developer.apple.com/documentation/uikit/uidatepicker/mode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatepicker/mode.json'
content_hash: 'sha256:e01195e258b03315'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDatePicker](../uidatepicker.md)

# UIDatePicker.Mode

<sub>Enumeration</sub>

The mode displayed by the date picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum Mode
```

## Overview

The mode determines whether dates, times, or both dates and times are displayed. You can also use it to specify the appearance of a countdown timer. You can set and retrieve the mode value through the [datePickerMode](datepickermode.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIDatePickerModeTime](mode/time.md) — A mode that displays the date in hours, minutes, and (optionally) an AM/PM designation. The exact items shown and their order depend upon the locale set. An example of this mode is “6 | 53 | PM”.
- [UIDatePickerModeDate](mode/date.md) — A mode that displays the date in months, days of the month, and years. The exact order of these items depends on the locale setting. An example of this mode is “November | 15 | 2007 “.
- [UIDatePickerModeDateAndTime](mode/dateandtime.md) — A mode that displays the date as unified day of the week, month, and day of the month values, plus hours, minutes, and (optionally) an AM/PM designation. The exact order and format of these items depends on the locale set. An example of this mode is “Wed Nov 15 | 6 | 53 | PM”.
- [UIDatePickerModeYearAndMonth](mode/yearandmonth.md) — A mode that displays the date in months and years.
- [UIDatePickerModeCountDownTimer](mode/countdowntimer.md) — A mode that displays hour and minute values, for example, “1 | 53”. The application must set a timer to fire at the proper interval and set the date picker as the seconds tick down.

### Initializers

- [init(rawValue:)](<mode/init(rawvalue_).md>)

## See Also

### Configuring the date picker mode

- [datePickerMode](datepickermode.md) — The mode of the date picker.
