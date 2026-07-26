---
title: 'segment(forTrackTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassettrack/segment(fortracktime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/segment(fortracktime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/segment%28fortracktime%3A%29.json'
content_hash: 'sha256:c76cb1240724083e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# segment(forTrackTime:)

<sub>Instance Method</sub>

Retrieves a segment with a target time range that contains, or is closest to, the specified track time.

> [!warning] Deprecated
> Use [- loadSegmentForTrackTime:completionHandler:](<loadsegment(fortracktime_completionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func segment(forTrackTime trackTime: CMTime) -> AVAssetTrackSegment?
```

## Parameters

- `trackTime` — The track time for which you want the segment.

## Return Value

The track segment matching, or closest to, the specied time.

## Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load a segment asynchronously using [- loadSegmentForTrackTime:completionHandler:](<loadsegment(fortracktime_completionhandler_).md>) instead.
