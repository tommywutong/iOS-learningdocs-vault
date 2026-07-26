---
title: 'insertEmptyTimeRange(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovietrack/insertemptytimerange(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/insertemptytimerange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/insertemptytimerange%28_%3A%29.json'
content_hash: 'sha256:0fb1c12cbeb5f41d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# insertEmptyTimeRange(_:)

<sub>Instance Method</sub>

Adds an empty time range to a track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func insertEmptyTimeRange(_ timeRange: CMTimeRange)
```

## Parameters

- `timeRange` — A time range to insert.

## Discussion

You can’t add empty time ranges to the end of a track.

## See Also

### Managing time ranges

- [- insertTimeRange:ofTrack:atTime:copySampleData:error:](<inserttimerange(__of_at_copysampledata_).md>) — Inserts a portion of an asset track into the target movie.
- [- removeTimeRange:](<removetimerange(__).md>) — Removes the specified time range from a track.
- [- scaleTimeRange:toDuration:](<scaletimerange(__toduration_).md>) — Changes the duration of a time range in a track.
