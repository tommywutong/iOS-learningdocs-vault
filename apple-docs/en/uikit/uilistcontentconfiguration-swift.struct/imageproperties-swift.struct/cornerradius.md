---
title: cornerRadius
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/cornerradius
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/cornerradius'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/cornerradius.json'
content_hash: 'sha256:37c9ba4e6adeb9ad'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIListContentConfiguration](../../uilistcontentconfiguration-swift.struct.md) · [ImageProperties](../imageproperties-swift.struct.md)

# cornerRadius

<sub>Instance Property</sub>

The preferred corner radius, using a continuous corner curve, for the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var cornerRadius: CGFloat { get set }
```

## Discussion

If the image is too small to fit the requested radius, the system adjusts the corner curve and radius.

## See Also

### Configuring image properties

- [preferredSymbolConfiguration](preferredsymbolconfiguration.md) — The symbol configuration to use.
- [tintColor](tintcolor.md) — The tint color to apply to the image view.
- [tintColorTransformer](tintcolortransformer.md) — The color transformer for resolving the tint color.
- [resolvedTintColor(for:)](<resolvedtintcolor(for_).md>) — Generates the resolved tint color for the specified tint color, using the tint color and color transformer.
- [maximumSize](maximumsize.md) — The maximum size for the image.
- [reservedLayoutSize](reservedlayoutsize.md) — The layout size that the system reserves for the image, and then centers the image within.
- [standardDimension](standarddimension.md) — The system standard layout dimension for reserved layout size.
- [accessibilityIgnoresInvertColors](accessibilityignoresinvertcolors.md) — A Boolean value that determines whether the image inverts its colors when the user turns on the Invert Colors accessibility setting.
