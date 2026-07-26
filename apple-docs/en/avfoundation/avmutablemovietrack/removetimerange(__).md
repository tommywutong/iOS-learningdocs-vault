---
title: 'removeTimeRange(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovietrack/removetimerange(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/removetimerange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/removetimerange%28_%3A%29.json'
content_hash: 'sha256:a34f159cbb4fa922'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# removeTimeRange(_:)

<sub>Instance Method</sub>

Removes the specified time range from a track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func removeTimeRange(_ timeRange: CMTimeRange)
```

## Parameters

- `timeRange` — The time range to remove.

## See Also

### Managing time ranges

- [- insertTimeRange:ofTrack:atTime:copySampleData:error:](<inserttimerange(__of_at_copysampledata_).md>) — Inserts a portion of an asset track into the target movie.
- [- insertEmptyTimeRange:](<insertemptytimerange(__).md>) — Adds an empty time range to a track.
- [- scaleTimeRange:toDuration:](<scaletimerange(__toduration_).md>) — Changes the duration of a time range in a track.
