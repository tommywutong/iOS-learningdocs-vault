---
title: datePickerMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatepicker/datepickermode
source_url: 'https://developer.apple.com/documentation/uikit/uidatepicker/datepickermode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatepicker/datepickermode.json'
content_hash: 'sha256:f36a14976dbe663d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDatePicker](../uidatepicker.md)

# datePickerMode

<sub>Instance Property</sub>

The mode of the date picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var datePickerMode: UIDatePicker.Mode { get set }
```

## Discussion

Use this property to change the type of information displayed by the date picker. It determines whether the date picker allows selection of a date, a time, both date and time, or a countdown time. The default mode is [UIDatePickerModeDateAndTime](mode/dateandtime.md). See [Mode](mode.md) for a list of mode constants.

## See Also

### Configuring the date picker mode

- [Mode](mode.md) — The mode displayed by the date picker.
