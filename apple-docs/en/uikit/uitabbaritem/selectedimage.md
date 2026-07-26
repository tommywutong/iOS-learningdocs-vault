---
title: selectedImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbaritem/selectedimage
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritem/selectedimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritem/selectedimage.json'
content_hash: 'sha256:f6051cdccc156bc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarItem](../uitabbaritem.md)

# selectedImage

<sub>Instance Property</sub>

The source image the item uses to generate its selected image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var selectedImage: UIImage? { get set }
```

## Discussion

If `nil`, the item uses the value in [image](../uibaritem/image.md) instead. The item creates the images it displays from the alpha values in its source images. To prevent system tinting, use images with the [UIImageRenderingModeAlwaysOriginal](../uiimage/renderingmode-swift.enum/alwaysoriginal.md) rendering mode. The item clips any image that’s larger than its bounds.

## See Also

### Configuring the item’s appearance

- [standardAppearance](standardappearance.md) — The appearance settings for a tab bar.
- [scrollEdgeAppearance](scrolledgeappearance.md) — The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.
- [titlePositionAdjustment](titlepositionadjustment.md) — The offset to apply to the title’s position.
