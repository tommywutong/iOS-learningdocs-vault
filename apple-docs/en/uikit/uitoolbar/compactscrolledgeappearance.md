---
title: compactScrollEdgeAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitoolbar/compactscrolledgeappearance
source_url: 'https://developer.apple.com/documentation/uikit/uitoolbar/compactscrolledgeappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitoolbar/compactscrolledgeappearance.json'
content_hash: 'sha256:8aa5e4911ef02c95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolbar](../uitoolbar.md)

# compactScrollEdgeAppearance

<sub>Instance Property</sub>

The appearance settings for a compact-height toolbar when the edge of any scrollable content aligns with the edge of a compact-height toolbar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var compactScrollEdgeAppearance: UIToolbarAppearance? { get set }
```

## Discussion

When a navigation controller contains a toolbar and a scroll view, part of the scroll view’s content appears underneath the toolbar. If the edge of the scrolled content reaches the toolbar, UIKit applies the appearance settings in this property.

This property applies to compact-height toolbars. If the value of this property is `nil`, UIKit uses the value of the [scrollEdgeAppearance](scrolledgeappearance.md) property. If no navigation controller manages your toolbar, UIKit ignores this property and uses the value of the [compactAppearance](compactappearance.md) property.

## See Also

### Customizing appearance

- [standardAppearance](standardappearance.md) — The appearance settings to use for a standard-height toolbar.
- [compactAppearance](compactappearance.md) — The appearance settings to use for a compact-height toolbar.
- [scrollEdgeAppearance](scrolledgeappearance.md) — The appearance settings for a standard-height toolbar when the edge of scrollable content aligns with the edge of the toolbar.
- [translucent](istranslucent.md) — A Boolean value that indicates whether the toolbar is translucent.
- [Legacy customizations](../uitoolbar-legacy-customizations.md) — Customize appearance information directly on the toolbar object.
