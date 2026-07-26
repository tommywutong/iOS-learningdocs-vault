---
title: 'animatedImage(with:duration:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/animatedimage(with:duration:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/animatedimage(with:duration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/animatedimage%28with%3Aduration%3A%29.json'
content_hash: 'sha256:7b63eb4ef4f15ab7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# animatedImage(with:duration:)

<sub>Type Method</sub>

Creates and returns an animated image from an existing set of images.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class func animatedImage(with images: [UIImage], duration: TimeInterval) -> UIImage?
```

## Parameters

- `images` — An array of [UIImage](../uiimage.md) objects.

- `duration` — The duration of the animation.

## Return Value

A new image object.

## Discussion

All images included in the animated image should share the same size and scale.

## See Also

### Creating animated images

- [+ animatedImageNamed:duration:](<animatedimagenamed(__duration_).md>) — Creates and returns an animated image.
- [+ animatedResizableImageNamed:capInsets:duration:](<animatedresizableimagenamed(__capinsets_duration_).md>) — Creates and returns an animated image with end caps.
- [+ animatedResizableImageNamed:capInsets:resizingMode:duration:](<animatedresizableimagenamed(__capinsets_resizingmode_duration_).md>) — Creates and returns an animated image with end caps and a specific resizing mode.
