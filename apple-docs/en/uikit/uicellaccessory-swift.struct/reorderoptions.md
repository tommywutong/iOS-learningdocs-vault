---
title: UICellAccessory.ReorderOptions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessory-swift.struct/reorderoptions
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/reorderoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/reorderoptions.json'
content_hash: 'sha256:77cec665de84163f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# UICellAccessory.ReorderOptions

<sub>Structure</sub>

Configuration options for a reorder accessory.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct ReorderOptions
```

## Topics

### Creating configuration options

- [init(isHidden:reservedLayoutWidth:tintColor:showsVerticalSeparator:)](<reorderoptions/init(ishidden_reservedlayoutwidth_tintcolor_showsverticalseparator_).md>) — Creates a reorder accessory options structure.

### Accessing configuration options

- [isHidden](reorderoptions/ishidden.md) — A Boolean value that determines whether the cell hides the accessory.
- [reservedLayoutWidth](reorderoptions/reservedlayoutwidth.md) — The layout width that the system reserves for the accessory, and then centers the accessory within.
- [tintColor](reorderoptions/tintcolor.md) — The tint color to apply to the accessory.
- [showsVerticalSeparator](reorderoptions/showsverticalseparator.md) — A Boolean value that determines whether a vertical separator displays before the accessory when it appears after another accessory.

## See Also

### Creating a reorder accessory

- [reorder(displayed:options:)](<reorder(displayed_options_).md>) — Creates a reorder system accessory with the specified display state and configuration options.
