---
title: defaultTextAttributes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/defaulttextattributes
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/defaulttextattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/defaulttextattributes.json'
content_hash: 'sha256:2e5a9970df676599'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# defaultTextAttributes

<sub>Instance Property</sub>

The default attributes to apply to the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var defaultTextAttributes: [NSAttributedString.Key : Any] { get set }
```

## Discussion

By default, this property returns a dictionary of text attributes with default values.

Setting this property applies the specified attributes to the entire text of the text field. Unset attributes maintain their default values.

Getting this property returns the previously set attributes, which may have been modified by setting properties such as [font](font.md) and [textColor](textcolor.md).

## See Also

### Configuring the text attributes

- [text](text.md) — The text that the text field displays.
- [attributedText](attributedtext.md) — The styled text that the text field displays.
- [placeholder](placeholder.md) — The string that displays when there is no other text in the text field.
- [attributedPlaceholder](attributedplaceholder.md) — The styled string that displays when there is no other text in the text field.
- [font](font.md) — The font of the text.
- [textColor](textcolor.md) — The color of the text.
- [textAlignment](textalignment.md) — The technique for aligning the text.
- [typingAttributes](typingattributes.md) — The attributes to apply to new text that the user enters.
- [BorderStyle](borderstyle-swift.enum.md) — The type of border around the text field.
