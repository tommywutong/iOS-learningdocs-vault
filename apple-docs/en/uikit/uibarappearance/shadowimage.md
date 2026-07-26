---
title: shadowImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarappearance/shadowimage
source_url: 'https://developer.apple.com/documentation/uikit/uibarappearance/shadowimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarappearance/shadowimage.json'
content_hash: 'sha256:4fffad318a4ab908'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarAppearance](../uibarappearance.md)

# shadowImage

<sub>Instance Property</sub>

The image to use for the bar’s shadow.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var shadowImage: UIImage? { get set }
```

## Discussion

UIKit uses this property and the [shadowColor](shadowcolor.md) property to determine the shadow’s appearance. When this property is `nil`, the bar displays a default shadow tinted according to the value in the [shadowColor](shadowcolor.md) property. If [shadowColor](shadowcolor.md) is `nil` or contains the [clearColor](../uicolor/clear.md) color, the bar displays no shadow.

If this property contains a template image, the bar uses the image for the shadow and tints it using the value in [shadowColor](shadowcolor.md). If [shadowColor](shadowcolor.md) is `nil` or contains the [clearColor](../uicolor/clear.md) color, the bar displays no shadow. However, if this property doesn’t contain a template image, the bar displays the image without applying the shadow color.

## See Also

### Configuring the shadow appearance

- [shadowColor](shadowcolor.md) — The color to apply to the bar’s custom or default shadow.
