---
title: scrollEdgeAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationbar/scrolledgeappearance
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/scrolledgeappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/scrolledgeappearance.json'
content_hash: 'sha256:9cd4701d06e9b1e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# scrollEdgeAppearance

<sub>Instance Property</sub>

The appearance settings for the navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var scrollEdgeAppearance: UINavigationBarAppearance? { get set }
```

## Discussion

When a navigation controller contains a navigation bar and a scroll view, part of the scroll view’s content appears underneath the navigation bar. If the edge of the scrolled content reaches that bar, UIKit applies the appearance settings in this property.

If the value of this property is `nil`, UIKit uses the settings found in the [standardAppearance](standardappearance.md) property, modified to use a transparent background. If no navigation controller manages your navigation bar, UIKit ignores this property and uses the standard appearance of the navigation bar.

When running on apps that use iOS 14 or earlier, this property applies to navigation bars with large titles. In iOS 15, this property applies to all navigation bars.

## See Also

### Customizing the bar’s appearance

- [prefersLargeTitles](preferslargetitles.md) — A Boolean value that indicates whether the title displays in a large format.
- [standardAppearance](standardappearance.md) — The appearance settings for a standard-height navigation bar.
- [compactAppearance](compactappearance.md) — The appearance settings for a compact-height navigation bar.
- [compactScrollEdgeAppearance](compactscrolledgeappearance.md) — The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [translucent](istranslucent.md) — A Boolean value that indicates whether the navigation bar is translucent.
- [Legacy customizations](../uinavigationbar-legacy-customizations.md) — Customize appearance information directly on the navigation bar object.
