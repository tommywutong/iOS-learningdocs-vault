---
title: 'fontPickerViewControllerDidPickFont(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifontpickerviewcontrollerdelegate/fontpickerviewcontrollerdidpickfont(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifontpickerviewcontrollerdelegate/fontpickerviewcontrollerdidpickfont(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontpickerviewcontrollerdelegate/fontpickerviewcontrollerdidpickfont%28_%3A%29.json'
content_hash: 'sha256:647b499ac23ec781'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontPickerViewControllerDelegate](../uifontpickerviewcontrollerdelegate.md)

# fontPickerViewControllerDidPickFont(_:)

<sub>Instance Method</sub>

Tells the delegate that the user has selected a font.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func fontPickerViewControllerDidPickFont(_ viewController: UIFontPickerViewController)
```

## Parameters

- `viewController` — The controller for the font picker that has the user’s font selection.

## Discussion

When the user picks a font, you can retrieve information about the user’s selected font from the view controller’s [selectedFontDescriptor](../uifontpickerviewcontroller/selectedfontdescriptor.md).

## See Also

### Receiving font picker interactions

- [- fontPickerViewControllerDidCancel:](<fontpickerviewcontrollerdidcancel(__).md>) — Tells the delegate that the user dismissed the font picker without selecting a font.
