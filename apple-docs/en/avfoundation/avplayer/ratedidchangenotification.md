---
title: rateDidChangeNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/ratedidchangenotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/ratedidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/ratedidchangenotification.json'
content_hash: 'sha256:19ec475d000c1f90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# rateDidChangeNotification

<sub>Type Property</sub>

A notification that a player posts when its rate changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let rateDidChangeNotification: NSNotification.Name
```

## Discussion

Observing this notification is similar to key-value observing the rate property, except the notification provides additional information about the rate change in the user information dictionary.

## Topics

### User information keys

- [AVPlayerRateDidChangeOriginatingParticipantKey](ratedidchangeoriginatingparticipantkey.md) — A key to retrieve the identifier of the participant that originates the rate change.
- [AVPlayerRateDidChangeReasonKey](ratedidchangereasonkey.md) — A key to retrieve the reason for the rate change.
- [RateDidChangeReason](ratedidchangereason.md) — A structure that represents a rate change reason.

## See Also

### Controlling playback

- [defaultRate](defaultrate.md) — A default rate at which to begin playback.
- [- play](<play().md>) — Begins playback of the current item.
- [- pause](<pause().md>) — Pauses playback of the current item.
- [rate](rate.md) — The current playback rate.
- [AVPlayerRateDidChangeReasonPlayheadReachedLiveEdge](ratedidchangereason/playheadreachedliveedge.md) — Indicates that the player automatically switched the playback rate from \> 1.0 back to 1.0 when the playhead reached the live edge during live streaming.
- [AVPlayerRateDidChangeReasonReversePlaybackReachedStartOfSeekableRange](ratedidchangereason/reverseplaybackreachedstartofseekablerange.md) — Indicates that the player automatically switched rate to 1.0 when the reverse playback reached start of seekable range. only for live.
