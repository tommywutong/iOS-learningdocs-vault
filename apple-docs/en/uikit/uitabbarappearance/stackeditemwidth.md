---
title: stackedItemWidth
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarappearance/stackeditemwidth
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarappearance/stackeditemwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarappearance/stackeditemwidth.json'
content_hash: 'sha256:1ff7e455c8c87993'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarAppearance](../uitabbarappearance.md)

# stackedItemWidth

<sub>Instance Property</sub>

The width of stacked items in the tab bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var stackedItemWidth: CGFloat { get set }
```

## Discussion

When the [stackedItemPositioning](stackeditempositioning.md) property is set to [UITabBarItemPositioningCentered](../uitabbar/itempositioning-swift.enum/centered.md), UIKit uses this property to set the width of each item. The default value of this property is `0`, which causes UIKit to use a system-defined width for items. For any values above `0`, UIKit uses the specified width, which is measured in points. If you try to assign a negative number to this property, UIKit sets the value to `0` instead.

## See Also

### Configuring stacked item appearances

- [stackedLayoutAppearance](stackedlayoutappearance.md) — The appearance attributes for items with a stacked layout.
- [stackedItemPositioning](stackeditempositioning.md) — The scheme to use when positioning stacked items within the tab bar.
- [stackedItemSpacing](stackeditemspacing.md) — The amount of space to insert between stacked tab bar items.
