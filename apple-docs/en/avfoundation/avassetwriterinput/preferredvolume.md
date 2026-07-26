---
title: preferredVolume
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/preferredvolume
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/preferredvolume'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/preferredvolume.json'
content_hash: 'sha256:ee225bacacef58b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# preferredVolume

<sub>Instance Property</sub>

The volume to prefer for playback of the output’s audio data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var preferredVolume: Float { get set }
```

## Discussion

The default value for audio data is `1.0`, which indicates typical playback level. Set the value for this property in the range of `0.0` to `1.0`. For nonaudio media, the default value is `0.0`.

You can’t set this value after writing starts.

## See Also

### Configuring presentation

- [naturalSize](naturalsize.md) — The natural display dimensions of the output’s visual media.
- [transform](transform.md) — The transform to use for display of the output’s visual media.
- [mediaTimeScale](mediatimescale.md) — The time scale of the track in the output file.
- [marksOutputTrackAsEnabled](marksoutputtrackasenabled.md) — A Boolean value that indicates whether to enable a track in the output for playback and processing.
