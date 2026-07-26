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
doc_path: /documentation/uikit/uitextfield/font
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/font'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/font.json'
content_hash: 'sha256:abf20f74fab6fa54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# font

<sub>Instance Property</sub>

The font of the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var font: UIFont? { get set }
```

## Discussion

This property applies to the entire text of the text field. It also applies to the placeholder text. The default value of this property is the body style of the system font.

Assigning a new value to this property causes the font to be applied to the entire string in the [attributedText](attributedtext.md) and [attributedPlaceholder](attributedplaceholder.md) properties. If you want to apply the font to only a portion of the text, create a new attributed string with the desired style information and associate it with the text field.

## See Also

### Configuring the text attributes

- [text](text.md) — The text that the text field displays.
- [attributedText](attributedtext.md) — The styled text that the text field displays.
- [placeholder](placeholder.md) — The string that displays when there is no other text in the text field.
- [attributedPlaceholder](attributedplaceholder.md) — The styled string that displays when there is no other text in the text field.
- [defaultTextAttributes](defaulttextattributes.md) — The default attributes to apply to the text.
- [textColor](textcolor.md) — The color of the text.
- [textAlignment](textalignment.md) — The technique for aligning the text.
- [typingAttributes](typingattributes.md) — The attributes to apply to new text that the user enters.
- [BorderStyle](borderstyle-swift.enum.md) — The type of border around the text field.
