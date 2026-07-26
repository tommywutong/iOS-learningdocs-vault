---
title: badgeTextAttributes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbaritemstateappearance/badgetextattributes
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritemstateappearance/badgetextattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritemstateappearance/badgetextattributes.json'
content_hash: 'sha256:ae737c18f3f00022'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarItemStateAppearance](../uitabbaritemstateappearance.md)

# badgeTextAttributes

<sub>Instance Property</sub>

String attributes to apply to the text of the item’s badge.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var badgeTextAttributes: [NSAttributedString.Key : Any] { get set }
```

## Discussion

If you don’t specify font or color attributes for the text, UIKit supplies appropriate default values. For a list of possible keys, see [NSAttributedString.Key](../../foundation/nsattributedstring/key.md).

## See Also

### Configuring the badge appearance

- [badgeBackgroundColor](badgebackgroundcolor.md) — The background color of the badge.
- [badgeTitlePositionAdjustment](badgetitlepositionadjustment.md) — The additional amount by which to offset the badge’s title horizontally and vertically.
- [badgePositionAdjustment](badgepositionadjustment.md) — The additional amount by which to offset the badge horizontally and vertically.
