---
title: UIListContentConfiguration.TextProperties
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-swift.struct/textproperties-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/textproperties-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-swift.struct/textproperties-swift.struct.json'
content_hash: 'sha256:eb73fb8d3deb8fb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentConfiguration](../uilistcontentconfiguration-swift.struct.md)

# UIListContentConfiguration.TextProperties

<sub>Structure</sub>

Properties that affect the list content configuration’s text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct TextProperties
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomReflectable](../../swift/customreflectable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md)

## Topics

### Configuring text properties

- [font](textproperties-swift.struct/font.md) — The font for the text.
- [color](textproperties-swift.struct/color.md) — The color of the text.
- [colorTransformer](textproperties-swift.struct/colortransformer.md) — The color transformer for resolving the text color.
- [resolvedColor()](<textproperties-swift.struct/resolvedcolor().md>) — Generates the resolved color for the specified color, using the text color and color transformer.
- [alignment](textproperties-swift.struct/alignment.md) — The alignment for the text.
- [lineBreakMode](textproperties-swift.struct/linebreakmode.md) — The line break mode to use for the text.
- [numberOfLines](textproperties-swift.struct/numberoflines.md) — The maximum number of lines for the text.
- [adjustsFontSizeToFitWidth](textproperties-swift.struct/adjustsfontsizetofitwidth.md) — A Boolean value that determines whether the configuration automatically adjusts the font size of the text when necessary to fit in the available width.
- [minimumScaleFactor](textproperties-swift.struct/minimumscalefactor.md) — The smallest multiplier for the font size that the configuration uses to make the text fit.
- [allowsDefaultTighteningForTruncation](textproperties-swift.struct/allowsdefaulttighteningfortruncation.md) — A Boolean value that determines whether the configuration tightens the text before truncating.
- [adjustsFontForContentSizeCategory](textproperties-swift.struct/adjustsfontforcontentsizecategory.md) — A Boolean value that determines whether the configuration automatically updates the font when the content size category changes.
- [TextAlignment](textproperties-swift.struct/textalignment.md) — Constants that specify the visual alignment of the text.
- [transform](textproperties-swift.struct/transform.md) — The transform to apply to the text.
- [TextTransform](textproperties-swift.struct/texttransform.md) — Constants that specify the transform to apply to the text.
- [showsExpansionTextWhenTruncated](textproperties-swift.struct/showsexpansiontextwhentruncated.md) — A Boolean value that determines whether the full text displays when the pointer hovers over the truncated text.

## See Also

### Customizing appearance

- [imageProperties](imageproperties-swift.property.md) — Properties for configuring the image.
- [textProperties](textproperties-swift.property.md) — Properties for configuring the primary text.
- [secondaryTextProperties](secondarytextproperties.md) — Properties for configuring the secondary text.
- [ImageProperties](imageproperties-swift.struct.md) — Properties that affect the list content configuration’s image.
