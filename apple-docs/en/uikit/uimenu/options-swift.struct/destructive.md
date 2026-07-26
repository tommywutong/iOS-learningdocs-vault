---
title: destructive
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenu/options-swift.struct/destructive
source_url: 'https://developer.apple.com/documentation/uikit/uimenu/options-swift.struct/destructive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenu/options-swift.struct/destructive.json'
content_hash: 'sha256:431f1d53337f3e4a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIMenu](../../uimenu.md) · [Options](../options-swift.struct.md)

# destructive

<sub>Type Property</sub>

An option indicating the menu’s appearance represents a destructive action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var destructive: UIMenu.Options { get }
```

## Discussion

Apply this option when you need a menu for a destructive action. Use the menu’s title to communicate the action to perform, and use the menu’s child menu elements to ask for user confirmation of that action.

## See Also

### Options

- [UIMenuOptionsDisplayInline](displayinline.md) — An option indicating the menu displays inline with its parent menu instead of displaying as a submenu.
- [UIMenuOptionsSingleSelection](singleselection.md) — An option indicating whether the menu and its submenus allow a single menu item that’s in the “on” state.
- [UIMenuOptionsDisplayAsPalette](displayaspalette.md) — An option indicating the menu displays as a row of menu elements for choosing from a collection of items.
