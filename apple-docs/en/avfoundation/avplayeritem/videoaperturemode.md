---
title: videoApertureMode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/videoaperturemode
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/videoaperturemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/videoaperturemode.json'
content_hash: 'sha256:3c021e3affb729cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# videoApertureMode

<sub>Instance Property</sub>

The video aperture mode to apply during playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated var videoApertureMode: AVVideoApertureMode { get set }
```

## Discussion

The default value for this property is [AVVideoApertureModeCleanAperture](../avvideoaperturemode/cleanaperture.md).

## See Also

### Configuring presentation

- [presentationSize](presentationsize.md) — The size at which the visual portion of the item is presented by the player.
- [preferredMaximumResolution](preferredmaximumresolution.md) — The desired maximum resolution of a video that is to be downloaded.
- [AVVideoApertureMode](../avvideoaperturemode.md) — A value that describes how a video is scaled or cropped.
