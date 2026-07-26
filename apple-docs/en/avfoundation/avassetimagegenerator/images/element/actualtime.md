---
title: actualTime
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/images/element/actualtime
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images/element/actualtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/images/element/actualtime.json'
content_hash: 'sha256:5c122490986212d8'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVAssetImageGenerator](../../../avassetimagegenerator.md) · [Images](../../images.md) · [Element](../element.md)

# actualTime

<sub>Instance Property</sub>

The actual time in the video timeline at which the image generator creates the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var actualTime: CMTime { get throws }
```

## Discussion

This value may differ from the [requestedTime](requestedtime.md) depending on the configuration of the image generator’s [requestedTimeToleranceBefore](../../requestedtimetolerancebefore.md) and [requestedTimeToleranceAfter](../../requestedtimetoleranceafter.md) properties.

## See Also

### Accessing image data

- [image](image.md) — An image for a requested time.
- [requestedTime](requestedtime.md) — A time in the video timeline at which you request an image.
