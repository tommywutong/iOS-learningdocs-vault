---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicolorpickerviewcontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uicolorpickerviewcontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolorpickerviewcontroller/delegate.json'
content_hash: 'sha256:9099216127d64bd3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColorPickerViewController](../uicolorpickerviewcontroller.md)

# delegate

<sub>Instance Property</sub>

The delegate that receives updates about the color selection.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UIColorPickerViewControllerDelegate)? { get set }
```

## See Also

### Configuring the color picker view controller

- [UIColorPickerViewControllerDelegate](../uicolorpickerviewcontrollerdelegate.md) — The delegate protocol to inform about changes in color selection.
- [maximumLinearExposure](maximumlinearexposure.md) — The maximum exposure to apply to a color when returned by the color picker.
- [selectedColor](selectedcolor.md) — The color selected by the user.
- [supportsAlpha](supportsalpha.md) — A Boolean value that enables alpha value control.
- [supportsEyedropper](supportseyedropper.md) — If set to `NO` the eyedropper functionality is not supported for this color picker.
