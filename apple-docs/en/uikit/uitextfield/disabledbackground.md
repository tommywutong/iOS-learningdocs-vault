---
title: disabledBackground
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/disabledbackground
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/disabledbackground'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/disabledbackground.json'
content_hash: 'sha256:0a18d7e71c22fca4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# disabledBackground

<sub>Instance Property</sub>

The image that represents the background appearance of the text field when it is in a disabled state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var disabledBackground: UIImage? { get set }
```

## Discussion

Background images are drawn in the border rectangle portion of the text field. Images you use for the text field’s background should be able to stretch to fit. This property is ignored if the [background](background.md) property is not also set.

This property is set to `nil` by default.

## See Also

### Setting the view’s background appearance

- [borderStyle](borderstyle-swift.property.md) — The border style for the text field.
- [background](background.md) — The image that represents the background appearance of the text field when it is in an enabled state.
