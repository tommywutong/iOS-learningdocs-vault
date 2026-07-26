---
title: preferredDatePickerStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatepicker/preferreddatepickerstyle
source_url: 'https://developer.apple.com/documentation/uikit/uidatepicker/preferreddatepickerstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatepicker/preferreddatepickerstyle.json'
content_hash: 'sha256:5e1beada286d086a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDatePicker](../uidatepicker.md)

# preferredDatePickerStyle

<sub>Instance Property</sub>

The preferred style of the date picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var preferredDatePickerStyle: UIDatePickerStyle { get set }
```

## Discussion

Use this property to specify the display style that you prefer. If the style changes, the date picker may generate a layout pass to update the display.

The default style is [UIDatePickerStyleAutomatic](../uidatepickerstyle/automatic.md). For a list of styles, see [UIDatePickerStyle](../uidatepickerstyle.md).

## See Also

### Configuring the date picker style

- [datePickerStyle](datepickerstyle.md) — The current style of the date picker.
- [UIDatePickerStyle](../uidatepickerstyle.md) — Styles that determine the appearance of a date picker.
