---
title: 'colorPickerViewControllerDidSelectColor(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+（15.0 起废弃）, iPadOS 14.0+（15.0 起废弃）, Mac Catalyst 14.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uicolorpickerviewcontrollerdelegate/colorpickerviewcontrollerdidselectcolor(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicolorpickerviewcontrollerdelegate/colorpickerviewcontrollerdidselectcolor(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolorpickerviewcontrollerdelegate/colorpickerviewcontrollerdidselectcolor%28_%3A%29.json'
content_hash: 'sha256:33a823cbfb444950'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColorPickerViewControllerDelegate](../uicolorpickerviewcontrollerdelegate.md)

# colorPickerViewControllerDidSelectColor(_:)

<sub>Instance Method</sub>

Informs the delegate when the user selects a color.

> [!warning] Deprecated
> Use [- colorPickerViewController:didSelectColor:continuously:](<colorpickerviewcontroller(__didselect_continuously_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func colorPickerViewControllerDidSelectColor(_ viewController: UIColorPickerViewController)
```

## Parameters

- `viewController` — The view controller that receives the color change.
