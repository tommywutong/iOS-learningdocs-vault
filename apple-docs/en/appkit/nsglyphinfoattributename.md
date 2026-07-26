---
title: NSGlyphInfoAttributeName
framework: AppKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsglyphinfoattributename
source_url: 'https://developer.apple.com/documentation/appkit/nsglyphinfoattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsglyphinfoattributename.json'
content_hash: 'sha256:999c69515ee2796c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSGlyphInfoAttributeName

<sub>Global Variable</sub>

The name of a glyph info object.

<sub>macOS</sub>

```objc
extern NSAttributedStringKey NSGlyphInfoAttributeName;
```

## Discussion

The [NSLayoutManager](nslayoutmanager.md) object assigns the glyph specified by this [NSGlyphInfo](nsglyphinfo.md) object to the entire attribute range, provided that its contents match the specified base string, and that the specified glyph is available in the font specified by `NSFontAttributeName`.

## See Also

### Getting rendering attribute keys

- [NSBackgroundColorAttributeName](nsbackgroundcolorattributename.md) — The color of the background behind the text.
- [NSBaselineOffsetAttributeName](nsbaselineoffsetattributename.md) — The vertical offset for the position of the text.
- [NSFontAttributeName](nsfontattributename.md) — The font of the text.
- [NSForegroundColorAttributeName](nsforegroundcolorattributename.md) — The color of the text.
- [NSKernAttributeName](nskernattributename.md) — The kerning of the text.
- [NSLigatureAttributeName](nsligatureattributename.md) — The ligature of the text.
- [NSParagraphStyleAttributeName](nsparagraphstyleattributename.md) — The paragraph style of the text.
- [NSStrikethroughColorAttributeName](nsstrikethroughcolorattributename.md) — The color of the strikethrough.
- [NSStrikethroughStyleAttributeName](nsstrikethroughstyleattributename.md) — The strikethrough style of the text.
- [NSStrokeColorAttributeName](nsstrokecolorattributename.md) — The color of the stroke.
- [NSStrokeWidthAttributeName](nsstrokewidthattributename.md) — The width of the stroke.
- [NSSuperscriptAttributeName](nssuperscriptattributename.md) — The superscript of the text.
- [NSTrackingAttributeName](nstrackingattributename.md) — The amount to modify the default tracking.
- [NSUnderlineColorAttributeName](nsunderlinecolorattributename.md) — The color of the underline.
- [NSUnderlineStyleAttributeName](nsunderlinestyleattributename.md) — The underline style of the text.
