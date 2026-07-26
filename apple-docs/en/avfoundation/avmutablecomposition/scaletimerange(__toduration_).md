---
title: 'scaleTimeRange(_:toDuration:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecomposition/scaletimerange(_:toduration:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecomposition/scaletimerange(_:toduration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecomposition/scaletimerange%28_%3Atoduration%3A%29.json'
content_hash: 'sha256:e503dbf6687fe2c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableComposition](../avmutablecomposition.md)

# scaleTimeRange(_:toDuration:)

<sub>Instance Method</sub>

Changes the duration of all tracks in a given time range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scaleTimeRange(_ timeRange: CMTimeRange, toDuration duration: CMTime)
```

## Parameters

- `timeRange` — The time range of the composition to scale.

- `duration` — The new time range duration.

## Discussion

A composition presents each track segment affected by the scaling operation at a rate equal to `source.duration / target.duration` of its resulting time mapping.

## See Also

### Managing time ranges

- [- removeTimeRange:](<removetimerange(__).md>) — Removes a specified time range from all tracks of the composition.
- [- insertEmptyTimeRange:](<insertemptytimerange(__).md>) — Adds or extends an empty time range within all tracks of the composition.
- [- insertTimeRange:ofAsset:atTime:completionHandler:](<inserttimerange(__of_at_completionhandler_).md>) — Inserts all tracks of an asset for a time range into a composition. _(deprecated)_
- [- insertTimeRange:ofAsset:atTime:error:](<inserttimerange(__of_at_).md>) — Inserts all the tracks within a given time range of a specified asset into the composition. _(deprecated)_
