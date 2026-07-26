---
title: AVPlayer.TimeControlStatus
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/timecontrolstatus-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/timecontrolstatus-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/timecontrolstatus-swift.enum.json'
content_hash: 'sha256:99ba1e7d58c92c33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# AVPlayer.TimeControlStatus

<sub>Enumeration</sub>

Constants that indicate the state of playback control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum TimeControlStatus
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Status values

- [AVPlayerTimeControlStatusPaused](timecontrolstatus-swift.enum/paused.md) — A state that indicates the player paused playback indefinitely.
- [AVPlayerTimeControlStatusWaitingToPlayAtSpecifiedRate](timecontrolstatus-swift.enum/waitingtoplayatspecifiedrate.md) — A state that indicates that the player is waiting for network conditions to improve before it can start or resume playback.
- [AVPlayerTimeControlStatusPlaying](timecontrolstatus-swift.enum/playing.md) — A state that indicates that the player is currently playing media.

### Initializers

- [init(rawValue:)](<timecontrolstatus-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring waiting behavior

- [automaticallyWaitsToMinimizeStalling](automaticallywaitstominimizestalling.md) — A Boolean value that indicates whether the player should automatically delay playback in order to minimize stalling.
- [reasonForWaitingToPlay](reasonforwaitingtoplay.md) — The reason the player is currently waiting for playback to begin or resume.
- [WaitingReason](waitingreason.md) — The reasons a player is waiting to begin or resume playback.
- [timeControlStatus](timecontrolstatus-swift.property.md) — A value that indicates whether playback is in progress, paused indefinitely, or waiting for network conditions to improve.
- [- playImmediatelyAtRate:](<playimmediately(atrate_).md>) — Plays the available media data immediately, at the specified rate.
