---
title: duration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/duration
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/duration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/duration.json'
content_hash: 'sha256:f3bf09aaaa92f87e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# duration

<sub>Instance Property</sub>

The duration of the item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var duration: CMTime { get }
```

## Discussion

This property indicates the duration of the item, not considering either its [forwardPlaybackEndTime](forwardplaybackendtime.md) or [reversePlaybackEndTime](reverseplaybackendtime.md).

The system reports the value of this property as [indefinite](../../coremedia/cmtime/indefinite.md) until it loads the duration of the underlying asset. There are two ways to make sure you don’t access the value of duration until the system makes it available:

- Wait until the [status](status-swift.property.md) of the player item is [AVPlayerItemStatusReadyToPlay](status-swift.enum/readytoplay.md).
- Register for key-value observation of the property and request the initial value. If the system reports the initial value as [indefinite](../../coremedia/cmtime/indefinite.md), wait for the player item to notify you when [duration](duration.md) becomes available.

> [!note] Note
> The value of [duration](duration.md) may remain [indefinite](../../coremedia/cmtime/indefinite.md) for live streams.

## See Also

### Accessing timing information

- [- currentTime](<currenttime().md>) — Returns the current time of the item.
- [- currentDate](<currentdate().md>) — Returns the current time of the item as a date.
- [timebase](timebase.md) — The timebase information for the item.
