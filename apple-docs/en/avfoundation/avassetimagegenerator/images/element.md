---
title: AVAssetImageGenerator.Images.Element
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/images/element
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images/element'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/images/element.json'
content_hash: 'sha256:3d54a6974c0facbe'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetImageGenerator](../../avassetimagegenerator.md) · [Images](../images.md)

# AVAssetImageGenerator.Images.Element

<sub>Enumeration</sub>

An element that provides the result of an image generation request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@frozen enum Element
```

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Cases

- [AVAssetImageGenerator.Images.Element.success(requestedTime:image:actualTime:)](<element/success(requestedtime_image_actualtime_).md>) — A result that indicates an image generation request succeeded.
- [AVAssetImageGenerator.Images.Element.failure(requestedTime:error:)](<element/failure(requestedtime_error_).md>) — A result that indicates an image generation request failed.

### Accessing image data

- [image](element/image.md) — An image for a requested time.
- [requestedTime](element/requestedtime.md) — A time in the video timeline at which you request an image.
- [actualTime](element/actualtime.md) — The actual time in the video timeline at which the image generator creates the image.

## See Also

### Iterating elements

- [next()](<next().md>) — Returns the next element in the sequence.
