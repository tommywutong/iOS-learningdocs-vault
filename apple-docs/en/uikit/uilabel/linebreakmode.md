---
title: lineBreakMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilabel/linebreakmode
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/linebreakmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/linebreakmode.json'
content_hash: 'sha256:b0efbd13ba220b73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# lineBreakMode

<sub>Instance Property</sub>

The technique for wrapping and truncating the label’s text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var lineBreakMode: NSLineBreakMode { get set }
```

## Discussion

If you aren’t using styled text, this property applies to the entire text string in the [text](text.md) property. If you’re using styled text, assigning a new value to this property applies the line break mode to the entirety of the string in the [attributedText](attributedtext.md) property. To apply the line break mode to only a portion of the text, create a new attributed string with the desired style information and associate it with the label. However, [NSParagraphStyle](../nsparagraphstyle.md) properties, such as those defined by [NSLineBreakMode](../nslinebreakmode.md), apply to entire paragraphs (as defined for [paragraphRange(for:)](<../../foundation/nsstring/paragraphrange(for_).md>)), not words within paragraphs.

This property is in effect both during normal drawing and in cases where the label must reduce the font size to fit the text in its bounding box. The default value of this property is [NSLineBreakByTruncatingTail](../nslinebreakmode/bytruncatingtail.md).

## See Also

### Related Documentation

- [adjustsFontSizeToFitWidth](adjustsfontsizetofitwidth.md) — A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.

### Accessing the text attributes

- [text](text.md) — The text that the label displays.
- [attributedText](attributedtext.md) — The styled text that the label displays.
- [font](font.md) — The font of the text.
- [textColor](textcolor.md) — The color of the text.
- [textAlignment](textalignment.md) — The technique for aligning the text.
- [lineBreakStrategy](linebreakstrategy.md) — The strategy that the system uses to break lines when laying out multiple lines of text.
- [enabled](isenabled.md) — A Boolean value that determines whether the label draws its text in an enabled state.
- [enablesMarqueeWhenAncestorFocused](enablesmarqueewhenancestorfocused.md) — A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.
- [showsExpansionTextWhenTruncated](showsexpansiontextwhentruncated.md) — A Boolean value that determines whether the full text of the label displays when the pointer hovers over the truncated text.
