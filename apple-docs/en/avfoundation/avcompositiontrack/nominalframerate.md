---
title: nominalFrameRate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontrack/nominalframerate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/nominalframerate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/nominalframerate.json'
content_hash: 'sha256:9692f9c467ae5510'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# nominalFrameRate

<sub>Instance Property</sub>

The frame rate of the track, in frames per second.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nominalFrameRate: Float { get }
```

## Discussion

The nominal frame rate indicates the number of frames per second for tracks that contain a full frame per media sample. For field-based (interlaced) video tracks, the value of this property indicates the field rate, not the frame rate.

## See Also

### Accessing frame-based characteristics

- [minFrameDuration](minframeduration.md) — The minimum duration of the track’s frames.
- [requiresFrameReordering](requiresframereordering.md) — A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.
