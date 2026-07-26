---
title: rateDidChangeNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferrendersynchronizer/ratedidchangenotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/ratedidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrendersynchronizer/ratedidchangenotification.json'
content_hash: 'sha256:e9b2713fd9e2b79f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md)

# rateDidChangeNotification

<sub>Type Property</sub>

The synchronizer’s rendering rate changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let rateDidChangeNotification: NSNotification.Name
```

## See Also

### Accessing time information

- [- currentTime](<currenttime().md>) — Returns the current time of the synchronizer.
- [timebase](timebase.md) — The synchronizer’s rendering timebase which determines how it interprets timestamps.
- [rate](rate.md) — The current playback rate.
- [- setRate:time:](<setrate(__time_).md>) — Sets the renderer’s time and rate.
- [- setRate:time:atHostTime:](<setrate(__time_athosttime_).md>) — Sets the playback rate and the relationship between the current time and host time.
- [delaysRateChangeUntilHasSufficientMediaData](delaysratechangeuntilhassufficientmediadata.md) — A Boolean value that Indicates whether the playback should start immediately on rate change requests.
