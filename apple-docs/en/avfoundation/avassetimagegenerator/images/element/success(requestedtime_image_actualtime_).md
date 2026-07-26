---
title: 'AVAssetImageGenerator.Images.Element.success(requestedTime:image:actualTime:)'
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetimagegenerator/images/element/success(requestedtime:image:actualtime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images/element/success(requestedtime:image:actualtime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/images/element/success%28requestedtime%3Aimage%3Aactualtime%3A%29.json'
content_hash: 'sha256:2b497f03abe74231'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVAssetImageGenerator](../../../avassetimagegenerator.md) · [Images](../../images.md) · [Element](../element.md)

# AVAssetImageGenerator.Images.Element.success(requestedTime:image:actualTime:)

<sub>Case</sub>

A result that indicates an image generation request succeeded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case success(requestedTime: CMTime, image: CGImage, actualTime: CMTime)
```

## Parameters

- `requestedTime` — A time in the video timeline at which you requested an image.

- `image` — An image for the requested time.

- `actualTime` — A time in the video timeline at which the image generator created an image.

## See Also

### Cases

- [AVAssetImageGenerator.Images.Element.failure(requestedTime:error:)](<failure(requestedtime_error_).md>) — A result that indicates an image generation request failed.
