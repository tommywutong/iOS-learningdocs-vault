---
title: 'AVAssetImageGenerator.Images.Element.failure(requestedTime:error:)'
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetimagegenerator/images/element/failure(requestedtime:error:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images/element/failure(requestedtime:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/images/element/failure%28requestedtime%3Aerror%3A%29.json'
content_hash: 'sha256:04bd274e500752c5'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVAssetImageGenerator](../../../avassetimagegenerator.md) · [Images](../../images.md) · [Element](../element.md)

# AVAssetImageGenerator.Images.Element.failure(requestedTime:error:)

<sub>Case</sub>

A result that indicates an image generation request failed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case failure(requestedTime: CMTime, error: any Error)
```

## Parameters

- `requestedTime` — A time in the video timeline at which you requested an image.

- `error` — An error that indicates the reason for the failure.

## See Also

### Cases

- [AVAssetImageGenerator.Images.Element.success(requestedTime:image:actualTime:)](<success(requestedtime_image_actualtime_).md>) — A result that indicates an image generation request succeeded.
