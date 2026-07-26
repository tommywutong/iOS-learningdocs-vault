---
title: isHeld
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/isheld
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/isheld'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/isheld.json'
content_hash: 'sha256:c4bc5e22d14d3792'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# isHeld

<sub>Instance Property</sub>

A Boolean value that indicates whether the button menu is visible.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isHeld: Bool { get }
```

## Discussion

The property is [true](../../swift/true.md) if the button is presenting a menu in response to a long press. Buttons that set [showsMenuAsPrimaryAction](../uicontrol/showsmenuasprimaryaction.md) to present a menu don’t set this property.

## See Also

### Supporting menu and toggle buttons

- [menu](menu.md) — A menu that the button displays.
- [changesSelectionAsPrimaryAction](changesselectionasprimaryaction.md) — A Boolean value that indicates whether the button tracks a selection, either through a menu or a toggle.
- [preferredMenuElementOrder](preferredmenuelementorder.md) — The preferred menu-element ordering strategy for the menu.
