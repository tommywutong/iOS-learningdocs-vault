---
title: UIListContentTextProperties
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontenttextproperties
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontenttextproperties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontenttextproperties.json'
content_hash: 'sha256:7123886d856ef82a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIListContentTextProperties

<sub>Class</sub>

Properties that affect the list content configuration’s text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UIListContentTextProperties : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Configuring text properties

- [font](uilistcontenttextproperties/font.md) — The font for the text.
- [color](uilistcontenttextproperties/color.md) — The color of the text.
- [colorTransformer](uilistcontenttextproperties/colortransformer.md) — The color transformer for resolving the text color.
- [resolvedColor](uilistcontenttextproperties/resolvedcolor.md) — Generates the resolved color for the specified color, using the text color and color transformer.
- [alignment](uilistcontenttextproperties/alignment.md) — The alignment for the text.
- [lineBreakMode](uilistcontenttextproperties/linebreakmode.md) — The line break mode to use for the text.
- [numberOfLines](uilistcontenttextproperties/numberoflines.md) — The maximum number of lines for the text.
- [adjustsFontSizeToFitWidth](uilistcontenttextproperties/adjustsfontsizetofitwidth.md) — A Boolean value that determines whether the configuration automatically adjusts the font size of the text when necessary to fit in the available width.
- [minimumScaleFactor](uilistcontenttextproperties/minimumscalefactor.md) — The smallest multiplier for the font size that the configuration uses to make the text fit.
- [allowsDefaultTighteningForTruncation](uilistcontenttextproperties/allowsdefaulttighteningfortruncation.md) — A Boolean value that determines whether the configuration tightens the text before truncating.
- [adjustsFontForContentSizeCategory](uilistcontenttextproperties/adjustsfontforcontentsizecategory.md) — A Boolean value that determines whether the configuration automatically updates the font when the content size category changes.
- [UIListContentTextAlignment](uilistcontenttextalignment.md) — Constants that specify the visual alignment of the text.
- [transform](uilistcontenttextproperties/transform.md) — The transform to apply to the text.
- [UIListContentTextTransform](uilistcontenttexttransform.md) — Constants that specify the transform to apply to the text.
- [showsExpansionTextWhenTruncated](uilistcontenttextproperties/showsexpansiontextwhentruncated.md) — A Boolean value that determines whether the full text displays when the pointer hovers over the truncated text.

## See Also

### Customizing appearance

- [imageProperties](uilistcontentconfiguration-c.class/imageproperties.md) — Properties for configuring the image.
- [textProperties](uilistcontentconfiguration-c.class/textproperties.md) — Properties for configuring the primary text.
- [secondaryTextProperties](uilistcontentconfiguration-c.class/secondarytextproperties.md) — Properties for configuring the secondary text.
- [UIListContentImageProperties](uilistcontentimageproperties.md) — Properties that affect the list content configuration’s image.
