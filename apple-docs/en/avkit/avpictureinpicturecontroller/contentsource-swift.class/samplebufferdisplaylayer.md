---
title: sampleBufferDisplayLayer
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/samplebufferdisplaylayer
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/samplebufferdisplaylayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/samplebufferdisplaylayer.json'
content_hash: 'sha256:607da63fcf606e6a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVPictureInPictureController](../../avpictureinpicturecontroller.md) · [ContentSource](../contentsource-swift.class.md)

# sampleBufferDisplayLayer

<sub>Instance Property</sub>

The presenting sample buffer display layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sampleBufferDisplayLayer: AVSampleBufferDisplayLayer? { get }
```

## Discussion

This value is `nil` if the content source doesn’t represent a sample buffer display layer.

## See Also

### Accessing the Presentation Layer

- [playerLayer](playerlayer.md) — The presenting player layer.
