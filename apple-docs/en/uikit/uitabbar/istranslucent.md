---
title: isTranslucent
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbar/istranslucent
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/istranslucent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/istranslucent.json'
content_hash: 'sha256:5058518f158d74a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBar](../uitabbar.md)

# isTranslucent

<sub>Instance Property</sub>

A Boolean value that indicates whether the tab bar is translucent.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isTranslucent: Bool { get set }
```

## Discussion

When the tab bar is translucent, configure the [edgesForExtendedLayout](../uiviewcontroller/edgesforextendedlayout.md) and [extendedLayoutIncludesOpaqueBars](../uiviewcontroller/extendedlayoutincludesopaquebars.md) properties of your view controller to display your content underneath the tab bar.

If the tab bar doesn’t have a custom background image, or if any pixel of the background image has an alpha value of less than `1.0`, the default value of this property is [true](../../swift/true.md). If the background image is completely opaque, the default value of this property is [false](../../swift/false.md). If you set this property to [true](../../swift/true.md) and the custom background image is completely opaque, UIKit applies a system-defined opacity of less than `1.0` to the image. If you set this property to [false](../../swift/false.md) and the background image is not opaque, UIKit adds an opaque backdrop.

## See Also

### Customizing tab bar appearance

- [standardAppearance](standardappearance.md) — The appearance settings for a standard-height tab bar.
- [scrollEdgeAppearance](scrolledgeappearance.md) — The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.
- [leadingAccessoryView](leadingaccessoryview.md) — The view at the leading edge of a tab bar on tvOS.
- [trailingAccessoryView](trailingaccessoryview.md) — The view at the trailing edge of a tab bar on tvOS.
- [Legacy customizations](../uitabbar-legacy-customizations.md) — Customize appearance information directly on the tab bar object.
