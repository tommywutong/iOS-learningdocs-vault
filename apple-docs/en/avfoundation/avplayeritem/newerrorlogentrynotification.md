---
title: newErrorLogEntryNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/newerrorlogentrynotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/newerrorlogentrynotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/newerrorlogentrynotification.json'
content_hash: 'sha256:0cf29a05d4949884'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# newErrorLogEntryNotification

<sub>Type Property</sub>

A notification the system posts when a player item adds a new entry to its error log.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let newErrorLogEntryNotification: NSNotification.Name
```

## Discussion

The notification’s object is the player item.

> [!important] Important
> The system may post this notification on a thread other than the one you use to register the observer.

## See Also

### Observing notifications

- [AVPlayerItemDidPlayToEndTimeNotification](didplaytoendtimenotification.md) — A notification the system posts when a player item plays to its end time.
- [AVPlayerItemFailedToPlayToEndTimeNotification](failedtoplaytoendtimenotification.md) — A notification that the system posts when a player item fails to play to its end time.
- [AVPlayerItemTimeJumpedNotification](timejumpednotification.md) — A notification the system posts when a player item’s time changes discontinuously.
- [AVPlayerItemPlaybackStalledNotification](playbackstallednotification.md) — A notification the system posts when a player item media doesn’t arrive in time to continue playback.
- [AVPlayerItemMediaSelectionDidChangeNotification](mediaselectiondidchangenotification.md) — A notification the player item posts when its media selection changes.
- [AVPlayerItemRecommendedTimeOffsetFromLiveDidChangeNotification](recommendedtimeoffsetfromlivedidchangenotification.md) — A notification the player item posts when its offset from the live time changes.
- [AVPlayerItemNewAccessLogEntryNotification](newaccesslogentrynotification.md) — A notification the system posts when a player item adds a new entry to its access log.
