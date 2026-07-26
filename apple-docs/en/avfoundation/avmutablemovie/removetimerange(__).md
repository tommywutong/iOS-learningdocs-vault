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
doc_path: '/documentation/avfoundation/avmutablemovie/removetimerange(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/removetimerange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/removetimerange%28_%3A%29.json'
content_hash: 'sha256:bcb080b7b2a29dfd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# removeTimeRange(_:)

<sub>Instance Method</sub>

Removes the specified time range from a movie.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func removeTimeRange(_ timeRange: CMTimeRange)
```

## Parameters

- `timeRange` — The time range to be removed.

## See Also

### Managing time ranges

- [- insertEmptyTimeRange:](<insertemptytimerange(__).md>) — Adds an empty time range to a movie.
- [- insertTimeRange:ofAsset:atTime:copySampleData:error:](<inserttimerange(__of_at_copysampledata_).md>) — Inserts all of the tracks in a specified time range of an asset into a movie.
- [- scaleTimeRange:toDuration:](<scale(__toduration_).md>) — Changes the duration of a time range in a movie.
