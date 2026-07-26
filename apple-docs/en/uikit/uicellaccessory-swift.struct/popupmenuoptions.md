---
title: UICellAccessory.PopUpMenuOptions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessory-swift.struct/popupmenuoptions
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/popupmenuoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/popupmenuoptions.json'
content_hash: 'sha256:a0aa6136cf2bcd0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# UICellAccessory.PopUpMenuOptions

<sub>Structure</sub>

Configuration options for a popup menu accessory.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct PopUpMenuOptions
```

## Topics

### Creating configuration options

- [init(isHidden:reservedLayoutWidth:tintColor:)](<popupmenuoptions/init(ishidden_reservedlayoutwidth_tintcolor_).md>) — Creates a popup menu accessory options structure.

### Accessing configuration options

- [isHidden](popupmenuoptions/ishidden.md) — A Boolean value that determines whether the cell hides the accessory.
- [reservedLayoutWidth](popupmenuoptions/reservedlayoutwidth.md) — The layout width that the system reserves for the accessory, and then centers the accessory within.
- [tintColor](popupmenuoptions/tintcolor.md) — The tint color to apply to the accessory.

## See Also

### Creating a popup menu accessory

- [popUpMenu(_:displayed:options:selectedElementDidChangeHandler:)](<popupmenu(__displayed_options_selectedelementdidchangehandler_).md>) — Creates a popup menu system accessory with the specified menu, display state, configuration options, and optional selection handler.
- [MenuSelectedElementDidChangeHandler](menuselectedelementdidchangehandler.md) — A closure type that defines a handler to perform when a user selects an element in the menu.
