---
title: 'resolvedTintColor(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/resolvedtintcolor(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/resolvedtintcolor(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/resolvedtintcolor%28for%3A%29.json'
content_hash: 'sha256:be5026c77c9146b6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIListContentConfiguration](../../uilistcontentconfiguration-swift.struct.md) · [ImageProperties](../imageproperties-swift.struct.md)

# resolvedTintColor(for:)

<sub>Instance Method</sub>

Generates the resolved tint color for the specified tint color, using the tint color and color transformer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func resolvedTintColor(for tintColor: UIColor) -> UIColor
```

## Discussion

The resulting color depends on [tintColor](tintcolor.md) and [tintColorTransformer](tintcolortransformer.md).

## See Also

### Configuring image properties

- [preferredSymbolConfiguration](preferredsymbolconfiguration.md) — The symbol configuration to use.
- [tintColor](tintcolor.md) — The tint color to apply to the image view.
- [tintColorTransformer](tintcolortransformer.md) — The color transformer for resolving the tint color.
- [cornerRadius](cornerradius.md) — The preferred corner radius, using a continuous corner curve, for the image.
- [maximumSize](maximumsize.md) — The maximum size for the image.
- [reservedLayoutSize](reservedlayoutsize.md) — The layout size that the system reserves for the image, and then centers the image within.
- [standardDimension](standarddimension.md) — The system standard layout dimension for reserved layout size.
- [accessibilityIgnoresInvertColors](accessibilityignoresinvertcolors.md) — A Boolean value that determines whether the image inverts its colors when the user turns on the Invert Colors accessibility setting.
