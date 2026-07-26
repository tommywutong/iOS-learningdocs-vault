---
title: textAlignment
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/textalignment
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/textalignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/textalignment.json'
content_hash: 'sha256:4c4a233efe4d2be5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# textAlignment

<sub>Instance Property</sub>

The technique for aligning the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var textAlignment: NSTextAlignment { get set }
```

## Discussion

This property applies to the entire text string. The default value of this property is [NSTextAlignmentNatural](../nstextalignment/natural.md).

Assigning a new value to this property causes the new text alignment to be applied to the entire contents of the text view. If you want to apply the alignment to only a portion of the text, you must create a new attributed string with the desired style information and assign it to the [attributedText](attributedtext.md) property.

## See Also

### Configuring appearance attributes

- [font](font.md) — The font of the text.
- [textColor](textcolor.md) — The color of the text.
- [typingAttributes](typingattributes.md) — The attributes to apply to new text that the user enters.
- [linkTextAttributes](linktextattributes.md) — The attributes to apply to links.
- [borderStyle](borderstyle-swift.property.md) — The border style for the text field.
- [textHighlightAttributes](texthighlightattributes.md)
- [- drawTextHighlightBackgroundForTextRange:origin:](<drawtexthighlightbackground(for_origin_).md>)
- [BorderStyle](borderstyle-swift.enum.md) — The type of border around the text view.
