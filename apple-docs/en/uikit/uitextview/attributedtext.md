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
doc_path: /documentation/uikit/uitextview/attributedtext
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/attributedtext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/attributedtext.json'
content_hash: 'sha256:0ec72128d483cfca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# attributedText

<sub>Instance Property</sub>

The styled text that the text view displays.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var attributedText: NSAttributedString! { get set }
```

## Discussion

Assigning a new value to this property also replaces the value of the [text](text.md) property with the same string data, albeit without any formatting information. In addition, the [font](font.md), [textColor](textcolor.md), and [textAlignment](textalignment.md) properties are updated to reflect the typing attributes of the text view.

## See Also

### Specifying the text content

- [text](text.md) — The text that the text view displays.
