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
doc_path: /documentation/avfoundation/avmutablecompositiontrack/segments
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/segments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecompositiontrack/segments.json'
content_hash: 'sha256:30a71c50f4c92e79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableCompositionTrack](../avmutablecompositiontrack.md)

# segments

<sub>Instance Property</sub>

The track segments that a composition track contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var segments: [AVCompositionTrackSegment]! { get set }
```

## See Also

### Managing time ranges

- [- insertEmptyTimeRange:](<insertemptytimerange(__).md>) — Adds or extends an empty time range within the track.
- [- insertTimeRange:ofTrack:atTime:error:](<inserttimerange(__of_at_).md>) — Inserts a time range of media from a source track into a composition track.
- [- insertTimeRanges:ofTracks:atTime:error:](<inserttimeranges(__of_at_).md>) — Inserts the time ranges of multiple source tracks into a track of a composition.
- [- removeTimeRange:](<removetimerange(__).md>) — Removes a time range of media from a composition track.
- [- scaleTimeRange:toDuration:](<scaletimerange(__toduration_).md>) — Changes the duration of a time range of the track.
