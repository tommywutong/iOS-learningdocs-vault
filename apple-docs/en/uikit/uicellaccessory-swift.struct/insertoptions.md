---
title: UICellAccessory.InsertOptions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessory-swift.struct/insertoptions
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/insertoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/insertoptions.json'
content_hash: 'sha256:f2fe3e3983b5072b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# UICellAccessory.InsertOptions

<sub>Structure</sub>

Configuration options for an insert accessory.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct InsertOptions
```

## Topics

### Creating configuration options

- [init(isHidden:reservedLayoutWidth:tintColor:backgroundColor:)](<insertoptions/init(ishidden_reservedlayoutwidth_tintcolor_backgroundcolor_).md>) — Creates an insert accessory options structure.

### Accessing configuration options

- [isHidden](insertoptions/ishidden.md) — A Boolean value that determines whether the cell hides the accessory.
- [reservedLayoutWidth](insertoptions/reservedlayoutwidth.md) — The layout width that the system reserves for the accessory, and then centers the accessory within.
- [tintColor](insertoptions/tintcolor.md) — The tint color to apply to the accessory.
- [backgroundColor](insertoptions/backgroundcolor.md) — The background color to apply to the accessory.

## See Also

### Creating an insert accessory

- [insert(displayed:options:actionHandler:)](<insert(displayed_options_actionhandler_).md>) — Creates an insert system accessory with the specified display state, configuration options, and optional action handler.
