---
title: UICellAccessory.OutlineDisclosureOptions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessory-swift.struct/outlinedisclosureoptions
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/outlinedisclosureoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/outlinedisclosureoptions.json'
content_hash: 'sha256:efb888ec9c6006c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# UICellAccessory.OutlineDisclosureOptions

<sub>Structure</sub>

Configuration options for an outline disclosure.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct OutlineDisclosureOptions
```

## Topics

### Creating configuration options

- [init(style:isHidden:reservedLayoutWidth:tintColor:)](<outlinedisclosureoptions/init(style_ishidden_reservedlayoutwidth_tintcolor_).md>) — Creates an outline disclosure options structure.

### Accessing configuration options

- [isHidden](outlinedisclosureoptions/ishidden.md) — A Boolean value that determines whether the cell hides the accessory.
- [reservedLayoutWidth](outlinedisclosureoptions/reservedlayoutwidth.md) — The layout width that the system reserves for the accessory, and then centers the accessory within.
- [tintColor](outlinedisclosureoptions/tintcolor.md) — The tint color to apply to the accessory.
- [style](outlinedisclosureoptions/style-swift.property.md) — The style of the outline disclosure accessory.
- [Style](outlinedisclosureoptions/style-swift.enum.md) — Constants that describe the style of the outline disclosure accessory.

## See Also

### Creating an outline disclosure

- [outlineDisclosure(displayed:options:actionHandler:)](<outlinedisclosure(displayed_options_actionhandler_).md>) — Creates an outline disclosure system accessory with the specified display state, configuration options, and optional action handler.
