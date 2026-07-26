---
title: attributedPlaceholder
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/attributedplaceholder
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/attributedplaceholder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/attributedplaceholder.json'
content_hash: 'sha256:f316f12f93c3979c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# attributedPlaceholder

<sub>Instance Property</sub>

The styled string that displays when there is no other text in the text field.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var attributedPlaceholder: NSAttributedString? { get set }
```

## Discussion

This property is `nil` by default. If set, the placeholder string is drawn using system-defined color and the remaining style information (except the text color) of the attributed string. Assigning a new value to this property also replaces the value of the [placeholder](placeholder.md) property with the same string data, albeit without any formatting information. Assigning a new value to this property does not affect any other style-related properties of the text field.

## See Also

### Configuring the text attributes

- [text](text.md) — The text that the text field displays.
- [attributedText](attributedtext.md) — The styled text that the text field displays.
- [placeholder](placeholder.md) — The string that displays when there is no other text in the text field.
- [defaultTextAttributes](defaulttextattributes.md) — The default attributes to apply to the text.
- [font](font.md) — The font of the text.
- [textColor](textcolor.md) — The color of the text.
- [textAlignment](textalignment.md) — The technique for aligning the text.
- [typingAttributes](typingattributes.md) — The attributes to apply to new text that the user enters.
- [BorderStyle](borderstyle-swift.enum.md) — The type of border around the text field.
