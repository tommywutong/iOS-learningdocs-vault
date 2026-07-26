---
title: itemPositioning
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbar/itempositioning-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/itempositioning-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/itempositioning-swift.property.json'
content_hash: 'sha256:496d9a0237cd3c1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBar](../uitabbar.md)

# itemPositioning

<sub>Instance Property</sub>

The positioning scheme for the tab bar items in the tab bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var itemPositioning: UITabBar.ItemPositioning { get set }
```

## Discussion

The default value for this property, [UITabBarItemPositioningAutomatic](itempositioning-swift.enum/automatic.md), results in the default tab bar item positioning according to the current environment:

- In a horizontally compact environment, the tab bar spreads items across the entire space, adjusting inter-item spacing as needed.
- In a horizontally regular environment, the tab bar uses the [itemWidth](itemwidth.md) and [itemSpacing](itemspacing.md) properties to set the width of items and the spacing between items, positioning those items in the center of the available space. This configuration has the potential to leave space along the left and right edges of the tab bar.

You can force a specific positioning scheme by changing the value of this property to a different value. For a list of possible values, see the constant descriptions for the [ItemPositioning](itempositioning-swift.enum.md) type.

## See Also

### Customizing item spacing

- [ItemPositioning](itempositioning-swift.enum.md) — Constants that specify tab bar item positioning.
- [itemSpacing](itemspacing.md) — The amount of space (in points) to use between tab bar items.
- [itemWidth](itemwidth.md) — The width (in points) of tab bar items.
