---
title: tintColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageview/tintcolor
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/tintcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/tintcolor.json'
content_hash: 'sha256:f504bb31d7631686'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# tintColor

<sub>Instance Property</sub>

A color used to tint template images in the view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var tintColor: UIColor! { get set }
```

## Discussion

The default is `nil`. If a non-`nil` value is specified, the color is applied to any template images attached to the image view. For more information, see the [renderingMode](../uiimage/renderingmode-swift.property.md) property on the [UIImage](../uiimage.md) class.

## See Also

### Configuring the image view

- [userInteractionEnabled](isuserinteractionenabled.md) — A Boolean value that determines whether user events are ignored and removed from the event queue.
- [highlighted](ishighlighted.md) — A Boolean value that determines whether the image is highlighted.
