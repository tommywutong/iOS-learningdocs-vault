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
doc_path: /documentation/uikit/uitextfield/textcolor
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/textcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/textcolor.json'
content_hash: 'sha256:6b0a1e8d3462baf8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# textColor

<sub>Instance Property</sub>

The color of the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var textColor: UIColor? { get set }
```

## Discussion

This property applies to the entire text string. The default value for this property is a black color. The value for the property can only be set to a non-`nil` value; setting this property to `nil` raises an exception.

If you are using styled text, assigning a new value to this property causes the text color to be applied to the entire string in the [attributedText](attributedtext.md) property. If you want to apply the color to only a portion of the text, create a new attributed string with the desired style information and associate it with the text field.

## See Also

### Configuring the text attributes

- [text](text.md) — The text that the text field displays.
- [attributedText](attributedtext.md) — The styled text that the text field displays.
- [placeholder](placeholder.md) — The string that displays when there is no other text in the text field.
- [attributedPlaceholder](attributedplaceholder.md) — The styled string that displays when there is no other text in the text field.
- [defaultTextAttributes](defaulttextattributes.md) — The default attributes to apply to the text.
- [font](font.md) — The font of the text.
- [textAlignment](textalignment.md) — The technique for aligning the text.
- [typingAttributes](typingattributes.md) — The attributes to apply to new text that the user enters.
- [BorderStyle](borderstyle-swift.enum.md) — The type of border around the text field.
