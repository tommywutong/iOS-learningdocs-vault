---
title: UIDatePickerStyle.inline
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatepickerstyle/inline
source_url: 'https://developer.apple.com/documentation/uikit/uidatepickerstyle/inline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatepickerstyle/inline.json'
content_hash: 'sha256:09a5f599a8803358'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDatePickerStyle](../uidatepickerstyle.md)

# UIDatePickerStyle.inline

<sub>Case</sub>

A style indicating that the date pickers displays as an inline, editable field.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case inline
```

## Discussion

Use this style when you want to let users edit the date picker value without having to tap the label shown in the [UIDatePickerStyleCompact](compact.md) style.

You can’t use this style with the [UIDatePickerModeCountDownTimer](../uidatepicker/mode/countdowntimer.md) mode.

## See Also

### Styles

- [UIDatePickerStyleAutomatic](automatic.md) — A style indicating that the system picks the concrete style based on the current platform and date picker mode.
- [UIDatePickerStyleCompact](compact.md) — A style indicating that the date picker displays as a label that when tapped displays a calendar-style editor.
- [UIDatePickerStyleWheels](wheels.md) — A style indicating that the date picker displays as a wheel picker.
