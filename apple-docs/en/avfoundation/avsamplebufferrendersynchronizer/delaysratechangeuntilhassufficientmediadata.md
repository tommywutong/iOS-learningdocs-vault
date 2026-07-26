---
title: delaysRateChangeUntilHasSufficientMediaData
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 11.3+, tvOS 14.5+, visionOS 1.0+, watchOS 7.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferrendersynchronizer/delaysratechangeuntilhassufficientmediadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/delaysratechangeuntilhassufficientmediadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrendersynchronizer/delaysratechangeuntilhassufficientmediadata.json'
content_hash: 'sha256:d7c482f7142cf8bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md)

# delaysRateChangeUntilHasSufficientMediaData

<sub>Instance Property</sub>

A Boolean value that Indicates whether the playback should start immediately on rate change requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var delaysRateChangeUntilHasSufficientMediaData: Bool { get set }
```

## See Also

### Accessing time information

- [- currentTime](<currenttime().md>) — Returns the current time of the synchronizer.
- [timebase](timebase.md) — The synchronizer’s rendering timebase which determines how it interprets timestamps.
- [rate](rate.md) — The current playback rate.
- [- setRate:time:](<setrate(__time_).md>) — Sets the renderer’s time and rate.
- [- setRate:time:atHostTime:](<setrate(__time_athosttime_).md>) — Sets the playback rate and the relationship between the current time and host time.
- [AVSampleBufferRenderSynchronizerRateDidChangeNotification](ratedidchangenotification.md) — The synchronizer’s rendering rate changed.
