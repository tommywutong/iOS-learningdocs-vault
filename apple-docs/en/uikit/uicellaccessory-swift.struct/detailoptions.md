---
title: UICellAccessory.DetailOptions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, tvOS 15.4+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessory-swift.struct/detailoptions
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/detailoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/detailoptions.json'
content_hash: 'sha256:a3185a22158b9bed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# UICellAccessory.DetailOptions

<sub>Structure</sub>

Configuration options for a detail accessory.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct DetailOptions
```

## Topics

### Creating configuration options

- [init(isHidden:reservedLayoutWidth:tintColor:)](<detailoptions/init(ishidden_reservedlayoutwidth_tintcolor_).md>) — Creates a detail accessory options structure.

### Accessing configuration options

- [isHidden](detailoptions/ishidden.md) — A Boolean value that determines whether the cell hides the accessory.
- [reservedLayoutWidth](detailoptions/reservedlayoutwidth.md) — The layout width that the system reserves for the accessory, and then centers the accessory within.
- [tintColor](detailoptions/tintcolor.md) — The tint color to apply to the accessory.

## See Also

### Creating a detail accessory

- [detail(displayed:options:actionHandler:)](<detail(displayed_options_actionhandler_).md>) — Creates a detail system accessory with the specified display state, configuration options, and optional action handler.
