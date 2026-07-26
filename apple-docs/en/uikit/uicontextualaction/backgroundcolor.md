---
title: backgroundColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontextualaction/backgroundcolor
source_url: 'https://developer.apple.com/documentation/uikit/uicontextualaction/backgroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextualaction/backgroundcolor.json'
content_hash: 'sha256:34bb51e5d90eaa2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextualAction](../uicontextualaction.md)

# backgroundColor

<sub>Instance Property</sub>

The background color of the action button.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var backgroundColor: UIColor! { get set }
```

## Discussion

The default value of this property is determined by the value of the [style](style-swift.property.md) property, which determines the default appearance of the button. Assigning a new color to this property changes the background to the color that you specify.

## See Also

### Configuring the appearance

- [title](title.md) — The title displayed on the action button.
- [image](image.md) — The image to display in the action button.
