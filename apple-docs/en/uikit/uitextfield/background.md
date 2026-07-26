---
title: background
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/background
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/background'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/background.json'
content_hash: 'sha256:9f365b1580221dc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# background

<sub>Instance Property</sub>

The image that represents the background appearance of the text field when it is in an enabled state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var background: UIImage? { get set }
```

## Discussion

When set, the image referred to by this property replaces the standard appearance controlled by the [borderStyle](borderstyle-swift.property.md) property. Background images are drawn in the border rectangle portion of the text field. Images you use for the text field’s background should be able to stretch to fit.

This property is set to `nil` by default.

## See Also

### Setting the view’s background appearance

- [borderStyle](borderstyle-swift.property.md) — The border style for the text field.
- [disabledBackground](disabledbackground.md) — The image that represents the background appearance of the text field when it is in a disabled state.
