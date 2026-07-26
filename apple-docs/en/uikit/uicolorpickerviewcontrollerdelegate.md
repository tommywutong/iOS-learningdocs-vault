---
title: UIColorPickerViewControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicolorpickerviewcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uicolorpickerviewcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolorpickerviewcontrollerdelegate.json'
content_hash: 'sha256:836355da66bd973f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIColorPickerViewControllerDelegate

<sub>Protocol</sub>

The delegate protocol to inform about changes in color selection.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIColorPickerViewControllerDelegate : NSObjectProtocol
```

## Overview

By implementing the [UIColorPickerViewControllerDelegate](uicolorpickerviewcontrollerdelegate.md) functions, your app can react to a color-selection change or the dismissal of the color picker.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Handling color picker activity

- [- colorPickerViewControllerDidFinish:](<uicolorpickerviewcontrollerdelegate/colorpickerviewcontrollerdidfinish(__).md>) — Informs the delegate that the user dismissed the color picker.
- [- colorPickerViewController:didSelectColor:continuously:](<uicolorpickerviewcontrollerdelegate/colorpickerviewcontroller(__didselect_continuously_).md>) — Informs the delegate when a user selects a color, indicating whether the update is part of a continuous user interaction.

### Deprecated

- [- colorPickerViewControllerDidSelectColor:](<uicolorpickerviewcontrollerdelegate/colorpickerviewcontrollerdidselectcolor(__).md>) — Informs the delegate when the user selects a color. _(deprecated)_

## See Also

### Color picker

- [UIColorPickerViewController](uicolorpickerviewcontroller.md) — A view controller that manages the interface for selecting a color.
