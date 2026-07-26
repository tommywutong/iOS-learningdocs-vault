---
title: leadingAccessoryView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 13.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbar/leadingaccessoryview
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/leadingaccessoryview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/leadingaccessoryview.json'
content_hash: 'sha256:d7a1dd1982fdd6be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBar](../uitabbar.md)

# leadingAccessoryView

<sub>Instance Property</sub>

The view at the leading edge of a tab bar on tvOS.

<sub>tvOS</sub>

```swift
var leadingAccessoryView: UIView { get }
```

## Discussion

Use this property to integrate a custom view at the leading edge of your tab bar interface. Use this view to display a custom logo or give access to custom accessories in your app.

## See Also

### Customizing tab bar appearance

- [standardAppearance](standardappearance.md) — The appearance settings for a standard-height tab bar.
- [scrollEdgeAppearance](scrolledgeappearance.md) — The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.
- [trailingAccessoryView](trailingaccessoryview.md) — The view at the trailing edge of a tab bar on tvOS.
- [translucent](istranslucent.md) — A Boolean value that indicates whether the tab bar is translucent.
- [Legacy customizations](../uitabbar-legacy-customizations.md) — Customize appearance information directly on the tab bar object.
