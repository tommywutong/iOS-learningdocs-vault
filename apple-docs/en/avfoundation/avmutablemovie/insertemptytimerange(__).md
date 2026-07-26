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
doc_path: '/documentation/avfoundation/avmutablemovie/insertemptytimerange(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/insertemptytimerange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/insertemptytimerange%28_%3A%29.json'
content_hash: 'sha256:588e431f2ac0fb2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# insertEmptyTimeRange(_:)

<sub>Instance Method</sub>

Adds an empty time range to a movie.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func insertEmptyTimeRange(_ timeRange: CMTimeRange)
```

## Parameters

- `timeRange` — The time range to be made empty.

## Discussion

You can’t add empty time ranges to the end of a movie.

## See Also

### Managing time ranges

- [- insertTimeRange:ofAsset:atTime:copySampleData:error:](<inserttimerange(__of_at_copysampledata_).md>) — Inserts all of the tracks in a specified time range of an asset into a movie.
- [- scaleTimeRange:toDuration:](<scale(__toduration_).md>) — Changes the duration of a time range in a movie.
- [- removeTimeRange:](<removetimerange(__).md>) — Removes the specified time range from a movie.
