---
title: segments
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/segments
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/segments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/segments.json'
content_hash: 'sha256:e7bc21814db166d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# segments

<sub>Type Property</sub>

The time mappings from the track’s media samples to its timeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var segments: AVAsyncProperty<Root, [AVAssetTrackSegment]> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

## See Also

### Loading track segments

- [- loadSegmentForTrackTime:completionHandler:](<../avassettrack/loadsegment(fortracktime_completionhandler_).md>) — Loads a segment with a target time range that contains, or is closest to, the specified track time.
- [- loadSamplePresentationTimeForTrackTime:completionHandler:](<../avassettrack/loadsamplepresentationtime(fortracktime_completionhandler_).md>) — Loads a sample presentation time that maps to the specified track time.
- [AVAssetTrackSegment](../avassettracksegment.md) — An object that represents a time range segment of an asset track.
