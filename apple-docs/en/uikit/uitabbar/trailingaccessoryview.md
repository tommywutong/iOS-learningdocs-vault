---
title: trailingAccessoryView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 13.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbar/trailingaccessoryview
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/trailingaccessoryview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/trailingaccessoryview.json'
content_hash: 'sha256:09f59dde8b33586d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBar](../uitabbar.md)

# trailingAccessoryView

<sub>Instance Property</sub>

The view at the trailing edge of a tab bar on tvOS.

<sub>tvOS</sub>

```swift
var trailingAccessoryView: UIView { get }
```

## Discussion

Use this property to integrate a custom view at the trailing edge of your tab bar interface. Use this view to display a custom logo or give access to custom accessories in your app.

## See Also

### Customizing tab bar appearance

- [standardAppearance](standardappearance.md) — The appearance settings for a standard-height tab bar.
- [scrollEdgeAppearance](scrolledgeappearance.md) — The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.
- [leadingAccessoryView](leadingaccessoryview.md) — The view at the leading edge of a tab bar on tvOS.
- [translucent](istranslucent.md) — A Boolean value that indicates whether the tab bar is translucent.
- [Legacy customizations](../uitabbar-legacy-customizations.md) — Customize appearance information directly on the tab bar object.
