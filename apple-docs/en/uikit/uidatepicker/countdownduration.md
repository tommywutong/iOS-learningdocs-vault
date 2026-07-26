---
title: countDownDuration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatepicker/countdownduration
source_url: 'https://developer.apple.com/documentation/uikit/uidatepicker/countdownduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatepicker/countdownduration.json'
content_hash: 'sha256:7aea0935c0ceeb81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDatePicker](../uidatepicker.md)

# countDownDuration

<sub>Instance Property</sub>

The value displayed by the date picker when the mode property is set to show a countdown time.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var countDownDuration: TimeInterval { get set }
```

## Discussion

Use this property to get and set the currently selected value when the date picker’s mode property is set to [UIDatePickerModeCountDownTimer](mode/countdowntimer.md). This property is of type [TimeInterval](../../foundation/timeinterval.md) and therefore is measured in seconds, although the date picker displays only hours and minutes. If the mode of the date picker is not [UIDatePickerModeCountDownTimer](mode/countdowntimer.md), this value is undefined; refer instead to the [date](date.md) property. The default value is 0.0 and the maximum value is 23:59 (86,340 seconds).

## See Also

### Configuring temporal attributes

- [maximumDate](maximumdate.md) — The maximum date that a date picker can show.
- [minimumDate](minimumdate.md) — The minimum date that a date picker can show.
- [minuteInterval](minuteinterval.md) — The interval at which the date picker should display minutes.
- [roundsToMinuteInterval](roundstominuteinterval.md) — A Boolean value that determines whether the date rounds to a specific minute interval.
