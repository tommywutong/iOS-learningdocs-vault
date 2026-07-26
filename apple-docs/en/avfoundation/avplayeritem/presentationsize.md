---
title: presentationSize
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/presentationsize
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/presentationsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/presentationsize.json'
content_hash: 'sha256:25dc75d675a025e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# presentationSize

<sub>Instance Property</sub>

The size at which the visual portion of the item is presented by the player.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var presentationSize: CGSize { get }
```

## Discussion

This property can be accessed at any time, but may return a value of `CGSizeZero` prior to the player item becoming ready to play. You can use key-value observing to obtain the player item’s valid presentation size as early as possible.

## See Also

### Configuring presentation

- [preferredMaximumResolution](preferredmaximumresolution.md) — The desired maximum resolution of a video that is to be downloaded.
- [videoApertureMode](videoaperturemode.md) — The video aperture mode to apply during playback.
- [AVVideoApertureMode](../avvideoaperturemode.md) — A value that describes how a video is scaled or cropped.
