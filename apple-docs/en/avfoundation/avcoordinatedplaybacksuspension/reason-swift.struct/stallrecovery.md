---
title: stallRecovery
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcoordinatedplaybacksuspension/reason-swift.struct/stallrecovery
source_url: 'https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybacksuspension/reason-swift.struct/stallrecovery'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcoordinatedplaybacksuspension/reason-swift.struct/stallrecovery.json'
content_hash: 'sha256:21bc62a396a97ac7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCoordinatedPlaybackSuspension](../../avcoordinatedplaybacksuspension.md) · [Reason](../reason-swift.struct.md)

# stallRecovery

<sub>Type Property</sub>

The player object is buffering media data after a stall.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let stallRecovery: AVCoordinatedPlaybackSuspension.Reason
```

## See Also

### Suspension reasons

- [AVCoordinatedPlaybackSuspensionReasonAudioSessionInterrupted](audiosessioninterrupted.md) — The system interrupts a participant’s audio session.
- [AVCoordinatedPlaybackSuspensionReasonCoordinatedPlaybackNotPossible](coordinatedplaybacknotpossible.md) — It’s not possible for a participant to start or resume coordinated playback.
- [AVCoordinatedPlaybackSuspensionReasonPlayingInterstitial](playinginterstitial.md) — A participant is playing content other than the primary content.
- [AVCoordinatedPlaybackSuspensionReasonUserActionRequired](useractionrequired.md) — A playback object requires user intervention to resume playback.
- [AVCoordinatedPlaybackSuspensionReasonUserIsChangingCurrentTime](userischangingcurrenttime.md) — A participant is actively changing the current time.
