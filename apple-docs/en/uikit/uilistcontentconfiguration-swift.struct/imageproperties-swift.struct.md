---
title: UIListContentConfiguration.ImageProperties
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct.json'
content_hash: 'sha256:54e4ebec07c3a5a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentConfiguration](../uilistcontentconfiguration-swift.struct.md)

# UIListContentConfiguration.ImageProperties

<sub>Structure</sub>

Properties that affect the list content configuration’s image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct ImageProperties
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomReflectable](../../swift/customreflectable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md)

## Topics

### Configuring image properties

- [preferredSymbolConfiguration](imageproperties-swift.struct/preferredsymbolconfiguration.md) — The symbol configuration to use.
- [tintColor](imageproperties-swift.struct/tintcolor.md) — The tint color to apply to the image view.
- [tintColorTransformer](imageproperties-swift.struct/tintcolortransformer.md) — The color transformer for resolving the tint color.
- [resolvedTintColor(for:)](<imageproperties-swift.struct/resolvedtintcolor(for_).md>) — Generates the resolved tint color for the specified tint color, using the tint color and color transformer.
- [cornerRadius](imageproperties-swift.struct/cornerradius.md) — The preferred corner radius, using a continuous corner curve, for the image.
- [maximumSize](imageproperties-swift.struct/maximumsize.md) — The maximum size for the image.
- [reservedLayoutSize](imageproperties-swift.struct/reservedlayoutsize.md) — The layout size that the system reserves for the image, and then centers the image within.
- [standardDimension](imageproperties-swift.struct/standarddimension.md) — The system standard layout dimension for reserved layout size.
- [accessibilityIgnoresInvertColors](imageproperties-swift.struct/accessibilityignoresinvertcolors.md) — A Boolean value that determines whether the image inverts its colors when the user turns on the Invert Colors accessibility setting.

### Instance Properties

- [strokeColor](imageproperties-swift.struct/strokecolor.md)
- [strokeColorTransformer](imageproperties-swift.struct/strokecolortransformer.md)
- [strokeWidth](imageproperties-swift.struct/strokewidth.md)

### Instance Methods

- [resolvedStrokeColor(for:)](<imageproperties-swift.struct/resolvedstrokecolor(for_).md>)

## See Also

### Customizing appearance

- [imageProperties](imageproperties-swift.property.md) — Properties for configuring the image.
- [textProperties](textproperties-swift.property.md) — Properties for configuring the primary text.
- [secondaryTextProperties](secondarytextproperties.md) — Properties for configuring the secondary text.
- [TextProperties](textproperties-swift.struct.md) — Properties that affect the list content configuration’s text.
