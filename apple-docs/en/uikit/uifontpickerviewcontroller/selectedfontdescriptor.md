---
title: selectedFontDescriptor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontpickerviewcontroller/selectedfontdescriptor
source_url: 'https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller/selectedfontdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontpickerviewcontroller/selectedfontdescriptor.json'
content_hash: 'sha256:e9bc8d110d22609c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontPickerViewController](../uifontpickerviewcontroller.md)

# selectedFontDescriptor

<sub>Instance Property</sub>

Information about the font family or face selected by the user in the font picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var selectedFontDescriptor: UIFontDescriptor? { get set }
```

## Discussion

This font descriptor does not include a size attribute, so if you want to use this descriptor as a parameter in [+ fontWithDescriptor:size:](<../uifont/init(descriptor_size_).md>), you also need a size parameter greater than `0.0`.

## See Also

### Responding to font picker interactions

- [delegate](delegate.md) — The object that handles messages about the user’s interaction with a font picker.
- [UIFontPickerViewControllerDelegate](../uifontpickerviewcontrollerdelegate.md) — A set of optional methods for receiving messages about the user’s interaction with the font picker.
