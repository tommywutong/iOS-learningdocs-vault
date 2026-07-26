---
title: UITextField.ViewMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/viewmode
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/viewmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/viewmode.json'
content_hash: 'sha256:5c36a39963d46f90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# UITextField.ViewMode

<sub>Enumeration</sub>

Constants that define when overlay views appear in a text field.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum ViewMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UITextFieldViewModeNever](viewmode/never.md) — The overlay view never appears.
- [UITextFieldViewModeWhileEditing](viewmode/whileediting.md) — The overlay view is displayed only while text is being edited in the text field.
- [UITextFieldViewModeUnlessEditing](viewmode/unlessediting.md) — The overlay view is displayed only when text is not being edited.
- [UITextFieldViewModeAlways](viewmode/always.md) — The overlay view is always displayed if the text field contains text.

### Initializers

- [init(rawValue:)](<viewmode/init(rawvalue_).md>)

## See Also

### Managing overlay views

- [clearButtonMode](clearbuttonmode.md) — A mode that controls when the standard Clear button appears in the text field.
- [leftView](leftview.md) — The overlay view that displays on the left (or leading) side of the text field.
- [leftViewMode](leftviewmode.md) — A mode that controls when the left overlay view appears in the text field.
- [rightView](rightview.md) — The overlay view that displays on the right (or trailing) side of the text field.
- [rightViewMode](rightviewmode.md) — A mode that controls when the right overlay view appears in the text field.
