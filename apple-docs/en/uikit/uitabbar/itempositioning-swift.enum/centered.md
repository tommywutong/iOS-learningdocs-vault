---
title: UITabBar.ItemPositioning.centered
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbar/itempositioning-swift.enum/centered
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/itempositioning-swift.enum/centered'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/itempositioning-swift.enum/centered.json'
content_hash: 'sha256:7573ab49270dea5f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITabBar](../../uitabbar.md) · [ItemPositioning](../itempositioning-swift.enum.md)

# UITabBar.ItemPositioning.centered

<sub>Case</sub>

Center items in the available space.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case centered
```

## Discussion

With this option, the tab bar uses the [itemWidth](../itemwidth.md) and [itemSpacing](../itemspacing.md) properties to set the width of items and the spacing between items, positioning those items in the center of the available space. When the [UITabBarItemPositioningAutomatic](automatic.md) option is selected, the tab bar uses this behavior in horizontally regular environments.

## See Also

### Constants

- [UITabBarItemPositioningAutomatic](automatic.md) — Specifies automatic tab bar item positioning according to the user interface idiom, as follows:
- [UITabBarItemPositioningFill](fill.md) — Distribute items across the entire width of the tab bar.
