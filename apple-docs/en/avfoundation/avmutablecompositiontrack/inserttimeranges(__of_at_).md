---
title: 'insertTimeRanges(_:of:at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecompositiontrack/inserttimeranges(_:of:at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/inserttimeranges(_:of:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecompositiontrack/inserttimeranges%28_%3Aof%3Aat%3A%29.json'
content_hash: 'sha256:4c12dc74e9bf2122'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableCompositionTrack](../avmutablecompositiontrack.md)

# insertTimeRanges(_:of:at:)

<sub>Instance Method</sub>

Inserts the time ranges of multiple source tracks into a track of a composition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func insertTimeRanges(_ timeRanges: [NSValue], of tracks: [AVAssetTrack], at startTime: CMTime) throws
```

## Parameters

- `timeRanges` — The time ranges of media in the source tracks to insert.

- `tracks` — The source asset tracks that contain the media to insert.

- `startTime` — A start time within composition the track to insert the time range.

## See Also

### Managing time ranges

- [segments](segments.md) — The track segments that a composition track contains.
- [- insertEmptyTimeRange:](<insertemptytimerange(__).md>) — Adds or extends an empty time range within the track.
- [- insertTimeRange:ofTrack:atTime:error:](<inserttimerange(__of_at_).md>) — Inserts a time range of media from a source track into a composition track.
- [- removeTimeRange:](<removetimerange(__).md>) — Removes a time range of media from a composition track.
- [- scaleTimeRange:toDuration:](<scaletimerange(__toduration_).md>) — Changes the duration of a time range of the track.
