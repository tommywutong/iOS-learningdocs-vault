---
title: rightViewMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/rightviewmode
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/rightviewmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/rightviewmode.json'
content_hash: 'sha256:afbd36c5f6df2901'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# rightViewMode

<sub>Instance Property</sub>

A mode that controls when the right overlay view appears in the text field.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var rightViewMode: UITextField.ViewMode { get set }
```

## Discussion

The default value for this property is [UITextFieldViewModeNever](viewmode/never.md). Note that the right overlay view flips automatically in a right-to-left user interface.

## See Also

### Managing overlay views

- [clearButtonMode](clearbuttonmode.md) — A mode that controls when the standard Clear button appears in the text field.
- [leftView](leftview.md) — The overlay view that displays on the left (or leading) side of the text field.
- [leftViewMode](leftviewmode.md) — A mode that controls when the left overlay view appears in the text field.
- [rightView](rightview.md) — The overlay view that displays on the right (or trailing) side of the text field.
- [ViewMode](viewmode.md) — Constants that define when overlay views appear in a text field.
