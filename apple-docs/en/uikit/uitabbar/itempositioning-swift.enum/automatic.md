---
title: UITabBar.ItemPositioning.automatic
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbar/itempositioning-swift.enum/automatic
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/itempositioning-swift.enum/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/itempositioning-swift.enum/automatic.json'
content_hash: 'sha256:4a3ef37d7ca4ae7f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITabBar](../../uitabbar.md) · [ItemPositioning](../itempositioning-swift.enum.md)

# UITabBar.ItemPositioning.automatic

<sub>Case</sub>

Specifies automatic tab bar item positioning according to the user interface idiom, as follows:

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case automatic
```

## Discussion

- In a horizontally compact environment, the tab bar spreads items across the entire space, adjusting inter-item spacing as needed.
- In a horizontally regular environment, the tab bar uses the [itemWidth](../itemwidth.md) and [itemSpacing](../itemspacing.md) properties to set the width of items and the spacing between items, positioning those items in the center of the available space. This configuration has the potential to leave space along the left and right edges of the tab bar.

## See Also

### Constants

- [UITabBarItemPositioningFill](fill.md) — Distribute items across the entire width of the tab bar.
- [UITabBarItemPositioningCentered](centered.md) — Center items in the available space.
