---
title: UICellAccessory.DeleteOptions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessory-swift.struct/deleteoptions
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/deleteoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/deleteoptions.json'
content_hash: 'sha256:179d12ec3e6dc7e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# UICellAccessory.DeleteOptions

<sub>Structure</sub>

Configuration options for a delete accessory.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct DeleteOptions
```

## Topics

### Creating configuration options

- [init(isHidden:reservedLayoutWidth:tintColor:backgroundColor:)](<deleteoptions/init(ishidden_reservedlayoutwidth_tintcolor_backgroundcolor_).md>) — Creates a delete accessory options structure.

### Accessing configuration options

- [isHidden](deleteoptions/ishidden.md) — A Boolean value that determines whether the cell hides the accessory.
- [reservedLayoutWidth](deleteoptions/reservedlayoutwidth.md) — The layout width that the system reserves for the accessory, and then centers the accessory within.
- [tintColor](deleteoptions/tintcolor.md) — The tint color to apply to the accessory.
- [backgroundColor](deleteoptions/backgroundcolor.md) — The background color to apply to the accessory.

## See Also

### Creating a delete accessory

- [delete(displayed:options:actionHandler:)](<delete(displayed_options_actionhandler_).md>) — Creates a delete system accessory with the specified display state, configuration options, and optional action handler.
