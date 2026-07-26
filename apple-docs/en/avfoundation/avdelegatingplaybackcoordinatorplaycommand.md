---
title: AVDelegatingPlaybackCoordinatorPlayCommand
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdelegatingplaybackcoordinatorplaycommand
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorplaycommand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinatorplaycommand.json'
content_hash: 'sha256:6b1d1bad9fa29774'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVDelegatingPlaybackCoordinatorPlayCommand

<sub>Class</sub>

A command that indicates to play at a specific rate and time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVDelegatingPlaybackCoordinatorPlayCommand
```

## Relationships

- **Inherits From**: [AVDelegatingPlaybackCoordinatorPlaybackControlCommand](avdelegatingplaybackcoordinatorplaybackcontrolcommand.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing command details

- [rate](avdelegatingplaybackcoordinatorplaycommand/rate.md) — A rate to use when starting playback.
- [itemTime](avdelegatingplaybackcoordinatorplaycommand/itemtime.md) — A time in the item timeline to use to begin playback.
- [hostClockTime](avdelegatingplaybackcoordinatorplaycommand/hostclocktime.md) — A host clock time to use to begin playback.

## See Also

### Playback commands

- [AVDelegatingPlaybackCoordinatorPlaybackControlCommand](avdelegatingplaybackcoordinatorplaybackcontrolcommand.md) — An abstract superclass for playback commands.
- [AVDelegatingPlaybackCoordinatorPauseCommand](avdelegatingplaybackcoordinatorpausecommand.md) — A command that indicates to pause playback.
- [AVDelegatingPlaybackCoordinatorSeekCommand](avdelegatingplaybackcoordinatorseekcommand.md) — A command that indicates to seek to a new time in the item timeline.
- [AVDelegatingPlaybackCoordinatorBufferingCommand](avdelegatingplaybackcoordinatorbufferingcommand.md) — A command that indicates to start buffering data in preparation for playback.
