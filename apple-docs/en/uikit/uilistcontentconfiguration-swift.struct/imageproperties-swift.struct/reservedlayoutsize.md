---
title: reservedLayoutSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/reservedlayoutsize
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/reservedlayoutsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/reservedlayoutsize.json'
content_hash: 'sha256:8250f8dffdf32d65'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIListContentConfiguration](../../uilistcontentconfiguration-swift.struct.md) · [ImageProperties](../imageproperties-swift.struct.md)

# reservedLayoutSize

<sub>Instance Property</sub>

The layout size that the system reserves for the image, and then centers the image within.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var reservedLayoutSize: CGSize { get set }
```

## Discussion

Use this property to ensure:

- Consistent horizontal alignment for images across adjacent content views, even when the images vary in width.
- Consistent height for content views, even when the images vary in height.

The reserved layout size only affects the amount of space for the image, and its positioning within that space. It doesn’t affect the size of the image.

The default value is [CGSizeZero](../../../coregraphics/cgsizezero.md). A width or height of zero means that the system uses the default behavior for that dimension:

- The system centers symbol images inside a predefined reserved layout size that scales with the content size category.
- Nonsymbol images use a reserved layout size equal to the actual size of the displayed image.

At Accessibility Dynamic Type sizes, content views ignore the reserved layout width. Content views ignore the reserved layout height when using the special Accessibility Dynamic Type layout where text wraps around the image.

## See Also

### Configuring image properties

- [preferredSymbolConfiguration](preferredsymbolconfiguration.md) — The symbol configuration to use.
- [tintColor](tintcolor.md) — The tint color to apply to the image view.
- [tintColorTransformer](tintcolortransformer.md) — The color transformer for resolving the tint color.
- [resolvedTintColor(for:)](<resolvedtintcolor(for_).md>) — Generates the resolved tint color for the specified tint color, using the tint color and color transformer.
- [cornerRadius](cornerradius.md) — The preferred corner radius, using a continuous corner curve, for the image.
- [maximumSize](maximumsize.md) — The maximum size for the image.
- [standardDimension](standarddimension.md) — The system standard layout dimension for reserved layout size.
- [accessibilityIgnoresInvertColors](accessibilityignoresinvertcolors.md) — A Boolean value that determines whether the image inverts its colors when the user turns on the Invert Colors accessibility setting.
