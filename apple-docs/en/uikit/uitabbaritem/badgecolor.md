---
title: badgeColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbaritem/badgecolor
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritem/badgecolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritem/badgecolor.json'
content_hash: 'sha256:ef715877d524921e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarItem](../uitabbaritem.md)

# badgeColor

<sub>Instance Property</sub>

The background color of the item’s badge.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var badgeColor: UIColor? { get set }
```

## Discussion

The default value is `nil`. If you don’t specify a value, the item uses [systemRedColor](../uicolor/systemred.md).

## See Also

### Configuring the item’s badge

- [badgeValue](badgevalue.md) — The text that the item’s badge displays.
- [- setBadgeTextAttributes:forState:](<setbadgetextattributes(__for_).md>) — Registers text attributes that the badge uses for the specified state.
- [- badgeTextAttributesForState:](<badgetextattributes(for_).md>) — Returns the badge’s text attributes for the specified state.
