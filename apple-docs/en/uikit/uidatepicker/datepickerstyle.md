---
title: datePickerStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatepicker/datepickerstyle
source_url: 'https://developer.apple.com/documentation/uikit/uidatepicker/datepickerstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatepicker/datepickerstyle.json'
content_hash: 'sha256:fefb2abdd70c8666'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDatePicker](../uidatepicker.md)

# datePickerStyle

<sub>Instance Property</sub>

The current style of the date picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var datePickerStyle: UIDatePickerStyle { get }
```

## Discussion

This property always returns a concrete style, never [UIDatePickerStyleAutomatic](../uidatepickerstyle/automatic.md).

## See Also

### Configuring the date picker style

- [preferredDatePickerStyle](preferreddatepickerstyle.md) — The preferred style of the date picker.
- [UIDatePickerStyle](../uidatepickerstyle.md) — Styles that determine the appearance of a date picker.
