---
title: maximumDate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatepicker/maximumdate
source_url: 'https://developer.apple.com/documentation/uikit/uidatepicker/maximumdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatepicker/maximumdate.json'
content_hash: 'sha256:33788420989c6d36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDatePicker](../uidatepicker.md)

# maximumDate

<sub>Instance Property</sub>

The maximum date that a date picker can show.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var maximumDate: Date? { get set }
```

## Discussion

Use this property to configure the maximum date that’s selected in the date picker interface. The property contains an [NSDate](../../foundation/nsdate.md) object or `nil` (the default), which means no maximum date. This property, along with the [minimumDate](minimumdate.md) property, lets you specify a valid date range. If the minimum date value is greater than the maximum date value, both properties are ignored. The minimum and maximum dates are also ignored in the countdown-timer mode ([UIDatePickerModeCountDownTimer](mode/countdowntimer.md)).

## See Also

### Configuring temporal attributes

- [minimumDate](minimumdate.md) — The minimum date that a date picker can show.
- [minuteInterval](minuteinterval.md) — The interval at which the date picker should display minutes.
- [countDownDuration](countdownduration.md) — The value displayed by the date picker when the mode property is set to show a countdown time.
- [roundsToMinuteInterval](roundstominuteinterval.md) — A Boolean value that determines whether the date rounds to a specific minute interval.
