---
title: enablesMarqueeWhenAncestorFocused
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 12.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilabel/enablesmarqueewhenancestorfocused
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/enablesmarqueewhenancestorfocused'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/enablesmarqueewhenancestorfocused.json'
content_hash: 'sha256:c0c83c14afc3cdbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# enablesMarqueeWhenAncestorFocused

<sub>Instance Property</sub>

A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.

<sub>tvOS</sub>

```swift
var enablesMarqueeWhenAncestorFocused: Bool { get set }
```

## Discussion

If this value is [true](../../swift/true.md), then the label ignores [lineBreakMode](linebreakmode.md), [adjustsFontSizeToFitWidth](adjustsfontsizetofitwidth.md), and [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md). The label scrolls its text when any ancestor in its view hierarchy has focus.

The default value for this property is [false](../../swift/false.md).

## See Also

### Accessing the text attributes

- [text](text.md) — The text that the label displays.
- [attributedText](attributedtext.md) — The styled text that the label displays.
- [font](font.md) — The font of the text.
- [textColor](textcolor.md) — The color of the text.
- [textAlignment](textalignment.md) — The technique for aligning the text.
- [lineBreakMode](linebreakmode.md) — The technique for wrapping and truncating the label’s text.
- [lineBreakStrategy](linebreakstrategy.md) — The strategy that the system uses to break lines when laying out multiple lines of text.
- [enabled](isenabled.md) — A Boolean value that determines whether the label draws its text in an enabled state.
- [showsExpansionTextWhenTruncated](showsexpansiontextwhentruncated.md) — A Boolean value that determines whether the full text of the label displays when the pointer hovers over the truncated text.
