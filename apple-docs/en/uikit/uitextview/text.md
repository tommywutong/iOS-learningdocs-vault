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
doc_path: /documentation/uikit/uitextview/text
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/text'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/text.json'
content_hash: 'sha256:03cd966f0de490a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# text

<sub>Instance Property</sub>

The text that the text view displays.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var text: String! { get set }
```

## Discussion

In iOS 6 and later, assigning a new value to this property also replaces the value of the [attributedText](attributedtext.md) property with the same text, albeit without any inherent style attributes. Instead the text view styles the new string using the [font](font.md), [textColor](textcolor.md), and other style-related properties of the class.

## See Also

### Specifying the text content

- [attributedText](attributedtext.md) — The styled text that the text view displays.
