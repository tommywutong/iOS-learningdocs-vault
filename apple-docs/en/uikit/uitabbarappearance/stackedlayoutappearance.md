---
title: stackedLayoutAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarappearance/stackedlayoutappearance
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarappearance/stackedlayoutappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarappearance/stackedlayoutappearance.json'
content_hash: 'sha256:603d930cf352bf26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarAppearance](../uitabbarappearance.md)

# stackedLayoutAppearance

<sub>Instance Property</sub>

The appearance attributes for items with a stacked layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var stackedLayoutAppearance: UITabBarItemAppearance { get set }
```

## Discussion

If you didn’t provide a set of explicit attributes at initialization time, UIKit provides an object with default attributes.

## See Also

### Configuring stacked item appearances

- [stackedItemPositioning](stackeditempositioning.md) — The scheme to use when positioning stacked items within the tab bar.
- [stackedItemSpacing](stackeditemspacing.md) — The amount of space to insert between stacked tab bar items.
- [stackedItemWidth](stackeditemwidth.md) — The width of stacked items in the tab bar.
