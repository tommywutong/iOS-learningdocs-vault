---
title: accessibilityIgnoresInvertColors
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentimageproperties/accessibilityignoresinvertcolors
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentimageproperties/accessibilityignoresinvertcolors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentimageproperties/accessibilityignoresinvertcolors.json'
content_hash: 'sha256:7910058a316c053e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentImageProperties](../uilistcontentimageproperties.md)

# accessibilityIgnoresInvertColors

<sub>Instance Property</sub>

A Boolean value that determines whether the image inverts its colors when the user turns on the Invert Colors accessibility setting.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) BOOL accessibilityIgnoresInvertColors;
```

## Discussion

If the value of this property is [true](../../swift/true.md), the image doesn’t invert its colors when the user turns on Invert Colors. The default value is [false](../../swift/false.md).

## See Also

### Configuring image properties

- [preferredSymbolConfiguration](preferredsymbolconfiguration.md) — The symbol configuration to use.
- [tintColor](tintcolor.md) — The tint color to apply to the image view.
- [tintColorTransformer](tintcolortransformer.md) — The color transformer for resolving the tint color.
- [resolvedTintColorForTintColor:](resolvedtintcolorfortintcolor_.md) — Generates the resolved tint color for the specified tint color, using the tint color and color transformer.
- [cornerRadius](cornerradius.md) — The preferred corner radius, using a continuous corner curve, for the image.
- [maximumSize](maximumsize.md) — The maximum size for the image.
- [reservedLayoutSize](reservedlayoutsize.md) — The layout size that the system reserves for the image, and then centers the image within.
- [UIListContentImageStandardDimension](../uilistcontentimagestandarddimension.md) — The system standard layout dimension for reserved layout size.
