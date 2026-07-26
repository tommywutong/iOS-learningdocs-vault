---
title: isHidden
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessory-swift.struct/outlinedisclosureoptions/ishidden
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/outlinedisclosureoptions/ishidden'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/outlinedisclosureoptions/ishidden.json'
content_hash: 'sha256:39091e02bbd9190f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICellAccessory](../../uicellaccessory-swift.struct.md) · [OutlineDisclosureOptions](../outlinedisclosureoptions.md)

# isHidden

<sub>Instance Property</sub>

A Boolean value that determines whether the cell hides the accessory.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isHidden: Bool
```

## Discussion

A hidden accessory takes up space in the layout, but it isn’t visible and doesn’t provide any behaviors.

Use this property to achieve a consistent layout across cells when some cells show this type of accessory and others don’t.

## See Also

### Accessing configuration options

- [reservedLayoutWidth](reservedlayoutwidth.md) — The layout width that the system reserves for the accessory, and then centers the accessory within.
- [tintColor](tintcolor.md) — The tint color to apply to the accessory.
- [style](style-swift.property.md) — The style of the outline disclosure accessory.
- [Style](style-swift.enum.md) — Constants that describe the style of the outline disclosure accessory.
