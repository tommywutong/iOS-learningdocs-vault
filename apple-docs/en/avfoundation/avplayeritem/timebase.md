---
title: timebase
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/timebase
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/timebase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/timebase.json'
content_hash: 'sha256:c798fa2f6863aedb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# timebase

<sub>Instance Property</sub>

The timebase information for the item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var timebase: CMTimebase? { get }
```

## Discussion

The system uses timebase information to synchronize playback of the current item with the host clock. You can use this property to access the timebase information, but you can’t use it to set the time or the rate of playback.

If you need to respond to changes in the effective playback rate, listen for [kCMTimebaseNotification_EffectiveRateChanged](../../coremedia/kcmtimebasenotification_effectiveratechanged.md) notifications that the player item’s [timebase](timebase.md) posts. These notifications announce when the effective playback rate changes, which includes any compensation necessary for drifting behaviors of audio output hardware.

## See Also

### Accessing timing information

- [- currentTime](<currenttime().md>) — Returns the current time of the item.
- [- currentDate](<currentdate().md>) — Returns the current time of the item as a date.
- [duration](duration.md) — The duration of the item.
