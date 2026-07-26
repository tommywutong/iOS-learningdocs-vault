---
title: timeRange
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontrack/timerange
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/timerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/timerange.json'
content_hash: 'sha256:3147ac9c64a6ab68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# timeRange

<sub>Instance Property</sub>

The time range of the track within the overall timeline of the asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeRange: CMTimeRange { get }
```

## Discussion

If the start of the time range is greater than [zero](../../coremedia/cmtime/zero.md), the track doesn’t initially have media data to present. This condition may occur when the media delays an audio track to align the start of audio with a specific video frame. You can test for this as the example below shows:

```swift
if track.timeRange.start > .zero {
    // Delayed start.
}
```

## See Also

### Accessing temporal information

- [naturalTimeScale](naturaltimescale.md) — The natural time scale of the media that a track references.
- [estimatedDataRate](estimateddatarate.md) — The estimated data rate, in bits per second, of the media that the track references.
- [- samplePresentationTimeForTrackTime:](<samplepresentationtime(fortracktime_).md>) — Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.
