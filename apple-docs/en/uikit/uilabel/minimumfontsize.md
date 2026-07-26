---
title: minimumFontSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（6.0 起废弃）, iPadOS 2.0+（6.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilabel/minimumfontsize
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/minimumfontsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/minimumfontsize.json'
content_hash: 'sha256:b70fc1188752b202'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# minimumFontSize

<sub>Instance Property</sub>

The size of the smallest permissible font when drawing the label’s text.

> [!warning] Deprecated
> Use [minimumScaleFactor](minimumscalefactor.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) CGFloat minimumFontSize;
```

## Discussion

When drawing text that might not fit within the bounding rectangle of the label, you can use this property to prevent the label from reducing the font size to a point where it’s no longer legible.

The default value for this property is `0.0`. If you enable font adjustment for the label, you should always increase this value. This property is effective only when the [numberOfLines](numberoflines.md) is `1`.

## See Also

### Sizing the label’s text

- [adjustsFontSizeToFitWidth](adjustsfontsizetofitwidth.md) — A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.
- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that determines whether the label tightens text before truncating.
- [baselineAdjustment](baselineadjustment.md) — An option that controls whether the text’s baseline remains fixed when text needs to shrink to fit in the label.
- [minimumScaleFactor](minimumscalefactor.md) — The minimum scale factor for the label’s text.
- [numberOfLines](numberoflines.md) — The maximum number of lines for rendering text.
- [sizingRule](../uiletterformawareadjusting/sizingrule.md) — The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.
- [adjustsLetterSpacingToFitWidth](adjustsletterspacingtofitwidth.md) — A Boolean value that indicates whether the label adjusts spacing between letters to fit the string within the label’s bounds rectangle. _(deprecated)_
