---
title: maintainsFixedSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessory-swift.struct/customviewconfiguration/maintainsfixedsize
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/customviewconfiguration/maintainsfixedsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/customviewconfiguration/maintainsfixedsize.json'
content_hash: 'sha256:b63ea21e9e90690b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICellAccessory](../../uicellaccessory-swift.struct.md) · [CustomViewConfiguration](../customviewconfiguration.md)

# maintainsFixedSize

<sub>Instance Property</sub>

A Boolean value that determines whether to preserve the frame size of the custom view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var maintainsFixedSize: Bool
```

## Discussion

When the value of this property is [true](../../../swift/true.md), the system preserves the current frame size of the view. When the value of this property is [false](../../../swift/false.md), the system sizes the view during layout of the accessories.

The default value of this property is [false](../../../swift/false.md).

## See Also

### Accessing configuration options

- [isHidden](ishidden.md) — A Boolean value that determines whether the cell hides the accessory.
- [customView](customview.md) — The custom view to display for the accessory.
- [placement](placement.md) — The placement for the accessory.
- [reservedLayoutWidth](reservedlayoutwidth.md) — The layout width that the system reserves for the accessory, and then centers the accessory within.
- [tintColor](tintcolor.md) — The tint color to apply to the accessory.
