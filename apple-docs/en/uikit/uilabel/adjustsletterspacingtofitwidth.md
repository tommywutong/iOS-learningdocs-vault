---
title: adjustsLetterSpacingToFitWidth
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（7.0 起废弃）, iPadOS 6.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilabel/adjustsletterspacingtofitwidth
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/adjustsletterspacingtofitwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/adjustsletterspacingtofitwidth.json'
content_hash: 'sha256:0e2c695dc7f6301b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# adjustsLetterSpacingToFitWidth

<sub>Instance Property</sub>

A Boolean value that indicates whether the label adjusts spacing between letters to fit the string within the label’s bounds rectangle.

> [!warning] Deprecated
> Hand tune instead by using [NSKernAttributeName](../nskernattributename.md) to affect tracking.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) BOOL adjustsLetterSpacingToFitWidth;
```

## Discussion

When this property is [true](../../swift/true.md), the label may alter the letter spacing of the text to make that text fit better within the label’s bounds. The label applies letter spacing to the text regardless of the current line break mode. The default value of this property is [false](../../swift/false.md).

If this property’s value is [true](../../swift/true.md), the label to ignore values value returned by the [tighteningFactorForTruncation](../../appkit/nsparagraphstyle/tighteningfactorfortruncation.md) method of any [NSParagraphStyle](../nsparagraphstyle.md) objects associated with the label text.

> [!important] Important
> If this property’s value is [true](../../swift/true.md), it’s a programmer error to set the [lineBreakMode](linebreakmode.md) property to a value that causes text to wrap to another line.

## See Also

### Sizing the label’s text

- [adjustsFontSizeToFitWidth](adjustsfontsizetofitwidth.md) — A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.
- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that determines whether the label tightens text before truncating.
- [baselineAdjustment](baselineadjustment.md) — An option that controls whether the text’s baseline remains fixed when text needs to shrink to fit in the label.
- [minimumScaleFactor](minimumscalefactor.md) — The minimum scale factor for the label’s text.
- [numberOfLines](numberoflines.md) — The maximum number of lines for rendering text.
- [sizingRule](../uiletterformawareadjusting/sizingrule.md) — The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.
- [minimumFontSize](minimumfontsize.md) — The size of the smallest permissible font when drawing the label’s text. _(deprecated)_
