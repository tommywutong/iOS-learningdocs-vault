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
doc_path: /documentation/uikit/uitextview/font
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/font'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/font.json'
content_hash: 'sha256:bfeabc082b0df26e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# font

<sub>Instance Property</sub>

The font of the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var font: UIFont? { get set }
```

## Discussion

This property applies to the entire text string. The default value of this property is the body style of the system font.

> [!note] Note
> You can get information about the fonts available on the system using the methods of the [UIFont](../uifont.md) class.

In iOS 6 and later, assigning a new value to this property causes the new font to be applied to the entire contents of the text view. If you want to apply the font to only a portion of the text, you must create a new attributed string with the desired style information and assign it to the [attributedText](attributedtext.md) property.

## See Also

### Configuring appearance attributes

- [textColor](textcolor.md) — The color of the text.
- [textAlignment](textalignment.md) — The technique for aligning the text.
- [typingAttributes](typingattributes.md) — The attributes to apply to new text that the user enters.
- [linkTextAttributes](linktextattributes.md) — The attributes to apply to links.
- [borderStyle](borderstyle-swift.property.md) — The border style for the text field.
- [textHighlightAttributes](texthighlightattributes.md)
- [- drawTextHighlightBackgroundForTextRange:origin:](<drawtexthighlightbackground(for_origin_).md>)
- [BorderStyle](borderstyle-swift.enum.md) — The type of border around the text view.
