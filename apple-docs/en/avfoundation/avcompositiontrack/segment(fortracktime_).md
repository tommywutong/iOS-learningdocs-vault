---
title: 'segment(forTrackTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcompositiontrack/segment(fortracktime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/segment(fortracktime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/segment%28fortracktime%3A%29.json'
content_hash: 'sha256:d93a9bffba52134e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# segment(forTrackTime:)

<sub>Instance Method</sub>

Returns a segment whose target time range contains, or is closest to, the specified track time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func segment(forTrackTime trackTime: CMTime) -> AVCompositionTrackSegment?
```

## Parameters

- `trackTime` — The track time of the segment to return.

## Return Value

The [AVCompositionTrackSegment](../avcompositiontracksegment.md) associated with the track time.

## See Also

### Accessing track segments

- [segments](segments.md) — The time mappings from the track’s media samples to its timeline.
