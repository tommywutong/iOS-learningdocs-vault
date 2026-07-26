---
title: currentTime()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferrendersynchronizer/currenttime()
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/currenttime()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrendersynchronizer/currenttime%28%29.json'
content_hash: 'sha256:60b48bd2fb67f8b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md)

# currentTime()

<sub>Instance Method</sub>

Returns the current time of the synchronizer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func currentTime() -> CMTime
```

## Return Value

A [CMTime](../../coremedia/cmtime.md) object.

## See Also

### Accessing time information

- [timebase](timebase.md) — The synchronizer’s rendering timebase which determines how it interprets timestamps.
- [rate](rate.md) — The current playback rate.
- [- setRate:time:](<setrate(__time_).md>) — Sets the renderer’s time and rate.
- [- setRate:time:atHostTime:](<setrate(__time_athosttime_).md>) — Sets the playback rate and the relationship between the current time and host time.
- [AVSampleBufferRenderSynchronizerRateDidChangeNotification](ratedidchangenotification.md) — The synchronizer’s rendering rate changed.
- [delaysRateChangeUntilHasSufficientMediaData](delaysratechangeuntilhassufficientmediadata.md) — A Boolean value that Indicates whether the playback should start immediately on rate change requests.
