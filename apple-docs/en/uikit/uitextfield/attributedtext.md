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
doc_path: /documentation/uikit/uitextfield/attributedtext
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/attributedtext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/attributedtext.json'
content_hash: 'sha256:517ec5e9d71a2003'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# attributedText

<sub>Instance Property</sub>

The styled text that the text field displays.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var attributedText: NSAttributedString? { get set }
```

## Discussion

This property is `nil` by default. Assigning a new value to this property also replaces the value of the [text](text.md) property with the same string data, albeit without any formatting information. In addition, assigning a new value updates the values in the [font](font.md), [textColor](textcolor.md), and other style-related properties so that they reflect the style information starting at location `0` in the attributed string.

## See Also

### Configuring the text attributes

- [text](text.md) — The text that the text field displays.
- [placeholder](placeholder.md) — The string that displays when there is no other text in the text field.
- [attributedPlaceholder](attributedplaceholder.md) — The styled string that displays when there is no other text in the text field.
- [defaultTextAttributes](defaulttextattributes.md) — The default attributes to apply to the text.
- [font](font.md) — The font of the text.
- [textColor](textcolor.md) — The color of the text.
- [textAlignment](textalignment.md) — The technique for aligning the text.
- [typingAttributes](typingattributes.md) — The attributes to apply to new text that the user enters.
- [BorderStyle](borderstyle-swift.enum.md) — The type of border around the text field.
