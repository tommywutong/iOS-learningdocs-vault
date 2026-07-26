---
title: image
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageview/image
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/image'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/image.json'
content_hash: 'sha256:f4f48523d65f2e54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# image

<sub>Instance Property</sub>

The image displayed in the image view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var image: UIImage? { get set }
```

## Discussion

This property contains the main image displayed by the image view. This image is displayed when the image view is in its natural state. When highlighted, the image view displays the image in its [highlightedImage](highlightedimage.md) property instead. If that property is set to `nil`, the image view applies a default highlight to this image. If the [animationImages](animationimages.md) property contains a valid set of images, those images are used instead.

Changing the image in this property does not automatically change the size of the image view. After setting the image, call the [- sizeToFit](<../uiview/sizetofit().md>) method to recompute the image view’s size based on the new image and the active constraints.

This property is set to the image you specified at initialization time. If you did not use the [- initWithImage:](<init(image_).md>) or [- initWithImage:highlightedImage:](<init(image_highlightedimage_).md>) method to initialize your image view, the initial value of this property is `nil`.

## See Also

### Related Documentation

- [animationImages](animationimages.md) — An array of [UIImage](../uiimage.md) objects to use for an animation.

### Accessing the displayed images

- [highlightedImage](highlightedimage.md) — The highlighted image displayed in the image view.
