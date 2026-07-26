---
title: 'insertTimeRange(_:of:at:copySampleData:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovie/inserttimerange(_:of:at:copysampledata:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/inserttimerange(_:of:at:copysampledata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/inserttimerange%28_%3Aof%3Aat%3Acopysampledata%3A%29.json'
content_hash: 'sha256:3b5b4256fdf99bf1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# insertTimeRange(_:of:at:copySampleData:)

<sub>Instance Method</sub>

Inserts all of the tracks in a specified time range of an asset into a movie.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func insertTimeRange(_ timeRange: CMTimeRange, of asset: AVAsset, at startTime: CMTime, copySampleData: Bool) throws
```

## Parameters

- `timeRange` — The time range of the asset to be inserted.

- `asset` — An [AVAsset](../avasset.md) object indicating the source of the inserted media. This value can’t be `nil`.

- `startTime` — The time in the target movie at which the media is to be inserted.

- `copySampleData` — A Boolean value that indicates whether sample data is to be copied from the source to the destination during edits.

## Discussion

This method may add new tracks to the target movie to ensure that all tracks of the asset are represented in the inserted time range.

## See Also

### Managing time ranges

- [- insertEmptyTimeRange:](<insertemptytimerange(__).md>) — Adds an empty time range to a movie.
- [- scaleTimeRange:toDuration:](<scale(__toduration_).md>) — Changes the duration of a time range in a movie.
- [- removeTimeRange:](<removetimerange(__).md>) — Removes the specified time range from a movie.
