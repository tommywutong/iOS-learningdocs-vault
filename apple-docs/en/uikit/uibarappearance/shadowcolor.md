---
title: shadowColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarappearance/shadowcolor
source_url: 'https://developer.apple.com/documentation/uikit/uibarappearance/shadowcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarappearance/shadowcolor.json'
content_hash: 'sha256:7b68dd0a89d6ec46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarAppearance](../uibarappearance.md)

# shadowColor

<sub>Instance Property</sub>

The color to apply to the bar’s custom or default shadow.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var shadowColor: UIColor? { get set }
```

## Discussion

UIKit uses this property and the [shadowImage](shadowimage.md) property to determine the shadow’s appearance. When [shadowImage](shadowimage.md) is `nil`, the bar displays a default shadow tinted according to the value of this property. If this property is `nil` or contains the [clearColor](../uicolor/clear.md) color, the bar displays no shadow.

If [shadowImage](shadowimage.md) contains a template image, the bar uses the image for the shadow and tints it using the value in this property. If this property is `nil` or contains the [clearColor](../uicolor/clear.md) color, the bar displays no shadow. However, if [shadowImage](shadowimage.md) doesn’t contain a template image, the bar displays the image without applying the color in this property.

## See Also

### Configuring the shadow appearance

- [shadowImage](shadowimage.md) — The image to use for the bar’s shadow.
