---
title: NSKernAttributeName
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nskernattributename
source_url: 'https://developer.apple.com/documentation/uikit/nskernattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nskernattributename.json'
content_hash: 'sha256:14718fb584685a82'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSKernAttributeName

<sub>Global Variable</sub>

The kerning of the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringKey const NSKernAttributeName;
```

## Discussion

The value of this attribute is an [NSNumber](../foundation/nsnumber.md) object containing a floating-point value. This value specifies the number of points by which to adjust kern-pair characters. Kerning prevents unwanted space from occurring between specific characters and depends on the font. The value `0` means kerning is disabled. The default value for this attribute is `0`.

## See Also

### Getting rendering attribute keys

- [NSBackgroundColorAttributeName](nsbackgroundcolorattributename.md) — The color of the background behind the text.
- [NSBaselineOffsetAttributeName](nsbaselineoffsetattributename.md) — The vertical offset for the position of the text.
- [NSFontAttributeName](nsfontattributename.md) — The font of the text.
- [NSForegroundColorAttributeName](nsforegroundcolorattributename.md) — The color of the text.
- [NSLigatureAttributeName](nsligatureattributename.md) — The ligature of the text.
- [NSParagraphStyleAttributeName](nsparagraphstyleattributename.md) — The paragraph style of the text.
- [NSStrikethroughColorAttributeName](nsstrikethroughcolorattributename.md) — The color of the strikethrough.
- [NSStrikethroughStyleAttributeName](nsstrikethroughstyleattributename.md) — The strikethrough style of the text.
- [NSStrokeColorAttributeName](nsstrokecolorattributename.md) — The color of the stroke.
- [NSStrokeWidthAttributeName](nsstrokewidthattributename.md) — The width of the stroke.
- [NSTrackingAttributeName](nstrackingattributename.md) — The amount to modify the default tracking.
- [NSUnderlineColorAttributeName](nsunderlinecolorattributename.md) — The color of the underline.
- [NSUnderlineStyleAttributeName](nsunderlinestyleattributename.md) — The underline style of the text.
- [NSWritingDirectionAttributeName](nswritingdirectionattributename.md) — The writing direction of the text.
