---
title: font
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilabel/font
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/font'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/font.json'
content_hash: 'sha256:54ea74f1ddfcd73b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# font

<sub>Instance Property</sub>

The font of the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var font: UIFont! { get set }
```

## Discussion

If you’re using styled text, assigning a new value to this property applies the font to the entirety of the string in the [attributedText](attributedtext.md) property. If you want to apply the font to only a portion of the text, create a new attributed string with the desired style information and associate it with the label. If you aren’t using styled text, this property applies to the entire text string in the [text](text.md) property.

The default value for this property is the system font at a size of 17 points (using the [+ systemFontOfSize:](<../uifont/systemfont(ofsize_).md>) class method of [UIFont](../uifont.md)). Setting this property to `nil` causes it to be reset to the default value.

## See Also

### Accessing the text attributes

- [text](text.md) — The text that the label displays.
- [attributedText](attributedtext.md) — The styled text that the label displays.
- [textColor](textcolor.md) — The color of the text.
- [textAlignment](textalignment.md) — The technique for aligning the text.
- [lineBreakMode](linebreakmode.md) — The technique for wrapping and truncating the label’s text.
- [lineBreakStrategy](linebreakstrategy.md) — The strategy that the system uses to break lines when laying out multiple lines of text.
- [enabled](isenabled.md) — A Boolean value that determines whether the label draws its text in an enabled state.
- [enablesMarqueeWhenAncestorFocused](enablesmarqueewhenancestorfocused.md) — A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.
- [showsExpansionTextWhenTruncated](showsexpansiontextwhentruncated.md) — A Boolean value that determines whether the full text of the label displays when the pointer hovers over the truncated text.
