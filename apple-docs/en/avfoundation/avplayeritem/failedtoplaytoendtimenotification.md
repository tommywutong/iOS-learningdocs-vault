---
title: failedToPlayToEndTimeNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/failedtoplaytoendtimenotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/failedtoplaytoendtimenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/failedtoplaytoendtimenotification.json'
content_hash: 'sha256:2eb6831ff81985c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# failedToPlayToEndTimeNotification

<sub>Type Property</sub>

A notification that the system posts when a player item fails to play to its end time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let failedToPlayToEndTimeNotification: NSNotification.Name
```

## Discussion

The notification’s object is the player item that finished playing.

> [!important] Important
> The system may post this notification on a thread other than the one you use to register the observer.

## Topics

### Error keys

- [AVPlayerItemFailedToPlayToEndTimeErrorKey](../avplayeritemfailedtoplaytoendtimeerrorkey.md) — The key to retrieve the error object from the notification’s user information dictionary.

## See Also

### Observing notifications

- [AVPlayerItemDidPlayToEndTimeNotification](didplaytoendtimenotification.md) — A notification the system posts when a player item plays to its end time.
- [AVPlayerItemTimeJumpedNotification](timejumpednotification.md) — A notification the system posts when a player item’s time changes discontinuously.
- [AVPlayerItemPlaybackStalledNotification](playbackstallednotification.md) — A notification the system posts when a player item media doesn’t arrive in time to continue playback.
- [AVPlayerItemMediaSelectionDidChangeNotification](mediaselectiondidchangenotification.md) — A notification the player item posts when its media selection changes.
- [AVPlayerItemRecommendedTimeOffsetFromLiveDidChangeNotification](recommendedtimeoffsetfromlivedidchangenotification.md) — A notification the player item posts when its offset from the live time changes.
- [AVPlayerItemNewAccessLogEntryNotification](newaccesslogentrynotification.md) — A notification the system posts when a player item adds a new entry to its access log.
- [AVPlayerItemNewErrorLogEntryNotification](newerrorlogentrynotification.md) — A notification the system posts when a player item adds a new entry to its error log.
