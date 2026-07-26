---
title: compactScrollEdgeAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationbar/compactscrolledgeappearance
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/compactscrolledgeappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/compactscrolledgeappearance.json'
content_hash: 'sha256:98ead3d93accb1cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# compactScrollEdgeAppearance

<sub>Instance Property</sub>

The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var compactScrollEdgeAppearance: UINavigationBarAppearance? { get set }
```

## Discussion

When a navigation controller contains a navigation bar and a scroll view, part of the scroll view’s content appears underneath the navigation bar. If the edge of the scrolled content reaches that bar, UIKit applies the appearance settings in this property.

This property applies to compact-height navigation bars. If the value of this property is `nil`, UIKit uses the value of the [scrollEdgeAppearance](scrolledgeappearance.md) of the navigation bar. If no navigation controller manages your navigation bar, UIKit ignores this property and uses the [compactAppearance](compactappearance.md) of the navigation bar.

You can customize the appearance of the navigation bar based on the top navigation item with the [compactScrollEdgeAppearance](../uinavigationitem/compactscrolledgeappearance.md) property of [UINavigationItem](../uinavigationitem.md).

## See Also

### Customizing the bar’s appearance

- [prefersLargeTitles](preferslargetitles.md) — A Boolean value that indicates whether the title displays in a large format.
- [standardAppearance](standardappearance.md) — The appearance settings for a standard-height navigation bar.
- [compactAppearance](compactappearance.md) — The appearance settings for a compact-height navigation bar.
- [scrollEdgeAppearance](scrolledgeappearance.md) — The appearance settings for the navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [translucent](istranslucent.md) — A Boolean value that indicates whether the navigation bar is translucent.
- [Legacy customizations](../uinavigationbar-legacy-customizations.md) — Customize appearance information directly on the navigation bar object.
