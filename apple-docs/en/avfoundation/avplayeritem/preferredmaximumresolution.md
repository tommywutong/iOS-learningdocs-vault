---
title: preferredMaximumResolution
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/preferredmaximumresolution
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/preferredmaximumresolution'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/preferredmaximumresolution.json'
content_hash: 'sha256:dedac475c1252d11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# preferredMaximumResolution

<sub>Instance Property</sub>

The desired maximum resolution of a video that is to be downloaded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated var preferredMaximumResolution: CGSize { get set }
```

## Discussion

Defaults to [CGSizeZero](../../coregraphics/cgsizezero.md), which indicates there is no limit on the video resolution. Any other value indicates a preferred maximum video resolution. This property only applies to HTTP Live Streaming assets.

## See Also

### Configuring presentation

- [presentationSize](presentationsize.md) — The size at which the visual portion of the item is presented by the player.
- [videoApertureMode](videoaperturemode.md) — The video aperture mode to apply during playback.
- [AVVideoApertureMode](../avvideoaperturemode.md) — A value that describes how a video is scaled or cropped.
