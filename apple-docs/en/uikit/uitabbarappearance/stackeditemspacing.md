---
title: stackedItemSpacing
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarappearance/stackeditemspacing
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarappearance/stackeditemspacing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarappearance/stackeditemspacing.json'
content_hash: 'sha256:16de44f070fad39a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarAppearance](../uitabbarappearance.md)

# stackedItemSpacing

<sub>Instance Property</sub>

The amount of space to insert between stacked tab bar items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var stackedItemSpacing: CGFloat { get set }
```

## Discussion

When the [stackedItemPositioning](stackeditempositioning.md) property is set to [UITabBarItemPositioningCentered](../uitabbar/itempositioning-swift.enum/centered.md), UIKit uses this property to determine how much space to insert between the items. The default value of this property is `0`, which causes UIKit to insert a system-defined default space between items. For any values above `0`, UIKit inserts the specified amount of space, measured in points, between the items. If you try to assign a negative number to this property, UIKit sets the value to `0` instead.

## See Also

### Configuring stacked item appearances

- [stackedLayoutAppearance](stackedlayoutappearance.md) — The appearance attributes for items with a stacked layout.
- [stackedItemPositioning](stackeditempositioning.md) — The scheme to use when positioning stacked items within the tab bar.
- [stackedItemWidth](stackeditemwidth.md) — The width of stacked items in the tab bar.
