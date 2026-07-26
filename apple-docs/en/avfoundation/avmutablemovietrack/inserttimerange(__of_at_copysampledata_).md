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
doc_path: '/documentation/avfoundation/avmutablemovietrack/inserttimerange(_:of:at:copysampledata:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/inserttimerange(_:of:at:copysampledata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/inserttimerange%28_%3Aof%3Aat%3Acopysampledata%3A%29.json'
content_hash: 'sha256:179140f972aaeabb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# insertTimeRange(_:of:at:copySampleData:)

<sub>Instance Method</sub>

Inserts a portion of an asset track into the target movie.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func insertTimeRange(_ timeRange: CMTimeRange, of track: AVAssetTrack, at startTime: CMTime, copySampleData: Bool) throws
```

## Parameters

- `timeRange` — The time range of the track to insert.

- `track` — An [AVAssetTrack](../avassettrack.md) object indicating the source of the inserted media. This value can’t be `nil`.

- `startTime` — The time in the target track at which the media is to be inserted.

- `copySampleData` — A Boolean value that indicates whether sample data is to be copied from the source to the destination during edits. If `YES`, the sample data is written to the location specified by the track property `mediaDataStorage` if non-nil, or else by the movie property `defaultMediaDataStorage` if non-nil; if both are nil, the method fails and returns `NO`. If `NO`, sample data isn’t written and sample references to the samples in their original container are added as necessary.

## See Also

### Managing time ranges

- [- insertEmptyTimeRange:](<insertemptytimerange(__).md>) — Adds an empty time range to a track.
- [- removeTimeRange:](<removetimerange(__).md>) — Removes the specified time range from a track.
- [- scaleTimeRange:toDuration:](<scaletimerange(__toduration_).md>) — Changes the duration of a time range in a track.
