---
title: 'pictureInPictureButtonStartImage(compatibleWith:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avpictureinpicturecontroller/pictureinpicturebuttonstartimage(compatiblewith:)'
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/pictureinpicturebuttonstartimage(compatiblewith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/pictureinpicturebuttonstartimage%28compatiblewith%3A%29.json'
content_hash: 'sha256:21b3239e12705a8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureController](../avpictureinpicturecontroller.md)

# pictureInPictureButtonStartImage(compatibleWith:)

<sub>Type Method</sub>

Returns a system-default template image that’s compatible with a trait collection for the button that starts Picture in Picture in your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func pictureInPictureButtonStartImage(compatibleWith traitCollection: UITraitCollection?) -> UIImage
```

## Parameters

- `traitCollection` — A trait collection that describes the image to retrieve. Pass `nil` to use traits that describe the main screen.

## Return Value

A system-default template image.

## See Also

### Retrieving Picture in Picture Template Images

- [pictureInPictureButtonStartImage](pictureinpicturebuttonstartimage.md) — A system-default template image for the button that starts Picture in Picture in your app.
- [pictureInPictureButtonStopImage](pictureinpicturebuttonstopimage.md) — A system-default template image for the button that stops Picture in Picture in your app.
- [+ pictureInPictureButtonStopImageCompatibleWithTraitCollection:](<pictureinpicturebuttonstopimage(compatiblewith_).md>) — Returns a system-default template image that’s compatible with a trait collection for the button that stops Picture in Picture in your app.
