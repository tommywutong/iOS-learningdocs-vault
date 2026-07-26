---
title: standardAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbaritem/standardappearance
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritem/standardappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritem/standardappearance.json'
content_hash: 'sha256:a6068ccc91fd2a51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarItem](../uitabbaritem.md)

# standardAppearance

<sub>Instance Property</sub>

The appearance settings for a tab bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var standardAppearance: UITabBarAppearance? { get set }
```

## Discussion

When a tab bar displays the selected item, the appearance setting in this property overrides the settings in the [standardAppearance](../uitabbar/standardappearance.md) property of [UITabBar](../uitabbar.md).

Use this property to apply a tab bar appearance based on the tab bar item stored in the [selectedItem](../uitabbar/selecteditem.md) property. If the selected item’s [standardAppearance](standardappearance.md) property is `nil`, UIKit uses the tab bar’s standard appearance.

## See Also

### Configuring the item’s appearance

- [selectedImage](selectedimage.md) — The source image the item uses to generate its selected image.
- [scrollEdgeAppearance](scrolledgeappearance.md) — The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.
- [titlePositionAdjustment](titlepositionadjustment.md) — The offset to apply to the title’s position.
