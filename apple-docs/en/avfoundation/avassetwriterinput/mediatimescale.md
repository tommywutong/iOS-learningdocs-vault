---
title: mediaTimeScale
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/mediatimescale
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/mediatimescale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/mediatimescale.json'
content_hash: 'sha256:1c618590bd24e07b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# mediaTimeScale

<sub>Instance Property</sub>

The time scale of the track in the output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var mediaTimeScale: CMTimeScale { get set }
```

## Discussion

The default value is `0`, which indicates that the input chooses an appropriate value, if applicable. It’s an error to set this value if the input’s media type is [AVMediaTypeAudio](../avmediatype/audio.md).

You can’t set this value after writing starts.

## See Also

### Configuring presentation

- [naturalSize](naturalsize.md) — The natural display dimensions of the output’s visual media.
- [transform](transform.md) — The transform to use for display of the output’s visual media.
- [preferredVolume](preferredvolume.md) — The volume to prefer for playback of the output’s audio data.
- [marksOutputTrackAsEnabled](marksoutputtrackasenabled.md) — A Boolean value that indicates whether to enable a track in the output for playback and processing.
