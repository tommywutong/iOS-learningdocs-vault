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
doc_path: /documentation/uikit/uinavigationbar/standardappearance
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/standardappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/standardappearance.json'
content_hash: 'sha256:32459dc0cdb6fe8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# standardAppearance

<sub>Instance Property</sub>

The appearance settings for a standard-height navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var standardAppearance: UINavigationBarAppearance { get set }
```

## Discussion

The default value of this property is an appearance object containing the system’s default appearance settings. You can customize the navigation bar appearance for specific navigation items with the [standardAppearance](../uinavigationitem/standardappearance.md) property of [UINavigationItem](../uinavigationitem.md).

## See Also

### Customizing the bar’s appearance

- [prefersLargeTitles](preferslargetitles.md) — A Boolean value that indicates whether the title displays in a large format.
- [compactAppearance](compactappearance.md) — The appearance settings for a compact-height navigation bar.
- [scrollEdgeAppearance](scrolledgeappearance.md) — The appearance settings for the navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [compactScrollEdgeAppearance](compactscrolledgeappearance.md) — The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [translucent](istranslucent.md) — A Boolean value that indicates whether the navigation bar is translucent.
- [Legacy customizations](../uinavigationbar-legacy-customizations.md) — Customize appearance information directly on the navigation bar object.
