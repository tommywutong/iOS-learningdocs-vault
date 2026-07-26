---
title: minimumDate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatepicker/minimumdate
source_url: 'https://developer.apple.com/documentation/uikit/uidatepicker/minimumdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatepicker/minimumdate.json'
content_hash: 'sha256:46bd33d7acc42764'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDatePicker](../uidatepicker.md)

# minimumDate

<sub>Instance Property</sub>

The minimum date that a date picker can show.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var minimumDate: Date? { get set }
```

## Discussion

Use this property to configure the minimum date that’s selected in the date picker interface. The property contains an [NSDate](../../foundation/nsdate.md) object or `nil` (the default), which means no minimum date. This property, along with the [maximumDate](maximumdate.md) property, lets you specify a valid date range. If the minimum date value is greater than the maximum date value, both properties are ignored. The minimum and maximum dates are also ignored in the countdown-timer mode ([UIDatePickerModeCountDownTimer](mode/countdowntimer.md)).

## See Also

### Configuring temporal attributes

- [maximumDate](maximumdate.md) — The maximum date that a date picker can show.
- [minuteInterval](minuteinterval.md) — The interval at which the date picker should display minutes.
- [countDownDuration](countdownduration.md) — The value displayed by the date picker when the mode property is set to show a countdown time.
- [roundsToMinuteInterval](roundstominuteinterval.md) — A Boolean value that determines whether the date rounds to a specific minute interval.
