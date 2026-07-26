---
title: nominalFrameRate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovietrack/nominalframerate
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/nominalframerate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/nominalframerate.json'
content_hash: 'sha256:3cf3dfa7940ae717'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# nominalFrameRate

<sub>Instance Property</sub>

The frame rate of the track, in frames per second.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var nominalFrameRate: Float { get }
```

## Discussion

The nominal frame rate indicates the number of frames per second for tracks that contain a full frame per media sample. For field-based (interlaced) video tracks, the value of this property indicates the field rate, not the frame rate.

## See Also

### Accessing frame-based characteristics

- [minFrameDuration](minframeduration.md) — The minimum duration of the track’s frames.
- [requiresFrameReordering](requiresframereordering.md) — A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.
