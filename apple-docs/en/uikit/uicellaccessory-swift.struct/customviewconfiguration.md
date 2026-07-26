---
title: UICellAccessory.CustomViewConfiguration
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessory-swift.struct/customviewconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/customviewconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/customviewconfiguration.json'
content_hash: 'sha256:f1ac2e9600b906ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# UICellAccessory.CustomViewConfiguration

<sub>Structure</sub>

Configuration options for a custom accessory.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct CustomViewConfiguration
```

## Topics

### Creating configuration options

- [init(customView:placement:isHidden:reservedLayoutWidth:tintColor:maintainsFixedSize:)](<customviewconfiguration/init(customview_placement_ishidden_reservedlayoutwidth_tintcolor_maintainsfixedsize_).md>) — Creates a custom accessory options structure.

### Accessing configuration options

- [isHidden](customviewconfiguration/ishidden.md) — A Boolean value that determines whether the cell hides the accessory.
- [customView](customviewconfiguration/customview.md) — The custom view to display for the accessory.
- [placement](customviewconfiguration/placement.md) — The placement for the accessory.
- [reservedLayoutWidth](customviewconfiguration/reservedlayoutwidth.md) — The layout width that the system reserves for the accessory, and then centers the accessory within.
- [tintColor](customviewconfiguration/tintcolor.md) — The tint color to apply to the accessory.
- [maintainsFixedSize](customviewconfiguration/maintainsfixedsize.md) — A Boolean value that determines whether to preserve the frame size of the custom view.

## See Also

### Creating a custom accessory

- [customView(configuration:)](<customview(configuration_).md>) — Creates a custom view accessory.
