---
title: normal
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbaritemappearance/normal
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritemappearance/normal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritemappearance/normal.json'
content_hash: 'sha256:59ee10feb4abcbdc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarItemAppearance](../uitabbaritemappearance.md)

# normal

<sub>Instance Property</sub>

The appearance data to apply to the tab bar item when it’s enabled, unselected, and not the focused item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var normal: UITabBarItemStateAppearance { get }
```

## Discussion

To set the attributes for this state, get the object in this property and modify it.

## See Also

### Configuring attributes for different item states

- [selected](selected.md) — The appearance data to apply to the tab bar item when it’s selected.
- [disabled](disabled.md) — The appearance data to apply to the tab bar item when it’s disabled.
- [focused](focused.md) — The appearance data to apply to the tab bar item when it’s focused.
