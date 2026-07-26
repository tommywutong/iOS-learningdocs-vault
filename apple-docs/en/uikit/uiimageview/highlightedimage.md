---
title: highlightedImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageview/highlightedimage
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/highlightedimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/highlightedimage.json'
content_hash: 'sha256:0c37e8efc9e5669b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# highlightedImage

<sub>Instance Property</sub>

The highlighted image displayed in the image view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var highlightedImage: UIImage? { get set }
```

## Discussion

The image in this property is displayed when the image view’s [highlighted](ishighlighted.md) property is [true](../../swift/true.md). If the [highlightedAnimationImages](highlightedanimationimages.md) property contains a valid set of images, those image are used instead.

This property is set to the image (if any) you specified at initialization time. If you did not use the [- initWithImage:highlightedImage:](<init(image_highlightedimage_).md>) method to initialize your image view, the initial value of this property is `nil`.

## See Also

### Related Documentation

- [highlightedAnimationImages](highlightedanimationimages.md) — An array of [UIImage](../uiimage.md) objects to use for an animation when the view is highlighted.

### Accessing the displayed images

- [image](image.md) — The image displayed in the image view.
