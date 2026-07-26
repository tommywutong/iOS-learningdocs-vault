---
title: textColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/textcolor
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/textcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/textcolor.json'
content_hash: 'sha256:6d95efaa903fac7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# textColor

<sub>Instance Property</sub>

The color of the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var textColor: UIColor? { get set }
```

## Discussion

This property applies to the entire text string. The default text color is black.

In iOS 6 and later, assigning a new value to this property causes the new text color to be applied to the entire contents of the text view. If you want to apply the color to only a portion of the text, you must create a new attributed string with the desired style information and assign it to the [attributedText](attributedtext.md) property.

## See Also

### Related Documentation

- [backgroundColor](../uiview/backgroundcolor.md) — The view’s background color.

### Configuring appearance attributes

- [font](font.md) — The font of the text.
- [textAlignment](textalignment.md) — The technique for aligning the text.
- [typingAttributes](typingattributes.md) — The attributes to apply to new text that the user enters.
- [linkTextAttributes](linktextattributes.md) — The attributes to apply to links.
- [borderStyle](borderstyle-swift.property.md) — The border style for the text field.
- [textHighlightAttributes](texthighlightattributes.md)
- [- drawTextHighlightBackgroundForTextRange:origin:](<drawtexthighlightbackground(for_origin_).md>)
- [BorderStyle](borderstyle-swift.enum.md) — The type of border around the text view.
