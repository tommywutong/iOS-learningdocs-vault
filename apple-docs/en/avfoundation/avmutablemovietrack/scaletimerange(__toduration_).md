---
title: 'scaleTimeRange(_:toDuration:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovietrack/scaletimerange(_:toduration:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/scaletimerange(_:toduration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/scaletimerange%28_%3Atoduration%3A%29.json'
content_hash: 'sha256:d6e4aa775b37d624'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# scaleTimeRange(_:toDuration:)

<sub>Instance Method</sub>

Changes the duration of a time range in a track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func scaleTimeRange(_ timeRange: CMTimeRange, toDuration duration: CMTime)
```

## Parameters

- `timeRange` — The time range to change.

- `duration` — The new duration for the time range.

## See Also

### Managing time ranges

- [- insertTimeRange:ofTrack:atTime:copySampleData:error:](<inserttimerange(__of_at_copysampledata_).md>) — Inserts a portion of an asset track into the target movie.
- [- insertEmptyTimeRange:](<insertemptytimerange(__).md>) — Adds an empty time range to a track.
- [- removeTimeRange:](<removetimerange(__).md>) — Removes the specified time range from a track.
