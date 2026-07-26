---
title: isTranslucent
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationbar/istranslucent
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/istranslucent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/istranslucent.json'
content_hash: 'sha256:209bd3ef6e0c1204'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# isTranslucent

<sub>Instance Property</sub>

A Boolean value that indicates whether the navigation bar is translucent.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isTranslucent: Bool { get set }
```

## Discussion

When the navigation bar is translucent, configure the [edgesForExtendedLayout](../uiviewcontroller/edgesforextendedlayout.md) and [extendedLayoutIncludesOpaqueBars](../uiviewcontroller/extendedlayoutincludesopaquebars.md) properties of your view controller to display your content underneath the navigation bar.

If the navigation bar doesn’t have a custom background image, or if any pixel of the background image has an alpha value of less than `1.0`, the default value of this property is [true](../../swift/true.md). If the background image is completely opaque, the default value of this property is [false](../../swift/false.md). If you set this property to [true](../../swift/true.md) and the custom background image is completely opaque, UIKit applies a system-defined opacity of less than `1.0` to the image. If you set this property to [false](../../swift/false.md) and the background image is not opaque, UIKit adds an opaque backdrop.

## See Also

### Customizing the bar’s appearance

- [prefersLargeTitles](preferslargetitles.md) — A Boolean value that indicates whether the title displays in a large format.
- [standardAppearance](standardappearance.md) — The appearance settings for a standard-height navigation bar.
- [compactAppearance](compactappearance.md) — The appearance settings for a compact-height navigation bar.
- [scrollEdgeAppearance](scrolledgeappearance.md) — The appearance settings for the navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [compactScrollEdgeAppearance](compactscrolledgeappearance.md) — The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [Legacy customizations](../uinavigationbar-legacy-customizations.md) — Customize appearance information directly on the navigation bar object.
