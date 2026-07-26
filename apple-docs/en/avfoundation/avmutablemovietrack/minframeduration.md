---
title: minFrameDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.10+, visionOS 1.0+, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovietrack/minframeduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/minframeduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/minframeduration.json'
content_hash: 'sha256:8863b709fab40952'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# minFrameDuration

<sub>Instance Property</sub>

The minimum duration of the track’s frames.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var minFrameDuration: CMTime { get }
```

## Discussion

A track’s minimum frame duration is the reciprocal of its maximum frame rate. For example, a video track with a maximum frame rate of 30 frames per second has a minimum frame duration of 1/30, or 0.033 seconds.

The value of this property is [invalid](../../coremedia/cmtime/invalid.md) if the track can’t calculate its minimum frame duration, or if it’s unknown.

## See Also

### Accessing frame-based characteristics

- [nominalFrameRate](nominalframerate.md) — The frame rate of the track, in frames per second.
- [requiresFrameReordering](requiresframereordering.md) — A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.
