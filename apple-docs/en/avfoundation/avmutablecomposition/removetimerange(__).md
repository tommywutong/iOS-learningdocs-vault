---
title: 'removeTimeRange(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecomposition/removetimerange(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecomposition/removetimerange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecomposition/removetimerange%28_%3A%29.json'
content_hash: 'sha256:a412dcd9e7629bbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableComposition](../avmutablecomposition.md)

# removeTimeRange(_:)

<sub>Instance Method</sub>

Removes a specified time range from all tracks of the composition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeTimeRange(_ timeRange: CMTimeRange)
```

## Parameters

- `timeRange` — The time range to remove.

## Discussion

After removing, existing content after the time range moves forward in the composition timeline.

Removing a time range doesn’t remove any existing tracks from the composition, even if removing it results in an empty track. Instead, it removes or truncates track segments that intersect with the time range.

## See Also

### Managing time ranges

- [- scaleTimeRange:toDuration:](<scaletimerange(__toduration_).md>) — Changes the duration of all tracks in a given time range.
- [- insertEmptyTimeRange:](<insertemptytimerange(__).md>) — Adds or extends an empty time range within all tracks of the composition.
- [- insertTimeRange:ofAsset:atTime:completionHandler:](<inserttimerange(__of_at_completionhandler_).md>) — Inserts all tracks of an asset for a time range into a composition. _(deprecated)_
- [- insertTimeRange:ofAsset:atTime:error:](<inserttimerange(__of_at_).md>) — Inserts all the tracks within a given time range of a specified asset into the composition. _(deprecated)_
