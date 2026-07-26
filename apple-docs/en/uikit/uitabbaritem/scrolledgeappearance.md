---
title: scrollEdgeAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbaritem/scrolledgeappearance
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritem/scrolledgeappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritem/scrolledgeappearance.json'
content_hash: 'sha256:a08faeb4332fd8c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarItem](../uitabbaritem.md)

# scrollEdgeAppearance

<sub>Instance Property</sub>

The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var scrollEdgeAppearance: UITabBarAppearance? { get set }
```

## Discussion

When a tab bar displays the selected item, the appearance setting in this property overrides the settings in the [scrollEdgeAppearance](../uitoolbar/scrolledgeappearance.md) property of [UIToolbar](../uitoolbar.md).

Use this property to apply a scroll edge appearance based on the tab bar item stored in the [selectedItem](../uitabbar/selecteditem.md) property. If the selected item’s [scrollEdgeAppearance](scrolledgeappearance.md) property is `nil`, UIKit uses the tab bar’s scroll edge appearance.

## See Also

### Configuring the item’s appearance

- [selectedImage](selectedimage.md) — The source image the item uses to generate its selected image.
- [standardAppearance](standardappearance.md) — The appearance settings for a tab bar.
- [titlePositionAdjustment](titlepositionadjustment.md) — The offset to apply to the title’s position.
