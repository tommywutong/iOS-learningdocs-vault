---
title: minimumFontSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/minimumfontsize
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/minimumfontsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/minimumfontsize.json'
content_hash: 'sha256:70b3a1bc54449921'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# minimumFontSize

<sub>Instance Property</sub>

The size of the smallest permissible font when drawing the text field’s text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var minimumFontSize: CGFloat { get set }
```

## Discussion

When drawing text that might not fit within the bounding rectangle of the text field, you can use this property to prevent the receiver from reducing the font size to the point where it is no longer legible.

The default value for this property is 0.0. If you enable font adjustment for the text field, you should always increase this value.

If you are using styled text in iOS 6 or later, assigning a new value to this property causes the minimum font size to be applied to the entirety of the string in the [attributedText](attributedtext.md) property. If you want to apply different minimum font sizes to different parts of your string, create a new attributed string with the desired style information and associate it with the text field.

## See Also

### Sizing the text field’s text

- [adjustsFontSizeToFitWidth](adjustsfontsizetofitwidth.md) — A Boolean value that indicates whether to reduce the font size to fit the text string into the text field’s bounding rectangle.
- [sizingRule](../uiletterformawareadjusting/sizingrule.md) — The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.
