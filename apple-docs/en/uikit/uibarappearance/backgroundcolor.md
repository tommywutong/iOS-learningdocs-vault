---
title: backgroundColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarappearance/backgroundcolor
source_url: 'https://developer.apple.com/documentation/uikit/uibarappearance/backgroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarappearance/backgroundcolor.json'
content_hash: 'sha256:02ac98361ea643a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarAppearance](../uibarappearance.md)

# backgroundColor

<sub>Instance Property</sub>

The background color of the bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var backgroundColor: UIColor? { get set }
```

## Discussion

The bar layers the specified color on top of any blur effects you specified in the [backgroundEffect](backgroundeffect.md) property, and below the image in the [backgroundImage](backgroundimage.md) property.

## See Also

### Configuring the background appearance

- [backgroundEffect](backgroundeffect.md) — The blur effect to apply to the bar’s background.
- [backgroundImage](backgroundimage.md) — The image to display on top of the bar’s background color.
- [backgroundImageContentMode](backgroundimagecontentmode.md) — The content mode to use when displaying the bar’s background image.
