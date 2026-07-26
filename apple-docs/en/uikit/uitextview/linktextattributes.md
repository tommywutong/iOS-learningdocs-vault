---
title: linkTextAttributes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/linktextattributes
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/linktextattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/linktextattributes.json'
content_hash: 'sha256:b5089a3705fb1df6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# linkTextAttributes

<sub>Instance Property</sub>

The attributes to apply to links.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var linkTextAttributes: [NSAttributedString.Key : Any]! { get set }
```

## Discussion

The default attributes specify blue text with a single underline and the pointing hand cursor.

## See Also

### Configuring appearance attributes

- [font](font.md) — The font of the text.
- [textColor](textcolor.md) — The color of the text.
- [textAlignment](textalignment.md) — The technique for aligning the text.
- [typingAttributes](typingattributes.md) — The attributes to apply to new text that the user enters.
- [borderStyle](borderstyle-swift.property.md) — The border style for the text field.
- [textHighlightAttributes](texthighlightattributes.md)
- [- drawTextHighlightBackgroundForTextRange:origin:](<drawtexthighlightbackground(for_origin_).md>)
- [BorderStyle](borderstyle-swift.enum.md) — The type of border around the text view.
