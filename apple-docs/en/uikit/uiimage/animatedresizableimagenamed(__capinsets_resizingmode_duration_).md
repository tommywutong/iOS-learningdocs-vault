---
title: 'animatedResizableImageNamed(_:capInsets:resizingMode:duration:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/animatedresizableimagenamed(_:capinsets:resizingmode:duration:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/animatedresizableimagenamed(_:capinsets:resizingmode:duration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/animatedresizableimagenamed%28_%3Acapinsets%3Aresizingmode%3Aduration%3A%29.json'
content_hash: 'sha256:1a3b48f15e74560c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# animatedResizableImageNamed(_:capInsets:resizingMode:duration:)

<sub>Type Method</sub>

Creates and returns an animated image with end caps and a specific resizing mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class func animatedResizableImageNamed(_ name: String, capInsets: UIEdgeInsets, resizingMode: UIImage.ResizingMode, duration: TimeInterval) -> UIImage?
```

## Parameters

- `name` — The full or partial path to the file (sans suffix).

- `capInsets` — The values to use for the cap insets.

- `resizingMode` — The mode with which the interior of the image is resized.

- `duration` — The duration of the animation.

## Return Value

A new animated image object with the specified cap insets and resizing mode.

## Discussion

This method is exactly the same as its counterpart [+ animatedResizableImageNamed:capInsets:duration:](<animatedresizableimagenamed(__capinsets_duration_).md>) except that the resizing mode of the new image object can be explicitly declared. Since the resizing mode of an image is [UIImageResizingModeTile](resizingmode-swift.enum/tile.md) by default, this method should only be used in place of its counterpart to create an animated image that needs to be resized with the [UIImageResizingModeStretch](resizingmode-swift.enum/stretch.md) resizing mode.

## See Also

### Related Documentation

- [- resizableImageWithCapInsets:](<resizableimage(withcapinsets_).md>) — Returns a new version of the image with the specified cap insets.
- [- resizableImageWithCapInsets:resizingMode:](<resizableimage(withcapinsets_resizingmode_).md>) — Returns a new version of the image with the specified cap insets and options.

### Creating animated images

- [+ animatedImageNamed:duration:](<animatedimagenamed(__duration_).md>) — Creates and returns an animated image.
- [+ animatedImageWithImages:duration:](<animatedimage(with_duration_).md>) — Creates and returns an animated image from an existing set of images.
- [+ animatedResizableImageNamed:capInsets:duration:](<animatedresizableimagenamed(__capinsets_duration_).md>) — Creates and returns an animated image with end caps.
