---
title: changesSelectionAsPrimaryAction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/changesselectionasprimaryaction
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/changesselectionasprimaryaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/changesselectionasprimaryaction.json'
content_hash: 'sha256:1765dabcdddd98be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# changesSelectionAsPrimaryAction

<sub>Instance Property</sub>

A Boolean value that indicates whether the button tracks a selection, either through a menu or a toggle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var changesSelectionAsPrimaryAction: Bool { get set }
```

## Discussion

This behavior of this property composes with [showsMenuAsPrimaryAction](../uicontrol/showsmenuasprimaryaction.md) and the [menu](menu.md) property.

If [menu](menu.md) is `nil`, setting this property to [true](../../swift/true.md) makes the button toggle its [UIControlStateSelected](../uicontrol/state-swift.struct/selected.md) state.

If you set a menu and [showsMenuAsPrimaryAction](../uicontrol/showsmenuasprimaryaction.md) is [false](../../swift/false.md), setting this property to [true](../../swift/true.md) makes the button a toggle button. The menu functions as a contextual menu, which appears after a long press.

If you set a menu and [showsMenuAsPrimaryAction](../uicontrol/showsmenuasprimaryaction.md) is [true](../../swift/true.md), setting this property to [true](../../swift/true.md) makes the button function as a pop-up. The button presents the menu on touch, the menu tracks the selection in its [selectedElements](../uimenu/selectedelements.md) property, and the button title updates to reflect the selection.

## See Also

### Supporting menu and toggle buttons

- [menu](menu.md) — A menu that the button displays.
- [held](isheld.md) — A Boolean value that indicates whether the button menu is visible.
- [preferredMenuElementOrder](preferredmenuelementorder.md) — The preferred menu-element ordering strategy for the menu.
