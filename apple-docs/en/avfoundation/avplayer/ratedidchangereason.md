---
title: AVPlayer.RateDidChangeReason
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/ratedidchangereason
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/ratedidchangereason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/ratedidchangereason.json'
content_hash: 'sha256:0d821bc8ed554842'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# AVPlayer.RateDidChangeReason

<sub>Structure</sub>

A structure that represents a rate change reason.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RateDidChangeReason
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(rawValue:)](<ratedidchangereason/init(rawvalue_).md>) — Creates a reason with a string value.

### Rate change reasons

- [AVPlayerRateDidChangeReasonAppBackgrounded](ratedidchangereason/appbackgrounded.md) — An app transitions to the background.
- [AVPlayerRateDidChangeReasonAudioSessionInterrupted](ratedidchangereason/audiosessioninterrupted.md) — The system interrupts the app’s audio session.
- [AVPlayerRateDidChangeReasonSetRateCalled](ratedidchangereason/setratecalled.md) — An app makes a call to set the player’s rate.
- [AVPlayerRateDidChangeReasonSetRateFailed](ratedidchangereason/setratefailed.md) — An attempt to change the player’s rate fails.

## See Also

### User information keys

- [AVPlayerRateDidChangeOriginatingParticipantKey](ratedidchangeoriginatingparticipantkey.md) — A key to retrieve the identifier of the participant that originates the rate change.
- [AVPlayerRateDidChangeReasonKey](ratedidchangereasonkey.md) — A key to retrieve the reason for the rate change.
