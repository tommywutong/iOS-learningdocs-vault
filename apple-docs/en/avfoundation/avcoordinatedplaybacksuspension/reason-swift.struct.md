---
title: AVCoordinatedPlaybackSuspension.Reason
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcoordinatedplaybacksuspension/reason-swift.struct
source_url: 'https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybacksuspension/reason-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcoordinatedplaybacksuspension/reason-swift.struct.json'
content_hash: 'sha256:c28e572ece07825d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCoordinatedPlaybackSuspension](../avcoordinatedplaybacksuspension.md)

# AVCoordinatedPlaybackSuspension.Reason

<sub>Structure</sub>

Constants that identify playback suspension reasons.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct Reason
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Suspension reasons

- [AVCoordinatedPlaybackSuspensionReasonAudioSessionInterrupted](reason-swift.struct/audiosessioninterrupted.md) — The system interrupts a participant’s audio session.
- [AVCoordinatedPlaybackSuspensionReasonCoordinatedPlaybackNotPossible](reason-swift.struct/coordinatedplaybacknotpossible.md) — It’s not possible for a participant to start or resume coordinated playback.
- [AVCoordinatedPlaybackSuspensionReasonPlayingInterstitial](reason-swift.struct/playinginterstitial.md) — A participant is playing content other than the primary content.
- [AVCoordinatedPlaybackSuspensionReasonStallRecovery](reason-swift.struct/stallrecovery.md) — The player object is buffering media data after a stall.
- [AVCoordinatedPlaybackSuspensionReasonUserActionRequired](reason-swift.struct/useractionrequired.md) — A playback object requires user intervention to resume playback.
- [AVCoordinatedPlaybackSuspensionReasonUserIsChangingCurrentTime](reason-swift.struct/userischangingcurrenttime.md) — A participant is actively changing the current time.

### Initializers

- [init(_:)](<reason-swift.struct/init(__).md>) — Creates a suspension with a string.
- [init(rawValue:)](<reason-swift.struct/init(rawvalue_).md>) — Creates a suspension with a raw string value.

## See Also

### Inspecting a suspension

- [beginDate](begindate.md) — The time the suspension begins.
- [reason](reason-swift.property.md) — The reason for the suspension.
