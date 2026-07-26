---
title: AVVideoApertureMode
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideoaperturemode
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideoaperturemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideoaperturemode.json'
content_hash: 'sha256:7220c1073932071f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoApertureMode

<sub>Structure</sub>

A value that describes how a video is scaled or cropped.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVVideoApertureMode
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Aperture modes

- [AVVideoApertureModeCleanAperture](avvideoaperturemode/cleanaperture.md) — The pixel aspect ratio and clean aperture will be applied.
- [AVVideoApertureModeEncodedPixels](avvideoaperturemode/encodedpixels.md) — The encoded dimensions of the image description are displayed.
- [AVVideoApertureModeProductionAperture](avvideoaperturemode/productionaperture.md) — The pixel aspect ratio will be applied.

### Initializers

- [init(rawValue:)](<avvideoaperturemode/init(rawvalue_).md>) — Creates a video aperture mode with a string.

## See Also

### Configuring presentation

- [presentationSize](avplayeritem/presentationsize.md) — The size at which the visual portion of the item is presented by the player.
- [preferredMaximumResolution](avplayeritem/preferredmaximumresolution.md) — The desired maximum resolution of a video that is to be downloaded.
- [videoApertureMode](avplayeritem/videoaperturemode.md) — The video aperture mode to apply during playback.
