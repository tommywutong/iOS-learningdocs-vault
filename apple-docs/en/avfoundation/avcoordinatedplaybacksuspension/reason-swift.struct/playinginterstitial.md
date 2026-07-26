---
title: playingInterstitial
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcoordinatedplaybacksuspension/reason-swift.struct/playinginterstitial
source_url: 'https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybacksuspension/reason-swift.struct/playinginterstitial'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcoordinatedplaybacksuspension/reason-swift.struct/playinginterstitial.json'
content_hash: 'sha256:1080c1bb9f6bf4c4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCoordinatedPlaybackSuspension](../../avcoordinatedplaybacksuspension.md) · [Reason](../reason-swift.struct.md)

# playingInterstitial

<sub>Type Property</sub>

A participant is playing content other than the primary content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let playingInterstitial: AVCoordinatedPlaybackSuspension.Reason
```

## Discussion

Interstitials are content a player presents that’s unrelated to the primary content, such as advertisements and legal warnings.

## See Also

### Suspension reasons

- [AVCoordinatedPlaybackSuspensionReasonAudioSessionInterrupted](audiosessioninterrupted.md) — The system interrupts a participant’s audio session.
- [AVCoordinatedPlaybackSuspensionReasonCoordinatedPlaybackNotPossible](coordinatedplaybacknotpossible.md) — It’s not possible for a participant to start or resume coordinated playback.
- [AVCoordinatedPlaybackSuspensionReasonStallRecovery](stallrecovery.md) — The player object is buffering media data after a stall.
- [AVCoordinatedPlaybackSuspensionReasonUserActionRequired](useractionrequired.md) — A playback object requires user intervention to resume playback.
- [AVCoordinatedPlaybackSuspensionReasonUserIsChangingCurrentTime](userischangingcurrenttime.md) — A participant is actively changing the current time.
