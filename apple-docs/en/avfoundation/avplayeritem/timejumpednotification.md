---
title: timeJumpedNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/timejumpednotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/timejumpednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/timejumpednotification.json'
content_hash: 'sha256:3740783900b9b2ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# timeJumpedNotification

<sub>Type Property</sub>

A notification the system posts when a player item’s time changes discontinuously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let timeJumpedNotification: NSNotification.Name
```

## Discussion

The notification’s object is the player item.

> [!important] Important
> The system may post this notification on a thread other than the one you use to register the observer.

## Topics

### User information keys

- [AVPlayerItemTimeJumpedOriginatingParticipantKey](timejumpedoriginatingparticipantkey.md) — A key to retrieve a unique identifier of the participant that caused the time jump.

## See Also

### Observing notifications

- [AVPlayerItemDidPlayToEndTimeNotification](didplaytoendtimenotification.md) — A notification the system posts when a player item plays to its end time.
- [AVPlayerItemFailedToPlayToEndTimeNotification](failedtoplaytoendtimenotification.md) — A notification that the system posts when a player item fails to play to its end time.
- [AVPlayerItemPlaybackStalledNotification](playbackstallednotification.md) — A notification the system posts when a player item media doesn’t arrive in time to continue playback.
- [AVPlayerItemMediaSelectionDidChangeNotification](mediaselectiondidchangenotification.md) — A notification the player item posts when its media selection changes.
- [AVPlayerItemRecommendedTimeOffsetFromLiveDidChangeNotification](recommendedtimeoffsetfromlivedidchangenotification.md) — A notification the player item posts when its offset from the live time changes.
- [AVPlayerItemNewAccessLogEntryNotification](newaccesslogentrynotification.md) — A notification the system posts when a player item adds a new entry to its access log.
- [AVPlayerItemNewErrorLogEntryNotification](newerrorlogentrynotification.md) — A notification the system posts when a player item adds a new entry to its error log.
