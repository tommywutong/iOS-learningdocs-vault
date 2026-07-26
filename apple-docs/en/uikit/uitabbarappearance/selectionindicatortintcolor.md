---
title: selectionIndicatorTintColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarappearance/selectionindicatortintcolor
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarappearance/selectionindicatortintcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarappearance/selectionindicatortintcolor.json'
content_hash: 'sha256:9e3ca7ffff9391fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarAppearance](../uitabbarappearance.md)

# selectionIndicatorTintColor

<sub>Instance Property</sub>

The tint color to apply to the selection indicator image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var selectionIndicatorTintColor: UIColor? { get set }
```

## Discussion

UIKit combines the color in this property with the image in the [selectionIndicatorImage](selectionindicatorimage.md) to create the final appearance for the selected item. If you supplied a template image in [selectionIndicatorImage](selectionindicatorimage.md), UIKit uses this color to tint that image. If [selectionIndicatorImage](selectionindicatorimage.md) is `nil`, UIKit provides a default selection indicator image that accepts your tint color. If this property is `nil` or contains a clear color, UIKit doesn’t display a selection indicator.

If the image you supplied in [selectionIndicatorImage](selectionindicatorimage.md) isn’t a template image, UIKit ignores the value in this property and displays your image as is.

The default value of this property is `nil`.

## See Also

### Specifying the selection appearance

- [selectionIndicatorImage](selectionindicatorimage.md) — The image to draw for the selected item.
