---
title: requiresFrameReordering
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontrack/requiresframereordering
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/requiresframereordering'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/requiresframereordering.json'
content_hash: 'sha256:2ac96534410be482'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# requiresFrameReordering

<sub>Instance Property</sub>

A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var requiresFrameReordering: Bool { get }
```

## See Also

### Accessing frame-based characteristics

- [nominalFrameRate](nominalframerate.md) — The frame rate of the track, in frames per second.
- [minFrameDuration](minframeduration.md) — The minimum duration of the track’s frames.
