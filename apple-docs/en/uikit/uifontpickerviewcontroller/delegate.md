---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontpickerviewcontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontpickerviewcontroller/delegate.json'
content_hash: 'sha256:44a482fb718f131e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontPickerViewController](../uifontpickerviewcontroller.md)

# delegate

<sub>Instance Property</sub>

The object that handles messages about the user’s interaction with a font picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UIFontPickerViewControllerDelegate)? { get set }
```

## See Also

### Responding to font picker interactions

- [UIFontPickerViewControllerDelegate](../uifontpickerviewcontrollerdelegate.md) — A set of optional methods for receiving messages about the user’s interaction with the font picker.
- [selectedFontDescriptor](selectedfontdescriptor.md) — Information about the font family or face selected by the user in the font picker.
