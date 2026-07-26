---
title: UIFontPickerViewControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontpickerviewcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uifontpickerviewcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontpickerviewcontrollerdelegate.json'
content_hash: 'sha256:b6a4f214280ed854'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFontPickerViewControllerDelegate

<sub>Protocol</sub>

A set of optional methods for receiving messages about the user’s interaction with the font picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIFontPickerViewControllerDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UITextFormattingCoordinator](uitextformattingcoordinator.md)

## Topics

### Receiving font picker interactions

- [- fontPickerViewControllerDidCancel:](<uifontpickerviewcontrollerdelegate/fontpickerviewcontrollerdidcancel(__).md>) — Tells the delegate that the user dismissed the font picker without selecting a font.
- [- fontPickerViewControllerDidPickFont:](<uifontpickerviewcontrollerdelegate/fontpickerviewcontrollerdidpickfont(__).md>) — Tells the delegate that the user has selected a font.

## See Also

### Font picker

- [UIFontPickerViewController](uifontpickerviewcontroller.md) — A view controller that manages the interface for selecting a font that the system provides or the user installs.
- [Configuration](uifontpickerviewcontroller/configuration-swift.class.md) — The filters and display settings a font picker view controller uses to set up a font picker.
