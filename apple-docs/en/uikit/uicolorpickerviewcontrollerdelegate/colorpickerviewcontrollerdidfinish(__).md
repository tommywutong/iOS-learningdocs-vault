---
title: 'colorPickerViewControllerDidFinish(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolorpickerviewcontrollerdelegate/colorpickerviewcontrollerdidfinish(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicolorpickerviewcontrollerdelegate/colorpickerviewcontrollerdidfinish(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolorpickerviewcontrollerdelegate/colorpickerviewcontrollerdidfinish%28_%3A%29.json'
content_hash: 'sha256:ecfe0173ca38ec9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColorPickerViewControllerDelegate](../uicolorpickerviewcontrollerdelegate.md)

# colorPickerViewControllerDidFinish(_:)

<sub>Instance Method</sub>

Informs the delegate that the user dismissed the color picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func colorPickerViewControllerDidFinish(_ viewController: UIColorPickerViewController)
```

## Parameters

- `viewController` — The view controller that starts dismissing.

## Discussion

The system calls this method when the user dismisses the color picker.

You can implement this method to show additional animations alongside the dismissal animation. For interactive dismissals, use the delegate of the presentation controller that manages the color picker instead.

## See Also

### Handling color picker activity

- [- colorPickerViewController:didSelectColor:continuously:](<colorpickerviewcontroller(__didselect_continuously_).md>) — Informs the delegate when a user selects a color, indicating whether the update is part of a continuous user interaction.
