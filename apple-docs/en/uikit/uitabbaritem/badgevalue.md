---
title: badgeValue
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbaritem/badgevalue
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritem/badgevalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritem/badgevalue.json'
content_hash: 'sha256:90dca63437ecb109'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarItem](../uitabbaritem.md)

# badgeValue

<sub>Instance Property</sub>

The text that the item’s badge displays.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var badgeValue: String? { get set }
```

## Discussion

The default value is `nil`.

## See Also

### Configuring the item’s badge

- [badgeColor](badgecolor.md) — The background color of the item’s badge.
- [- setBadgeTextAttributes:forState:](<setbadgetextattributes(__for_).md>) — Registers text attributes that the badge uses for the specified state.
- [- badgeTextAttributesForState:](<badgetextattributes(for_).md>) — Returns the badge’s text attributes for the specified state.
