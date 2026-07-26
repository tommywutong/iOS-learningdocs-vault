---
title: UICellAccessory.LabelOptions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessory-swift.struct/labeloptions
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/labeloptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/labeloptions.json'
content_hash: 'sha256:422912cf098d139d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# UICellAccessory.LabelOptions

<sub>Structure</sub>

Configuration options for a label accessory.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct LabelOptions
```

## Topics

### Creating configuration options

- [init(isHidden:reservedLayoutWidth:tintColor:font:adjustsFontForContentSizeCategory:)](<labeloptions/init(ishidden_reservedlayoutwidth_tintcolor_font_adjustsfontforcontentsizecategory_).md>) — Creates a label accessory options structure.

### Accessing configuration options

- [isHidden](labeloptions/ishidden.md) — A Boolean value that determines whether the cell hides the accessory.
- [reservedLayoutWidth](labeloptions/reservedlayoutwidth.md) — The layout width that the system reserves for the accessory, and then centers the accessory within.
- [tintColor](labeloptions/tintcolor.md) — The tint color to apply to the accessory.
- [font](labeloptions/font.md) — The font for the label.
- [adjustsFontForContentSizeCategory](labeloptions/adjustsfontforcontentsizecategory.md) — A Boolean value that determines whether the label automatically adjusts its font according to the content size category.

## See Also

### Creating a label accessory

- [label(text:displayed:options:)](<label(text_displayed_options_).md>) — Creates a label system accessory with the specified text, display state, and configuration options.
