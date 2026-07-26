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
doc_path: /documentation/uikit/uitextview/typingattributes
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/typingattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/typingattributes.json'
content_hash: 'sha256:837eece9034914a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# typingAttributes

<sub>Instance Property</sub>

The attributes to apply to new text that the user enters.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var typingAttributes: [NSAttributedString.Key : Any] { get set }
```

## Discussion

This dictionary contains the attribute keys (and corresponding values) to apply to newly typed text. When the text view’s selection changes, the contents of the dictionary are cleared automatically.

## See Also

### Related Documentation

- [editable](iseditable.md) — A Boolean value that indicates whether the text view is editable.

### Configuring appearance attributes

- [font](font.md) — The font of the text.
- [textColor](textcolor.md) — The color of the text.
- [textAlignment](textalignment.md) — The technique for aligning the text.
- [linkTextAttributes](linktextattributes.md) — The attributes to apply to links.
- [borderStyle](borderstyle-swift.property.md) — The border style for the text field.
- [textHighlightAttributes](texthighlightattributes.md)
- [- drawTextHighlightBackgroundForTextRange:origin:](<drawtexthighlightbackground(for_origin_).md>)
- [BorderStyle](borderstyle-swift.enum.md) — The type of border around the text view.
