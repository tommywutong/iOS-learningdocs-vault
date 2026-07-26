---
title: selectionIndicatorImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarappearance/selectionindicatorimage
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarappearance/selectionindicatorimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarappearance/selectionindicatorimage.json'
content_hash: 'sha256:e2b2d5fe14d394dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarAppearance](../uitabbarappearance.md)

# selectionIndicatorImage

<sub>Instance Property</sub>

The image to draw for the selected item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var selectionIndicatorImage: UIImage? { get set }
```

## Discussion

UIKit renders the image in this property above the tab bar, but behind the tab bar item. If you specify a template or symbol image, UIKit renders that image with the tint color from the [selectionIndicatorTintColor](selectionindicatortintcolor.md) property. If you specify any other type of image, UIKit displays your image without any additional tinting.

The default value of this property is `nil`, which causes UIKit to provide a default selection image.

## See Also

### Specifying the selection appearance

- [selectionIndicatorTintColor](selectionindicatortintcolor.md) — The tint color to apply to the selection indicator image.
