---
title: recommendedTimeOffsetFromLiveDidChangeNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/recommendedtimeoffsetfromlivedidchangenotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/recommendedtimeoffsetfromlivedidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/recommendedtimeoffsetfromlivedidchangenotification.json'
content_hash: 'sha256:ea44f86e7b96360b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# recommendedTimeOffsetFromLiveDidChangeNotification

<sub>Type Property</sub>

A notification the player item posts when its offset from the live time changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let recommendedTimeOffsetFromLiveDidChangeNotification: NSNotification.Name
```

## Discussion

Register to observe notifications of this type to observe changes to the value of the [recommendedTimeOffsetFromLive](recommendedtimeoffsetfromlive.md) property.

## See Also

### Observing notifications

- [AVPlayerItemDidPlayToEndTimeNotification](didplaytoendtimenotification.md) — A notification the system posts when a player item plays to its end time.
- [AVPlayerItemFailedToPlayToEndTimeNotification](failedtoplaytoendtimenotification.md) — A notification that the system posts when a player item fails to play to its end time.
- [AVPlayerItemTimeJumpedNotification](timejumpednotification.md) — A notification the system posts when a player item’s time changes discontinuously.
- [AVPlayerItemPlaybackStalledNotification](playbackstallednotification.md) — A notification the system posts when a player item media doesn’t arrive in time to continue playback.
- [AVPlayerItemMediaSelectionDidChangeNotification](mediaselectiondidchangenotification.md) — A notification the player item posts when its media selection changes.
- [AVPlayerItemNewAccessLogEntryNotification](newaccesslogentrynotification.md) — A notification the system posts when a player item adds a new entry to its access log.
- [AVPlayerItemNewErrorLogEntryNotification](newerrorlogentrynotification.md) — A notification the system posts when a player item adds a new entry to its error log.
