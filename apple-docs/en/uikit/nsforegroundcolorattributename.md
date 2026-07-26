---
title: NSForegroundColorAttributeName
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsforegroundcolorattributename
source_url: 'https://developer.apple.com/documentation/uikit/nsforegroundcolorattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsforegroundcolorattributename.json'
content_hash: 'sha256:46a8f1c53804f73e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSForegroundColorAttributeName

<sub>Global Variable</sub>

The color of the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringKey const NSForegroundColorAttributeName;
```

## Discussion

In macOS, the value of this attribute is an [NSColor](../appkit/nscolor.md) instance. In iOS, tvOS, watchOS, and Mac Catalyst, the value of this attribute is a [UIColor](uicolor.md) instance. Use this attribute to specify the color of the text during rendering. If you don’t specify this attribute, the text renders in black.

## See Also

### Getting rendering attribute keys

- [NSBackgroundColorAttributeName](nsbackgroundcolorattributename.md) — The color of the background behind the text.
- [NSBaselineOffsetAttributeName](nsbaselineoffsetattributename.md) — The vertical offset for the position of the text.
- [NSFontAttributeName](nsfontattributename.md) — The font of the text.
- [NSKernAttributeName](nskernattributename.md) — The kerning of the text.
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
