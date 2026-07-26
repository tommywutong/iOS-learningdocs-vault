---
title: requestedTime
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/images/element/requestedtime
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images/element/requestedtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/images/element/requestedtime.json'
content_hash: 'sha256:97c79104519141d6'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVAssetImageGenerator](../../../avassetimagegenerator.md) · [Images](../../images.md) · [Element](../element.md)

# requestedTime

<sub>Instance Property</sub>

A time in the video timeline at which you request an image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requestedTime: CMTime { get }
```

## See Also

### Accessing image data

- [image](image.md) — An image for a requested time.
- [actualTime](actualtime.md) — The actual time in the video timeline at which the image generator creates the image.
