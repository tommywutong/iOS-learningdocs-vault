---
title: resolvedColor
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontenttextproperties/resolvedcolor
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontenttextproperties/resolvedcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontenttextproperties/resolvedcolor.json'
content_hash: 'sha256:19236b3b2fff1eb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentTextProperties](../uilistcontenttextproperties.md)

# resolvedColor

<sub>Instance Method</sub>

Generates the resolved color for the specified color, using the text color and color transformer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (UIColor *) resolvedColor;
```

## Discussion

The resulting color depends on [color](../uilistcontentconfiguration-swift.struct/textproperties-swift.struct/color.md) and [colorTransformer](../uilistcontentconfiguration-swift.struct/textproperties-swift.struct/colortransformer.md).

## See Also

### Configuring text properties

- [font](font.md) — The font for the text.
- [color](color.md) — The color of the text.
- [colorTransformer](colortransformer.md) — The color transformer for resolving the text color.
- [alignment](alignment.md) — The alignment for the text.
- [lineBreakMode](linebreakmode.md) — The line break mode to use for the text.
- [numberOfLines](numberoflines.md) — The maximum number of lines for the text.
- [adjustsFontSizeToFitWidth](adjustsfontsizetofitwidth.md) — A Boolean value that determines whether the configuration automatically adjusts the font size of the text when necessary to fit in the available width.
- [minimumScaleFactor](minimumscalefactor.md) — The smallest multiplier for the font size that the configuration uses to make the text fit.
- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that determines whether the configuration tightens the text before truncating.
- [adjustsFontForContentSizeCategory](adjustsfontforcontentsizecategory.md) — A Boolean value that determines whether the configuration automatically updates the font when the content size category changes.
- [UIListContentTextAlignment](../uilistcontenttextalignment.md) — Constants that specify the visual alignment of the text.
- [transform](transform.md) — The transform to apply to the text.
- [UIListContentTextTransform](../uilistcontenttexttransform.md) — Constants that specify the transform to apply to the text.
- [showsExpansionTextWhenTruncated](showsexpansiontextwhentruncated.md) — A Boolean value that determines whether the full text displays when the pointer hovers over the truncated text.
