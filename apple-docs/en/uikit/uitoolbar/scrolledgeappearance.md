---
title: scrollEdgeAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitoolbar/scrolledgeappearance
source_url: 'https://developer.apple.com/documentation/uikit/uitoolbar/scrolledgeappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitoolbar/scrolledgeappearance.json'
content_hash: 'sha256:c244683a3283c493'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolbar](../uitoolbar.md)

# scrollEdgeAppearance

<sub>Instance Property</sub>

The appearance settings for a standard-height toolbar when the edge of scrollable content aligns with the edge of the toolbar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var scrollEdgeAppearance: UIToolbarAppearance? { get set }
```

## Discussion

When a navigation controller contains a toolbar and a scroll view, part of the scroll view’s content appears underneath the toolbar. If the edge of the scrolled content reaches the toolbar, UIKit applies the appearance settings in this property.

This property applies to standard-height toolbars. If the value of this property is `nil`, UIKit uses the value of the [standardAppearance](standardappearance.md) property, modified to have a transparent background. If no navigation controller manages your toolbar, UIKit ignores this property and uses the tool bar’s standard appearance.

## See Also

### Customizing appearance

- [standardAppearance](standardappearance.md) — The appearance settings to use for a standard-height toolbar.
- [compactAppearance](compactappearance.md) — The appearance settings to use for a compact-height toolbar.
- [compactScrollEdgeAppearance](compactscrolledgeappearance.md) — The appearance settings for a compact-height toolbar when the edge of any scrollable content aligns with the edge of a compact-height toolbar.
- [translucent](istranslucent.md) — A Boolean value that indicates whether the toolbar is translucent.
- [Legacy customizations](../uitoolbar-legacy-customizations.md) — Customize appearance information directly on the toolbar object.
