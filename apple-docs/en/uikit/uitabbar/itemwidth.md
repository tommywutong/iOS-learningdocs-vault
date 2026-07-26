---
title: itemWidth
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbar/itemwidth
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/itemwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/itemwidth.json'
content_hash: 'sha256:ad3e3ae88e90da5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBar](../uitabbar.md)

# itemWidth

<sub>Instance Property</sub>

The width (in points) of tab bar items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var itemWidth: CGFloat { get set }
```

## Discussion

When the tab bar positions items using the [UITabBarItemPositioningCentered](itempositioning-swift.enum/centered.md) option, it checks the value of this property to see if a custom width value has been supplied. The default value of this property is `0`, which causes the tab bar to use a system-defined default width for each item. Specifying a value greater than `0` causes the tab bar to use your custom value instead. If you try to set this property to a negative value, the tab bar sets the value to `0` instead.

## See Also

### Customizing item spacing

- [itemPositioning](itempositioning-swift.property.md) — The positioning scheme for the tab bar items in the tab bar.
- [ItemPositioning](itempositioning-swift.enum.md) — Constants that specify tab bar item positioning.
- [itemSpacing](itemspacing.md) — The amount of space (in points) to use between tab bar items.
