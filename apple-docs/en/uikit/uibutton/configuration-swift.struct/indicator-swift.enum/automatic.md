---
title: UIButton.Configuration.Indicator.automatic
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/indicator-swift.enum/automatic
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/indicator-swift.enum/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/indicator-swift.enum/automatic.json'
content_hash: 'sha256:0e04509f7d7581dd'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [UIKit](../../../../uikit.md) · [UIButton](../../../uibutton.md) · [Configuration](../../configuration-swift.struct.md) · [Indicator](../indicator-swift.enum.md)

# UIButton.Configuration.Indicator.automatic

<sub>Case</sub>

A constant that automatically determines an indicator style according to the button’s properties.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case automatic
```

## Discussion

With this behavior, the system automatically shows an indicator if the button shows a menu and has single-selection behavior (when its [contextMenuInteractionEnabled](../../../uicontrol/iscontextmenuinteractionenabled.md), [showsMenuAsPrimaryAction](../../../uicontrol/showsmenuasprimaryaction.md), and [changesSelectionAsPrimaryAction](../../changesselectionasprimaryaction.md) properties are [true](../../../../swift/true.md)).

## See Also

### Indicator styles

- [UIButton.Configuration.Indicator.none](none.md) — A constant that doesn’t show an indicator.
- [UIButton.Configuration.Indicator.popup](popup.md) — A constant that shows a popup-style indicator.
