---
title: naturalSize
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/naturalsize
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/naturalsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/naturalsize.json'
content_hash: 'sha256:06275821c3c165cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# naturalSize

<sub>Instance Property</sub>

The natural display dimensions of the output’s visual media.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var naturalSize: CGSize { get set }
```

## Discussion

The default value is [CGSizeZero](../../coregraphics/cgsizezero.md), which indicates the system sets the natural size according to the dimensions of the output track’s format descriptions.

You can’t set this value after writing starts.

## See Also

### Configuring presentation

- [transform](transform.md) — The transform to use for display of the output’s visual media.
- [preferredVolume](preferredvolume.md) — The volume to prefer for playback of the output’s audio data.
- [mediaTimeScale](mediatimescale.md) — The time scale of the track in the output file.
- [marksOutputTrackAsEnabled](marksoutputtrackasenabled.md) — A Boolean value that indicates whether to enable a track in the output for playback and processing.
