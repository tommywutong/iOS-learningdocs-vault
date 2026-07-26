---
title: image
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/images/element/image
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images/element/image'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/images/element/image.json'
content_hash: 'sha256:d5bc0c0d0cf682fe'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVAssetImageGenerator](../../../avassetimagegenerator.md) · [Images](../../images.md) · [Element](../element.md)

# image

<sub>Instance Property</sub>

An image for a requested time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var image: CGImage { get throws }
```

## See Also

### Accessing image data

- [requestedTime](requestedtime.md) — A time in the video timeline at which you request an image.
- [actualTime](actualtime.md) — The actual time in the video timeline at which the image generator creates the image.
