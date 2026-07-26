---
title: isTranslucent
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitoolbar/istranslucent
source_url: 'https://developer.apple.com/documentation/uikit/uitoolbar/istranslucent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitoolbar/istranslucent.json'
content_hash: 'sha256:0b08e5aed30224c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolbar](../uitoolbar.md)

# isTranslucent

<sub>Instance Property</sub>

A Boolean value that indicates whether the toolbar is translucent.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isTranslucent: Bool { get set }
```

## Discussion

When the toolbar is translucent, configure the [edgesForExtendedLayout](../uiviewcontroller/edgesforextendedlayout.md) and [extendedLayoutIncludesOpaqueBars](../uiviewcontroller/extendedlayoutincludesopaquebars.md) properties of your view controller to display your content underneath the toolbar.

If the toolbar doesn’t have a custom background image, or if any pixel of the background image has an alpha value of less than `1.0`, the default value of this property is [true](../../swift/true.md). If the background image is completely opaque, the default value of this property is [false](../../swift/false.md). If you set this property to [true](../../swift/true.md) and the custom background image is completely opaque, UIKit applies a system-defined opacity of less than `1.0` to the image. If you set this property to [false](../../swift/false.md) and the background image isn’t opaque, UIKit adds an opaque backdrop.

## See Also

### Customizing appearance

- [standardAppearance](standardappearance.md) — The appearance settings to use for a standard-height toolbar.
- [compactAppearance](compactappearance.md) — The appearance settings to use for a compact-height toolbar.
- [scrollEdgeAppearance](scrolledgeappearance.md) — The appearance settings for a standard-height toolbar when the edge of scrollable content aligns with the edge of the toolbar.
- [compactScrollEdgeAppearance](compactscrolledgeappearance.md) — The appearance settings for a compact-height toolbar when the edge of any scrollable content aligns with the edge of a compact-height toolbar.
- [Legacy customizations](../uitoolbar-legacy-customizations.md) — Customize appearance information directly on the toolbar object.
