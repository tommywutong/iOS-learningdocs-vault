---
title: tintColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/tintcolor
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/tintcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/tintcolor.json'
content_hash: 'sha256:1299821fb3b541fe'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIListContentConfiguration](../../uilistcontentconfiguration-swift.struct.md) · [ImageProperties](../imageproperties-swift.struct.md)

# tintColor

<sub>Instance Property</sub>

The tint color to apply to the image view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var tintColor: UIColor? { get set }
```

## Discussion

The default value of this property is `nil`, which means that the image view uses its inherited tint color.

## See Also

### Configuring image properties

- [preferredSymbolConfiguration](preferredsymbolconfiguration.md) — The symbol configuration to use.
- [tintColorTransformer](tintcolortransformer.md) — The color transformer for resolving the tint color.
- [resolvedTintColor(for:)](<resolvedtintcolor(for_).md>) — Generates the resolved tint color for the specified tint color, using the tint color and color transformer.
- [cornerRadius](cornerradius.md) — The preferred corner radius, using a continuous corner curve, for the image.
- [maximumSize](maximumsize.md) — The maximum size for the image.
- [reservedLayoutSize](reservedlayoutsize.md) — The layout size that the system reserves for the image, and then centers the image within.
- [standardDimension](standarddimension.md) — The system standard layout dimension for reserved layout size.
- [accessibilityIgnoresInvertColors](accessibilityignoresinvertcolors.md) — A Boolean value that determines whether the image inverts its colors when the user turns on the Invert Colors accessibility setting.
