---
title: preferredTransform
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayervideooutput/configuration/preferredtransform
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayervideooutput/configuration/preferredtransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayervideooutput/configuration/preferredtransform.json'
content_hash: 'sha256:f27b1beaf635c475'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayerVideoOutput](../../avplayervideooutput.md) · [Configuration](../configuration.md)

# preferredTransform

<sub>Instance Property</sub>

The preferred transform of the visual media.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preferredTransform: CGAffineTransform { get }
```

## Discussion

The system retrieves the transform from the [AVAssetTrack](../../avassettrack.md) that provides the media data. If the source track doesn’t specify a transform, the value of this property is [CGAffineTransformIdentity](../../../coregraphics/cgaffinetransformidentity.md).

## See Also

### Inspecting the configuration

- [sourcePlayerItem](sourceplayeritem.md) — The player item that’s the source of this configuration.
- [dataChannelDescription](datachanneldescription.md) — An array of data channels selected for this configuration.
- [activationTime](activationtime.md) — The host time this configuration became active on its associated player object.
