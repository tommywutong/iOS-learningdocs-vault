---
title: minimumScaleFactor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontenttextproperties/minimumscalefactor
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontenttextproperties/minimumscalefactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontenttextproperties/minimumscalefactor.json'
content_hash: 'sha256:06f51514db3a4c09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentTextProperties](../uilistcontenttextproperties.md)

# minimumScaleFactor

<sub>Instance Property</sub>

The smallest multiplier for the font size that the configuration uses to make the text fit.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) CGFloat minimumScaleFactor;
```

## Discussion

This value applies when [adjustsFontSizeToFitWidth](../uilistcontentconfiguration-swift.struct/textproperties-swift.struct/adjustsfontsizetofitwidth.md) is [true](../../swift/true.md).

## See Also

### Configuring text properties

- [font](font.md) — The font for the text.
- [color](color.md) — The color of the text.
- [colorTransformer](colortransformer.md) — The color transformer for resolving the text color.
- [resolvedColor](resolvedcolor.md) — Generates the resolved color for the specified color, using the text color and color transformer.
- [alignment](alignment.md) — The alignment for the text.
- [lineBreakMode](linebreakmode.md) — The line break mode to use for the text.
- [numberOfLines](numberoflines.md) — The maximum number of lines for the text.
- [adjustsFontSizeToFitWidth](adjustsfontsizetofitwidth.md) — A Boolean value that determines whether the configuration automatically adjusts the font size of the text when necessary to fit in the available width.
- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that determines whether the configuration tightens the text before truncating.
- [adjustsFontForContentSizeCategory](adjustsfontforcontentsizecategory.md) — A Boolean value that determines whether the configuration automatically updates the font when the content size category changes.
- [UIListContentTextAlignment](../uilistcontenttextalignment.md) — Constants that specify the visual alignment of the text.
- [transform](transform.md) — The transform to apply to the text.
- [UIListContentTextTransform](../uilistcontenttexttransform.md) — Constants that specify the transform to apply to the text.
- [showsExpansionTextWhenTruncated](showsexpansiontextwhentruncated.md) — A Boolean value that determines whether the full text displays when the pointer hovers over the truncated text.
