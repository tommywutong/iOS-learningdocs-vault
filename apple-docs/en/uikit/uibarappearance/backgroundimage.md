---
title: backgroundImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarappearance/backgroundimage
source_url: 'https://developer.apple.com/documentation/uikit/uibarappearance/backgroundimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarappearance/backgroundimage.json'
content_hash: 'sha256:ed304256672ed7e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarAppearance](../uibarappearance.md)

# backgroundImage

<sub>Instance Property</sub>

The image to display on top of the bar’s background color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var backgroundImage: UIImage? { get set }
```

## Discussion

The bar layers the specified image on top of the content in the [backgroundEffect](backgroundeffect.md) and [backgroundColor](backgroundcolor.md) properties. UIKit sizes the image according to the value in the [backgroundImageContentMode](backgroundimagecontentmode.md) property.

## See Also

### Configuring the background appearance

- [backgroundEffect](backgroundeffect.md) — The blur effect to apply to the bar’s background.
- [backgroundColor](backgroundcolor.md) — The background color of the bar.
- [backgroundImageContentMode](backgroundimagecontentmode.md) — The content mode to use when displaying the bar’s background image.
