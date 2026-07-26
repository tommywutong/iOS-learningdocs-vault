---
title: lineBreakStrategy
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilabel/linebreakstrategy
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/linebreakstrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/linebreakstrategy.json'
content_hash: 'sha256:2b5c17e5a2e56e0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# lineBreakStrategy

<sub>Instance Property</sub>

The strategy that the system uses to break lines when laying out multiple lines of text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy { get set }
```

## Discussion

The default value is [NSLineBreakStrategyStandard](../nsparagraphstyle/linebreakstrategy-swift.struct/standard.md).

> [!note] Note
> When the label has an attributed string value, the system ignores the [textColor](textcolor.md), [font](font.md), [textAlignment](textalignment.md), [lineBreakMode](linebreakmode.md), and [lineBreakStrategy](linebreakstrategy.md) properties. Set the [NSForegroundColorAttributeName](../nsforegroundcolorattributename.md), [NSFontAttributeName](../nsfontattributename.md), [alignment](../nsmutableparagraphstyle/alignment.md), [lineBreakMode](../nsparagraphstyle/linebreakmode.md), and [lineBreakStrategy](../nsparagraphstyle/linebreakstrategy-swift.property.md) properties in the attributed string instead.

## See Also

### Accessing the text attributes

- [text](text.md) — The text that the label displays.
- [attributedText](attributedtext.md) — The styled text that the label displays.
- [font](font.md) — The font of the text.
- [textColor](textcolor.md) — The color of the text.
- [textAlignment](textalignment.md) — The technique for aligning the text.
- [lineBreakMode](linebreakmode.md) — The technique for wrapping and truncating the label’s text.
- [enabled](isenabled.md) — A Boolean value that determines whether the label draws its text in an enabled state.
- [enablesMarqueeWhenAncestorFocused](enablesmarqueewhenancestorfocused.md) — A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.
- [showsExpansionTextWhenTruncated](showsexpansiontextwhentruncated.md) — A Boolean value that determines whether the full text of the label displays when the pointer hovers over the truncated text.
