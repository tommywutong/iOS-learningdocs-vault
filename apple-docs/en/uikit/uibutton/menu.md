---
title: menu
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/menu
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/menu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/menu.json'
content_hash: 'sha256:3868a9efcfeb9390'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# menu

<sub>Instance Property</sub>

A menu that the button displays.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var menu: UIMenu? { get set }
```

## Discussion

The default value is `nil`. When this property changes, the button automatically enables and disables the [contextMenuInteraction](../uicontrol/contextmenuinteraction.md).

## See Also

### Supporting menu and toggle buttons

- [held](isheld.md) — A Boolean value that indicates whether the button menu is visible.
- [changesSelectionAsPrimaryAction](changesselectionasprimaryaction.md) — A Boolean value that indicates whether the button tracks a selection, either through a menu or a toggle.
- [preferredMenuElementOrder](preferredmenuelementorder.md) — The preferred menu-element ordering strategy for the menu.
