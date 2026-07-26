---
title: 'setDate(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidatepicker/setdate(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidatepicker/setdate(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatepicker/setdate%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:854b8b87246ffc4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDatePicker](../uidatepicker.md)

# setDate(_:animated:)

<sub>Instance Method</sub>

Sets the date to display in the date picker, with an option to animate the setting.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setDate(_ date: Date, animated: Bool)
```

## Parameters

- `date` — An `NSDate` object representing the new date to display in the date picker.

- `animated` — [true](../../swift/true.md) to animate the setting of the new date, otherwise [false](../../swift/false.md). The animation rotates the wheels until the new date and time is shown under the highlight rectangle.

## See Also

### Managing the date and calendar

- [calendar](calendar.md) — The calendar to use for the date picker.
- [date](date.md) — The date displayed by the date picker.
- [locale](locale.md) — The locale used by the date picker.
- [timeZone](timezone.md) — The time zone reflected in the date displayed by the date picker.
