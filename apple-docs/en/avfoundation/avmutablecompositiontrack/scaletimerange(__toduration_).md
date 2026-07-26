---
title: 'scaleTimeRange(_:toDuration:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecompositiontrack/scaletimerange(_:toduration:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/scaletimerange(_:toduration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecompositiontrack/scaletimerange%28_%3Atoduration%3A%29.json'
content_hash: 'sha256:8b442f3b949e4069'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableCompositionTrack](../avmutablecompositiontrack.md)

# scaleTimeRange(_:toDuration:)

<sub>Instance Method</sub>

Changes the duration of a time range of the track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scaleTimeRange(_ timeRange: CMTimeRange, toDuration duration: CMTime)
```

## Parameters

- `timeRange` — The time range to scale.

- `duration` — A new duration value.

## See Also

### Managing time ranges

- [segments](segments.md) — The track segments that a composition track contains.
- [- insertEmptyTimeRange:](<insertemptytimerange(__).md>) — Adds or extends an empty time range within the track.
- [- insertTimeRange:ofTrack:atTime:error:](<inserttimerange(__of_at_).md>) — Inserts a time range of media from a source track into a composition track.
- [- insertTimeRanges:ofTracks:atTime:error:](<inserttimeranges(__of_at_).md>) — Inserts the time ranges of multiple source tracks into a track of a composition.
- [- removeTimeRange:](<removetimerange(__).md>) — Removes a time range of media from a composition track.
