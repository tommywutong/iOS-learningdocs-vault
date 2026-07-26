---
title: segments
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovietrack/segments
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/segments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/segments.json'
content_hash: 'sha256:237d5e58606c9b93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# segments

<sub>Instance Property</sub>

The time mappings from the track’s media samples to its timeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var segments: [AVAssetTrackSegment] { get }
```

## See Also

### Accessing track segments

- [- segmentForTrackTime:](<segment(fortracktime_).md>) — Returns a segment whose target time range contains, or is closest to, the specified track time.
