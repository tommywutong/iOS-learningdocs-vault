---
title: transform
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/transform
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/transform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/transform.json'
content_hash: 'sha256:c96528798b9ab745'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# transform

<sub>Instance Property</sub>

The transform to use for display of the output’s visual media.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var transform: CGAffineTransform { get set }
```

## Discussion

By default, the input uses the [CGAffineTransformIdentity](../../coregraphics/cgaffinetransformidentity.md) transform.

You can’t set this value after writing starts.

## See Also

### Configuring presentation

- [naturalSize](naturalsize.md) — The natural display dimensions of the output’s visual media.
- [preferredVolume](preferredvolume.md) — The volume to prefer for playback of the output’s audio data.
- [mediaTimeScale](mediatimescale.md) — The time scale of the track in the output file.
- [marksOutputTrackAsEnabled](marksoutputtrackasenabled.md) — A Boolean value that indicates whether to enable a track in the output for playback and processing.
