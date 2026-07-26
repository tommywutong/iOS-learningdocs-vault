---
title: timebase
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferrendersynchronizer/timebase
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/timebase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrendersynchronizer/timebase.json'
content_hash: 'sha256:d1f52edea137d030'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md)

# timebase

<sub>Instance Property</sub>

The synchronizer’s rendering timebase which determines how it interprets timestamps.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timebase: CMTimebase { get }
```

## Discussion

The default for this property is the clock for an added [AVSampleBufferAudioRenderer](../avsamplebufferaudiorenderer.md) object. If you haven’t added a renderer, the timebase is the system host clock.

## See Also

### Accessing time information

- [- currentTime](<currenttime().md>) — Returns the current time of the synchronizer.
- [rate](rate.md) — The current playback rate.
- [- setRate:time:](<setrate(__time_).md>) — Sets the renderer’s time and rate.
- [- setRate:time:atHostTime:](<setrate(__time_athosttime_).md>) — Sets the playback rate and the relationship between the current time and host time.
- [AVSampleBufferRenderSynchronizerRateDidChangeNotification](ratedidchangenotification.md) — The synchronizer’s rendering rate changed.
- [delaysRateChangeUntilHasSufficientMediaData](delaysratechangeuntilhassufficientmediadata.md) — A Boolean value that Indicates whether the playback should start immediately on rate change requests.
