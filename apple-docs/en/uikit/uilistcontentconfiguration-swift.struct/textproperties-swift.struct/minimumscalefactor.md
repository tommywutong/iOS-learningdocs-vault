---
title: minimumScaleFactor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-swift.struct/textproperties-swift.struct/minimumscalefactor
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/textproperties-swift.struct/minimumscalefactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-swift.struct/textproperties-swift.struct/minimumscalefactor.json'
content_hash: 'sha256:cd4eef8026873727'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIListContentConfiguration](../../uilistcontentconfiguration-swift.struct.md) · [TextProperties](../textproperties-swift.struct.md)

# minimumScaleFactor

<sub>Instance Property</sub>

The smallest multiplier for the font size that the configuration uses to make the text fit.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var minimumScaleFactor: CGFloat { get set }
```

## Discussion

This value applies when [adjustsFontSizeToFitWidth](adjustsfontsizetofitwidth.md) is [true](../../../swift/true.md).

## See Also

### Configuring text properties

- [font](font.md) — The font for the text.
- [color](color.md) — The color of the text.
- [colorTransformer](colortransformer.md) — The color transformer for resolving the text color.
- [resolvedColor()](<resolvedcolor().md>) — Generates the resolved color for the specified color, using the text color and color transformer.
- [alignment](alignment.md) — The alignment for the text.
- [lineBreakMode](linebreakmode.md) — The line break mode to use for the text.
- [numberOfLines](numberoflines.md) — The maximum number of lines for the text.
- [adjustsFontSizeToFitWidth](adjustsfontsizetofitwidth.md) — A Boolean value that determines whether the configuration automatically adjusts the font size of the text when necessary to fit in the available width.
- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that determines whether the configuration tightens the text before truncating.
- [adjustsFontForContentSizeCategory](adjustsfontforcontentsizecategory.md) — A Boolean value that determines whether the configuration automatically updates the font when the content size category changes.
- [TextAlignment](textalignment.md) — Constants that specify the visual alignment of the text.
- [transform](transform.md) — The transform to apply to the text.
- [TextTransform](texttransform.md) — Constants that specify the transform to apply to the text.
- [showsExpansionTextWhenTruncated](showsexpansiontextwhentruncated.md) — A Boolean value that determines whether the full text displays when the pointer hovers over the truncated text.
