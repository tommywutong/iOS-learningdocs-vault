---
title: timeRange
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassettrack/timerange
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/timerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/timerange.json'
content_hash: 'sha256:d79ac3d2d4ab3c95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# timeRange

<sub>Instance Property</sub>

The time range of the track within the overall timeline of the asset.

> [!warning] Deprecated
> Load the value of [timeRange](../avpartialasyncproperty/timerange.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeRange: CMTimeRange { get }
```

## Discussion

If the start of the time range is greater than [zero](../../coremedia/cmtime/zero.md), the track doesn’t initially have media data to present. This condition may occur when the media delays an audio track to align the start of audio with a specific video frame. You can test for this as the example below shows:

**Swift**

```swift
if track.timeRange.start > .zero {
    // Delayed start.
}
```

**Objective-C**

```objc
if CMTIME_COMPARE_INLINE(track.timeRange.start, >, kCMTimeZero) {
    // Delayed start.
}
```
