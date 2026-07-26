---
title: NSParagraphStyleAttributeName
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsparagraphstyleattributename
source_url: 'https://developer.apple.com/documentation/uikit/nsparagraphstyleattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsparagraphstyleattributename.json'
content_hash: 'sha256:408968d4ed26f59b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSParagraphStyleAttributeName

<sub>Global Variable</sub>

The paragraph style of the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringKey const NSParagraphStyleAttributeName;
```

## Discussion

The value of this attribute is an [NSParagraphStyle](nsparagraphstyle.md) object. Use this attribute to apply multiple attributes to a range of text. If you do not specify this attribute, the string uses the default paragraph attributes, as returned by the [defaultParagraphStyle](nsparagraphstyle/default.md) method of [NSParagraphStyle](nsparagraphstyle.md).

## See Also

### Getting rendering attribute keys

- [NSBackgroundColorAttributeName](nsbackgroundcolorattributename.md) — The color of the background behind the text.
- [NSBaselineOffsetAttributeName](nsbaselineoffsetattributename.md) — The vertical offset for the position of the text.
- [NSFontAttributeName](nsfontattributename.md) — The font of the text.
- [NSForegroundColorAttributeName](nsforegroundcolorattributename.md) — The color of the text.
- [NSKernAttributeName](nskernattributename.md) — The kerning of the text.
- [NSLigatureAttributeName](nsligatureattributename.md) — The ligature of the text.
- [NSStrikethroughColorAttributeName](nsstrikethroughcolorattributename.md) — The color of the strikethrough.
- [NSStrikethroughStyleAttributeName](nsstrikethroughstyleattributename.md) — The strikethrough style of the text.
- [NSStrokeColorAttributeName](nsstrokecolorattributename.md) — The color of the stroke.
- [NSStrokeWidthAttributeName](nsstrokewidthattributename.md) — The width of the stroke.
- [NSTrackingAttributeName](nstrackingattributename.md) — The amount to modify the default tracking.
- [NSUnderlineColorAttributeName](nsunderlinecolorattributename.md) — The color of the underline.
- [NSUnderlineStyleAttributeName](nsunderlinestyleattributename.md) — The underline style of the text.
- [NSWritingDirectionAttributeName](nswritingdirectionattributename.md) — The writing direction of the text.
