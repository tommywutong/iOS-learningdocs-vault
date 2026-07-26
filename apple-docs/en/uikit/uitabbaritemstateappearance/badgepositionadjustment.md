---
title: badgePositionAdjustment
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbaritemstateappearance/badgepositionadjustment
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritemstateappearance/badgepositionadjustment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritemstateappearance/badgepositionadjustment.json'
content_hash: 'sha256:453ed69b0d361646'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarItemStateAppearance](../uitabbaritemstateappearance.md)

# badgePositionAdjustment

<sub>Instance Property</sub>

The additional amount by which to offset the badge horizontally and vertically.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var badgePositionAdjustment: UIOffset { get set }
```

## Discussion

Use this property to specify the distance, in points, by which to offset the badge from its default position over its item. Positive values move the title down and to the right. Negative values move the title up and to the left.

## See Also

### Configuring the badge appearance

- [badgeTextAttributes](badgetextattributes.md) — String attributes to apply to the text of the item’s badge.
- [badgeBackgroundColor](badgebackgroundcolor.md) — The background color of the badge.
- [badgeTitlePositionAdjustment](badgetitlepositionadjustment.md) — The additional amount by which to offset the badge’s title horizontally and vertically.
