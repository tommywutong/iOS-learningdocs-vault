---
title: minuteInterval
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatepicker/minuteinterval
source_url: 'https://developer.apple.com/documentation/uikit/uidatepicker/minuteinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatepicker/minuteinterval.json'
content_hash: 'sha256:a68636d4b4f6609b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDatePicker](../uidatepicker.md)

# minuteInterval

<sub>Instance Property</sub>

The interval at which the date picker should display minutes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var minuteInterval: Int { get set }
```

## Discussion

Use this property to set the interval displayed by the minutes wheel (for example, 15 minutes). The interval value must be evenly divided into 60; if it isn’t, the default value is used. The default and minimum values are 1; the maximum value is 30.

## See Also

### Configuring temporal attributes

- [maximumDate](maximumdate.md) — The maximum date that a date picker can show.
- [minimumDate](minimumdate.md) — The minimum date that a date picker can show.
- [countDownDuration](countdownduration.md) — The value displayed by the date picker when the mode property is set to show a countdown time.
- [roundsToMinuteInterval](roundstominuteinterval.md) — A Boolean value that determines whether the date rounds to a specific minute interval.
