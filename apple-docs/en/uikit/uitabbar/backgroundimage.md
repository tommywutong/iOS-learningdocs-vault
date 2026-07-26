---
title: backgroundImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbar/backgroundimage
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/backgroundimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/backgroundimage.json'
content_hash: 'sha256:ccabe9bbcda8e837'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBar](../uitabbar.md)

# backgroundImage

<sub>Instance Property</sub>

The custom background image for the tab bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var backgroundImage: UIImage? { get set }
```

## Discussion

If you specify a stretchable background image, the tab bar stretches your image to fill the available space. If your image is not stretchable and not large enough to fill the available space, the tab bar tiles the image. For information about how stretching works, see the [ResizingMode](../uiimage/resizingmode-swift.enum.md) type in [UIImage](../uiimage.md).

When a custom background image is present, the tab bar does not draw any blur effects behind itself, even when the [translucent](istranslucent.md) property is [true](../../swift/true.md).

## See Also

### Changing the background

- [barTintColor](bartintcolor.md) — The tint color to apply to the tab bar background.
