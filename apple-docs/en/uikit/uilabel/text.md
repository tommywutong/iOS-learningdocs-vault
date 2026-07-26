---
title: text
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilabel/text
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/text'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/text.json'
content_hash: 'sha256:1ae5886317af1a90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# text

<sub>Instance Property</sub>

The text that the label displays.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var text: String? { get set }
```

## Discussion

This property is `nil` by default. Assigning a new value to this property also replaces the value of the [attributedText](attributedtext.md) property with the same text, although without any inherent style attributes. Instead the label styles the new string using [shadowColor](shadowcolor.md), [textAlignment](textalignment.md), and other style-related properties of the class.

## See Also

### Accessing the text attributes

- [attributedText](attributedtext.md) — The styled text that the label displays.
- [font](font.md) — The font of the text.
- [textColor](textcolor.md) — The color of the text.
- [textAlignment](textalignment.md) — The technique for aligning the text.
- [lineBreakMode](linebreakmode.md) — The technique for wrapping and truncating the label’s text.
- [lineBreakStrategy](linebreakstrategy.md) — The strategy that the system uses to break lines when laying out multiple lines of text.
- [enabled](isenabled.md) — A Boolean value that determines whether the label draws its text in an enabled state.
- [enablesMarqueeWhenAncestorFocused](enablesmarqueewhenancestorfocused.md) — A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.
- [showsExpansionTextWhenTruncated](showsexpansiontextwhentruncated.md) — A Boolean value that determines whether the full text of the label displays when the pointer hovers over the truncated text.
