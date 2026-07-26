---
title: segments
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontrack/segments
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/segments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/segments.json'
content_hash: 'sha256:b486b2860bd43bd4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# segments

<sub>Instance Property</sub>

The time mappings from the track’s media samples to its timeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var segments: [AVCompositionTrackSegment] { get }
```

## See Also

### Accessing track segments

- [- segmentForTrackTime:](<segment(fortracktime_).md>) — Returns a segment whose target time range contains, or is closest to, the specified track time.
