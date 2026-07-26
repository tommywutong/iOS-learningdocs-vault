---
title: 'scale(_:toDuration:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovie/scale(_:toduration:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/scale(_:toduration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/scale%28_%3Atoduration%3A%29.json'
content_hash: 'sha256:3b66db411860290c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# scale(_:toDuration:)

<sub>Instance Method</sub>

Changes the duration of a time range in a movie.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func scale(_ timeRange: CMTimeRange, toDuration duration: CMTime)
```

## Parameters

- `timeRange` — The time range to be changed.

- `duration` — The new duration for the time range.

## See Also

### Managing time ranges

- [- insertEmptyTimeRange:](<insertemptytimerange(__).md>) — Adds an empty time range to a movie.
- [- insertTimeRange:ofAsset:atTime:copySampleData:error:](<inserttimerange(__of_at_copysampledata_).md>) — Inserts all of the tracks in a specified time range of an asset into a movie.
- [- removeTimeRange:](<removetimerange(__).md>) — Removes the specified time range from a movie.
