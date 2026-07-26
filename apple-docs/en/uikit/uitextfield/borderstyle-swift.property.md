---
title: borderStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/borderstyle-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/borderstyle-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/borderstyle-swift.property.json'
content_hash: 'sha256:c69c423c0570a43e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# borderStyle

<sub>Instance Property</sub>

The border style for the text field.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var borderStyle: UITextField.BorderStyle { get set }
```

## Discussion

The default value for this property is [UITextBorderStyleNone](borderstyle-swift.enum/none.md). If the value is set to the [UITextBorderStyleRoundedRect](borderstyle-swift.enum/roundedrect.md) style, the custom background image associated with the text field is ignored.

## See Also

### Setting the view’s background appearance

- [background](background.md) — The image that represents the background appearance of the text field when it is in an enabled state.
- [disabledBackground](disabledbackground.md) — The image that represents the background appearance of the text field when it is in a disabled state.
