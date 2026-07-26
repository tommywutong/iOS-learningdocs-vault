---
title: 'colorPickerViewController(_:didSelect:continuously:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolorpickerviewcontrollerdelegate/colorpickerviewcontroller(_:didselect:continuously:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicolorpickerviewcontrollerdelegate/colorpickerviewcontroller(_:didselect:continuously:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolorpickerviewcontrollerdelegate/colorpickerviewcontroller%28_%3Adidselect%3Acontinuously%3A%29.json'
content_hash: 'sha256:854ea2b4430e07ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColorPickerViewControllerDelegate](../uicolorpickerviewcontrollerdelegate.md)

# colorPickerViewController(_:didSelect:continuously:)

<sub>Instance Method</sub>

Informs the delegate when a user selects a color, indicating whether the update is part of a continuous user interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func colorPickerViewController(_ viewController: UIColorPickerViewController, didSelect color: UIColor, continuously: Bool)
```

## Parameters

- `viewController` — The color picker.

- `color` — The new color.

- `continuously` — A Boolean value that indicates whether the update is part of a continuous user interaction.

## Discussion

A continuous selection is always followed by a noncontinuous one when the user finishes the gesture. Apps that support undoing should update their UI for all color changes but only undo to noncontinuous color changes.

## See Also

### Handling color picker activity

- [- colorPickerViewControllerDidFinish:](<colorpickerviewcontrollerdidfinish(__).md>) — Informs the delegate that the user dismissed the color picker.
