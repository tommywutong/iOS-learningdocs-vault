---
title: 'insertEmptyTimeRange(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecomposition/insertemptytimerange(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecomposition/insertemptytimerange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecomposition/insertemptytimerange%28_%3A%29.json'
content_hash: 'sha256:bb1ad8446b6796da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableComposition](../avmutablecomposition.md)

# insertEmptyTimeRange(_:)

<sub>Instance Method</sub>

Adds or extends an empty time range within all tracks of the composition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func insertEmptyTimeRange(_ timeRange: CMTimeRange)
```

## Parameters

- `timeRange` — The empty time range to insert.

## Discussion

Inserting an empty time range pushes out existing content by the time range’s duration. Use this method to reserve a time range in the composition for a subsequently created track to present its media.

## See Also

### Managing time ranges

- [- removeTimeRange:](<removetimerange(__).md>) — Removes a specified time range from all tracks of the composition.
- [- scaleTimeRange:toDuration:](<scaletimerange(__toduration_).md>) — Changes the duration of all tracks in a given time range.
- [- insertTimeRange:ofAsset:atTime:completionHandler:](<inserttimerange(__of_at_completionhandler_).md>) — Inserts all tracks of an asset for a time range into a composition. _(deprecated)_
- [- insertTimeRange:ofAsset:atTime:error:](<inserttimerange(__of_at_).md>) — Inserts all the tracks within a given time range of a specified asset into the composition. _(deprecated)_
