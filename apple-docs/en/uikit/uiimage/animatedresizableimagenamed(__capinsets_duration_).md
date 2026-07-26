---
title: 'animatedResizableImageNamed(_:capInsets:duration:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/animatedresizableimagenamed(_:capinsets:duration:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/animatedresizableimagenamed(_:capinsets:duration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/animatedresizableimagenamed%28_%3Acapinsets%3Aduration%3A%29.json'
content_hash: 'sha256:6f3938aa25d62016'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# animatedResizableImageNamed(_:capInsets:duration:)

<sub>Type Method</sub>

Creates and returns an animated image with end caps.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class func animatedResizableImageNamed(_ name: String, capInsets: UIEdgeInsets, duration: TimeInterval) -> UIImage?
```

## Parameters

- `name` — The full or partial path to the file (sans suffix).

- `capInsets` — The values to use for the cap insets.

- `duration` — The duration of the animation.

## Return Value

A new image object.

## Discussion

This method loads a series of files by appending a series of numbers to the base file name provided in the `name` parameter. For example, if the `name` parameter had ‘image’ as its contents, this method would attempt to load images from files with the names ‘image0’, ‘image1’ and so on all the way up to ‘image1024’. All images included in the animated image should share the same size and scale.

Each frame in the animation follows the rules for resizable images created by the [- resizableImageWithCapInsets:](<resizableimage(withcapinsets_).md>) method.

## See Also

### Related Documentation

- [- resizableImageWithCapInsets:](<resizableimage(withcapinsets_).md>) — Returns a new version of the image with the specified cap insets.
- [- resizableImageWithCapInsets:resizingMode:](<resizableimage(withcapinsets_resizingmode_).md>) — Returns a new version of the image with the specified cap insets and options.

### Creating animated images

- [+ animatedImageNamed:duration:](<animatedimagenamed(__duration_).md>) — Creates and returns an animated image.
- [+ animatedImageWithImages:duration:](<animatedimage(with_duration_).md>) — Creates and returns an animated image from an existing set of images.
- [+ animatedResizableImageNamed:capInsets:resizingMode:duration:](<animatedresizableimagenamed(__capinsets_resizingmode_duration_).md>) — Creates and returns an animated image with end caps and a specific resizing mode.
