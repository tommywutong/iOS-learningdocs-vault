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
doc_path: /documentation/uikit/uitextfield/text
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/text'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/text.json'
content_hash: 'sha256:60d054e5f953964f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# text

<sub>Instance Property</sub>

The text that the text field displays.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var text: String? { get set }
```

## Discussion

Assigning a new value to this property also replaces the value of the [attributedText](attributedtext.md) property with the same text, albeit without any inherent style attributes. Instead the text view styles the new string using the [font](font.md), [textColor](textcolor.md), and other style-related properties of the class.

This value is `nil` by default.

## See Also

### Configuring the text attributes

- [attributedText](attributedtext.md) — The styled text that the text field displays.
- [placeholder](placeholder.md) — The string that displays when there is no other text in the text field.
- [attributedPlaceholder](attributedplaceholder.md) — The styled string that displays when there is no other text in the text field.
- [defaultTextAttributes](defaulttextattributes.md) — The default attributes to apply to the text.
- [font](font.md) — The font of the text.
- [textColor](textcolor.md) — The color of the text.
- [textAlignment](textalignment.md) — The technique for aligning the text.
- [typingAttributes](typingattributes.md) — The attributes to apply to new text that the user enters.
- [BorderStyle](borderstyle-swift.enum.md) — The type of border around the text field.
