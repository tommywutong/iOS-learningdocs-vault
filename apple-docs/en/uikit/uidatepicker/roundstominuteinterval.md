---
title: roundsToMinuteInterval
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatepicker/roundstominuteinterval
source_url: 'https://developer.apple.com/documentation/uikit/uidatepicker/roundstominuteinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatepicker/roundstominuteinterval.json'
content_hash: 'sha256:45bf5959fdb6f512'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDatePicker](../uidatepicker.md)

# roundsToMinuteInterval

<sub>Instance Property</sub>

A Boolean value that determines whether the date rounds to a specific minute interval.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var roundsToMinuteInterval: Bool { get set }
```

## Discussion

If this property is [true](../../swift/true.md), [date](date.md) always rounds to the [minuteInterval](minuteinterval.md) and only produces dates that align with the minute interval. If this property is [false](../../swift/false.md), changes to [date](date.md) ignore the [minuteInterval](minuteinterval.md) property.

The default value is [true](../../swift/true.md).

## See Also

### Configuring temporal attributes

- [maximumDate](maximumdate.md) — The maximum date that a date picker can show.
- [minimumDate](minimumdate.md) — The minimum date that a date picker can show.
- [minuteInterval](minuteinterval.md) — The interval at which the date picker should display minutes.
- [countDownDuration](countdownduration.md) — The value displayed by the date picker when the mode property is set to show a countdown time.
