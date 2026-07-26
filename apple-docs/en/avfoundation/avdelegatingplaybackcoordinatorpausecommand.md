---
title: AVDelegatingPlaybackCoordinatorPauseCommand
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdelegatingplaybackcoordinatorpausecommand
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorpausecommand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinatorpausecommand.json'
content_hash: 'sha256:272e61ccf17af06c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVDelegatingPlaybackCoordinatorPauseCommand

<sub>Class</sub>

A command that indicates to pause playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVDelegatingPlaybackCoordinatorPauseCommand
```

## Relationships

- **Inherits From**: [AVDelegatingPlaybackCoordinatorPlaybackControlCommand](avdelegatingplaybackcoordinatorplaybackcontrolcommand.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing command details

- [shouldBufferInAnticipationOfPlayback](avdelegatingplaybackcoordinatorpausecommand/shouldbufferinanticipationofplayback.md) — A Boolean value that indicates whether the player starts buffering in preparation for a request to begin playback.
- [anticipatedPlaybackRate](avdelegatingplaybackcoordinatorpausecommand/anticipatedplaybackrate.md) — The rate at which the coordinator expects the current item to play.

## See Also

### Playback commands

- [AVDelegatingPlaybackCoordinatorPlaybackControlCommand](avdelegatingplaybackcoordinatorplaybackcontrolcommand.md) — An abstract superclass for playback commands.
- [AVDelegatingPlaybackCoordinatorPlayCommand](avdelegatingplaybackcoordinatorplaycommand.md) — A command that indicates to play at a specific rate and time.
- [AVDelegatingPlaybackCoordinatorSeekCommand](avdelegatingplaybackcoordinatorseekcommand.md) — A command that indicates to seek to a new time in the item timeline.
- [AVDelegatingPlaybackCoordinatorBufferingCommand](avdelegatingplaybackcoordinatorbufferingcommand.md) — A command that indicates to start buffering data in preparation for playback.
