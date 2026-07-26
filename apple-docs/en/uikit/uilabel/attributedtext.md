---
title: attributedText
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilabel/attributedtext
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/attributedtext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/attributedtext.json'
content_hash: 'sha256:2a32dcdf4bc55989'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# attributedText

<sub>Instance Property</sub>

The styled text that the label displays.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var attributedText: NSAttributedString? { get set }
```

## Discussion

This property is `nil` by default.

Assigning a new value to this property also replaces the value of the [text](text.md) property with the same string data, although without any formatting information. In addition, assigning a new value updates the values in the [font](font.md), [textColor](textcolor.md), and other style-related properties so that they reflect the style information starting at location `0` in the attributed string.

Turn autokerning on for the label by setting the [NSKernAttributeName](../nskernattributename.md) of the string to [null](../../foundation/nsnull/null.md).

## See Also

### Accessing the text attributes

- [text](text.md) — The text that the label displays.
- [font](font.md) — The font of the text.
- [textColor](textcolor.md) — The color of the text.
- [textAlignment](textalignment.md) — The technique for aligning the text.
- [lineBreakMode](linebreakmode.md) — The technique for wrapping and truncating the label’s text.
- [lineBreakStrategy](linebreakstrategy.md) — The strategy that the system uses to break lines when laying out multiple lines of text.
- [enabled](isenabled.md) — A Boolean value that determines whether the label draws its text in an enabled state.
- [enablesMarqueeWhenAncestorFocused](enablesmarqueewhenancestorfocused.md) — A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.
- [showsExpansionTextWhenTruncated](showsexpansiontextwhentruncated.md) — A Boolean value that determines whether the full text of the label displays when the pointer hovers over the truncated text.
