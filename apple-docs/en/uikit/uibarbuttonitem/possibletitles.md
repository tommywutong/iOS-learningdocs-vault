---
title: possibleTitles
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitem/possibletitles
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/possibletitles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/possibletitles.json'
content_hash: 'sha256:a3d723ee934e017f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# possibleTitles

<sub>Instance Property</sub>

The set of possible titles to display on the bar button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var possibleTitles: Set<String>? { get set }
```

## Discussion

Use this property to provide a hint to the system on how to correctly size the bar button item to be wide enough to accommodate your widest title. Set the value of this property to an [NSSet](../../foundation/nsset.md) object containing all the titles you intend as possible titles for the bar button item. Use the actual text strings you intend to display.

This property applies to bar button items placed on navigation bars or toolbars.

## See Also

### Customizing item appearance

- [style](style-swift.property.md) — The style of the item.
- [Style](style-swift.enum.md) — Constants that specify the style of an item.
- [tintColor](tintcolor.md) — The tint color to apply to the button item.
- [hidden](ishidden.md) — A Boolean that determines the visibility of the item.
- [selected](isselected.md) — A Boolean value that indicates whether the button is in a selected state.
- [width](width.md) — The width of the item.
