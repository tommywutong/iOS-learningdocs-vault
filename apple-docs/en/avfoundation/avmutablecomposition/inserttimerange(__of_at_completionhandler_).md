---
title: 'insertTimeRange(_:of:at:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+（18.0 起废弃）, iPadOS 16.0+（18.0 起废弃）, Mac Catalyst 16.0+（18.0 起废弃）, macOS 13.0+（15.0 起废弃）, tvOS 16.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 9.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avmutablecomposition/inserttimerange(_:of:at:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecomposition/inserttimerange(_:of:at:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecomposition/inserttimerange%28_%3Aof%3Aat%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:905099e473d210f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableComposition](../avmutablecomposition.md)

# insertTimeRange(_:of:at:completionHandler:)

<sub>Instance Method</sub>

Inserts all tracks of an asset for a time range into a composition.

> [!warning] Deprecated
> Use [insertTimeRange(_:of:at:isolation:)](<inserttimerange(__of_at_isolation_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func insertTimeRange(_ timeRange: CMTimeRange, of asset: AVAsset, at startTime: CMTime, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

## Parameters

- `timeRange` — The time range of the asset’s tracks to insert into the composition.

- `asset` — The source asset that contains the tracks to insert.

- `startTime` — A time in the composition to present the inserted tracks.

- `completionHandler` — A callback the system invokes when the insertion is complete. If an error occurs, the system passes the callback an error object that describes the failure.

## Discussion

If necessary, a composition adds new tracks to ensure that it inserts all tracks in the source asset for the time range. Inserting a time range pushes out existing content at the specified start time by the time range’s duration.

The composition presents the media data for the inserted time range at its natural duration and rate. You can scale it to a different duration, which changes the presentation rate, by calling [- scaleTimeRange:toDuration:](<scaletimerange(__toduration_).md>).

## See Also

### Managing time ranges

- [- removeTimeRange:](<removetimerange(__).md>) — Removes a specified time range from all tracks of the composition.
- [- scaleTimeRange:toDuration:](<scaletimerange(__toduration_).md>) — Changes the duration of all tracks in a given time range.
- [- insertEmptyTimeRange:](<insertemptytimerange(__).md>) — Adds or extends an empty time range within all tracks of the composition.
- [- insertTimeRange:ofAsset:atTime:error:](<inserttimerange(__of_at_).md>) — Inserts all the tracks within a given time range of a specified asset into the composition. _(deprecated)_
