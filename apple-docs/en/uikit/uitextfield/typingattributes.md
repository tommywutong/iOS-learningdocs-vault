---
title: typingAttributes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/typingattributes
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/typingattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/typingattributes.json'
content_hash: 'sha256:a4e9a7f273c8e5f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# typingAttributes

<sub>Instance Property</sub>

The attributes to apply to new text that the user enters.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var typingAttributes: [NSAttributedString.Key : Any]? { get set }
```

## Discussion

This dictionary contains the attribute keys (and corresponding values) to apply to newly typed text. When the text field’s selection changes, the contents of the dictionary are cleared automatically.

If the text field is not in editing mode, this property contains the value `nil`. Similarly, you cannot assign a value to this property unless the text field is currently in editing mode.

## See Also

### Related Documentation

- [editing](isediting.md) — A Boolean value that indicates whether the text field is currently in edit mode.

### Configuring the text attributes

- [text](text.md) — The text that the text field displays.
- [attributedText](attributedtext.md) — The styled text that the text field displays.
- [placeholder](placeholder.md) — The string that displays when there is no other text in the text field.
- [attributedPlaceholder](attributedplaceholder.md) — The styled string that displays when there is no other text in the text field.
- [defaultTextAttributes](defaulttextattributes.md) — The default attributes to apply to the text.
- [font](font.md) — The font of the text.
- [textColor](textcolor.md) — The color of the text.
- [textAlignment](textalignment.md) — The technique for aligning the text.
- [BorderStyle](borderstyle-swift.enum.md) — The type of border around the text field.
