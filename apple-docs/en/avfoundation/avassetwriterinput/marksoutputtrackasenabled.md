---
title: marksOutputTrackAsEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/marksoutputtrackasenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/marksoutputtrackasenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/marksoutputtrackasenabled.json'
content_hash: 'sha256:265ca3c8c171496d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# marksOutputTrackAsEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether to enable a track in the output for playback and processing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var marksOutputTrackAsEnabled: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md). If the format you’re writing supports disabling tracks, you can disable a track by setting this value to [false](../../swift/false.md).

You can’t set this value after writing starts.

## See Also

### Configuring presentation

- [naturalSize](naturalsize.md) — The natural display dimensions of the output’s visual media.
- [transform](transform.md) — The transform to use for display of the output’s visual media.
- [preferredVolume](preferredvolume.md) — The volume to prefer for playback of the output’s audio data.
- [mediaTimeScale](mediatimescale.md) — The time scale of the track in the output file.
