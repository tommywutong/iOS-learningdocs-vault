---
title: 'fontPickerViewControllerDidCancel(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifontpickerviewcontrollerdelegate/fontpickerviewcontrollerdidcancel(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifontpickerviewcontrollerdelegate/fontpickerviewcontrollerdidcancel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontpickerviewcontrollerdelegate/fontpickerviewcontrollerdidcancel%28_%3A%29.json'
content_hash: 'sha256:8bd102afe374c667'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontPickerViewControllerDelegate](../uifontpickerviewcontrollerdelegate.md)

# fontPickerViewControllerDidCancel(_:)

<sub>Instance Method</sub>

Tells the delegate that the user dismissed the font picker without selecting a font.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func fontPickerViewControllerDidCancel(_ viewController: UIFontPickerViewController)
```

## Parameters

- `viewController` — The controller for the font picker that was canceled.

## Discussion

Implement this optional method if your app needs to add custom logic when the user cancels the font picker instead of picking a font.

## See Also

### Receiving font picker interactions

- [- fontPickerViewControllerDidPickFont:](<fontpickerviewcontrollerdidpickfont(__).md>) — Tells the delegate that the user has selected a font.
