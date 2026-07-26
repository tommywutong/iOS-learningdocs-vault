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
doc_path: /documentation/uikit/uitabbar/standardappearance
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/standardappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/standardappearance.json'
content_hash: 'sha256:f15c03f962cd3a35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBar](../uitabbar.md)

# standardAppearance

<sub>Instance Property</sub>

The appearance settings for a standard-height tab bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var standardAppearance: UITabBarAppearance { get set }
```

## Discussion

The default value of this property is an appearance object containing the system’s default appearance settings.

## See Also

### Customizing tab bar appearance

- [scrollEdgeAppearance](scrolledgeappearance.md) — The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.
- [leadingAccessoryView](leadingaccessoryview.md) — The view at the leading edge of a tab bar on tvOS.
- [trailingAccessoryView](trailingaccessoryview.md) — The view at the trailing edge of a tab bar on tvOS.
- [translucent](istranslucent.md) — A Boolean value that indicates whether the tab bar is translucent.
- [Legacy customizations](../uitabbar-legacy-customizations.md) — Customize appearance information directly on the tab bar object.
