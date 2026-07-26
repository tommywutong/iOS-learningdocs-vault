---
title: clearButtonMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/clearbuttonmode
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/clearbuttonmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/clearbuttonmode.json'
content_hash: 'sha256:9a84d3abaf65523b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# clearButtonMode

<sub>Instance Property</sub>

A mode that controls when the standard Clear button appears in the text field.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var clearButtonMode: UITextField.ViewMode { get set }
```

## Discussion

The standard clear button displays at the right side of the text field when the text field has contents, providing a way for the user to remove text quickly.

This button appears automatically based on the value of this property. The default value for this property is [UITextFieldViewModeNever](viewmode/never.md).

## See Also

### Managing overlay views

- [leftView](leftview.md) — The overlay view that displays on the left (or leading) side of the text field.
- [leftViewMode](leftviewmode.md) — A mode that controls when the left overlay view appears in the text field.
- [rightView](rightview.md) — The overlay view that displays on the right (or trailing) side of the text field.
- [rightViewMode](rightviewmode.md) — A mode that controls when the right overlay view appears in the text field.
- [ViewMode](viewmode.md) — Constants that define when overlay views appear in a text field.
