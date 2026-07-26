---
title: maximumSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/maximumsize
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/maximumsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/maximumsize.json'
content_hash: 'sha256:d9d22dbec23c1777'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIListContentConfiguration](../../uilistcontentconfiguration-swift.struct.md) · [ImageProperties](../imageproperties-swift.struct.md)

# maximumSize

<sub>Instance Property</sub>

The maximum size for the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var maximumSize: CGSize { get set }
```

## Discussion

The default value is [CGSizeZero](../../../coregraphics/cgsizezero.md). A width or height of zero means that the system doesn’t constrain the size for that dimension.

If the image exceeds this size on either dimension, the system reduces the size proportionately, maintaining the aspect ratio.

## See Also

### Configuring image properties

- [preferredSymbolConfiguration](preferredsymbolconfiguration.md) — The symbol configuration to use.
- [tintColor](tintcolor.md) — The tint color to apply to the image view.
- [tintColorTransformer](tintcolortransformer.md) — The color transformer for resolving the tint color.
- [resolvedTintColor(for:)](<resolvedtintcolor(for_).md>) — Generates the resolved tint color for the specified tint color, using the tint color and color transformer.
- [cornerRadius](cornerradius.md) — The preferred corner radius, using a continuous corner curve, for the image.
- [reservedLayoutSize](reservedlayoutsize.md) — The layout size that the system reserves for the image, and then centers the image within.
- [standardDimension](standarddimension.md) — The system standard layout dimension for reserved layout size.
- [accessibilityIgnoresInvertColors](accessibilityignoresinvertcolors.md) — A Boolean value that determines whether the image inverts its colors when the user turns on the Invert Colors accessibility setting.
