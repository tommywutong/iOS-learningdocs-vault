---
title: 'insertTimeRange(_:of:at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（18.0 起废弃）, iPadOS 4.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 1.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avmutablecomposition/inserttimerange(_:of:at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecomposition/inserttimerange(_:of:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecomposition/inserttimerange%28_%3Aof%3Aat%3A%29.json'
content_hash: 'sha256:839965835cc0c115'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableComposition](../avmutablecomposition.md)

# insertTimeRange(_:of:at:)

<sub>Instance Method</sub>

Inserts all the tracks within a given time range of a specified asset into the composition.

> [!warning] Deprecated
> Use [insertTimeRange(_:of:at:isolation:)](<inserttimerange(__of_at_isolation_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func insertTimeRange(_ timeRange: CMTimeRange, of asset: AVAsset, at startTime: CMTime) throws
```

## Parameters

- `timeRange` — The time range of the asset to be inserted.

- `asset` — An asset that contains the tracks to be inserted.

- `startTime` — The time at which the inserted tracks should be presented by the receiver.

## Discussion

This method may add new tracks to ensure that all tracks of the asset are represented in the inserted time range.

Existing content at the specified start time is pushed out by the duration of the time range.

Media data for the inserted time range is presented at its natural duration; you can scale it to a different duration using [- scaleTimeRange:toDuration:](<scaletimerange(__toduration_).md>).

## See Also

### Managing time ranges

- [- removeTimeRange:](<removetimerange(__).md>) — Removes a specified time range from all tracks of the composition.
- [- scaleTimeRange:toDuration:](<scaletimerange(__toduration_).md>) — Changes the duration of all tracks in a given time range.
- [- insertEmptyTimeRange:](<insertemptytimerange(__).md>) — Adds or extends an empty time range within all tracks of the composition.
- [- insertTimeRange:ofAsset:atTime:completionHandler:](<inserttimerange(__of_at_completionhandler_).md>) — Inserts all tracks of an asset for a time range into a composition. _(deprecated)_
