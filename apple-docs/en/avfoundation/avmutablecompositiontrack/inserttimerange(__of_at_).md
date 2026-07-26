---
title: 'insertTimeRange(_:of:at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecompositiontrack/inserttimerange(_:of:at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/inserttimerange(_:of:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecompositiontrack/inserttimerange%28_%3Aof%3Aat%3A%29.json'
content_hash: 'sha256:64c9aeaaf626fd5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableCompositionTrack](../avmutablecompositiontrack.md)

# insertTimeRange(_:of:at:)

<sub>Instance Method</sub>

Inserts a time range of media from a source track into a composition track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func insertTimeRange(_ timeRange: CMTimeRange, of track: AVAssetTrack, at startTime: CMTime) throws
```

## Parameters

- `timeRange` — The time range of media in the source track to add.

- `track` — The source asset track that contains the media to add.

- `startTime` — A start time within the composition track to insert the time range.

## Discussion

The time range you insert presents at its natural duration and rate. If necessary, you can scale it to a different duration by calling the [- scaleTimeRange:toDuration:](<scaletimerange(__toduration_).md>) method.

## See Also

### Managing time ranges

- [segments](segments.md) — The track segments that a composition track contains.
- [- insertEmptyTimeRange:](<insertemptytimerange(__).md>) — Adds or extends an empty time range within the track.
- [- insertTimeRanges:ofTracks:atTime:error:](<inserttimeranges(__of_at_).md>) — Inserts the time ranges of multiple source tracks into a track of a composition.
- [- removeTimeRange:](<removetimerange(__).md>) — Removes a time range of media from a composition track.
- [- scaleTimeRange:toDuration:](<scaletimerange(__toduration_).md>) — Changes the duration of a time range of the track.
