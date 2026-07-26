---
title: AVDelegatingPlaybackCoordinatorPlaybackControlCommand
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdelegatingplaybackcoordinatorplaybackcontrolcommand
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorplaybackcontrolcommand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinatorplaybackcontrolcommand.json'
content_hash: 'sha256:381950228764be66'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVDelegatingPlaybackCoordinatorPlaybackControlCommand

<sub>Class</sub>

An abstract superclass for playback commands.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVDelegatingPlaybackCoordinatorPlaybackControlCommand
```

## Overview

Playback commands inherit state that identifies their originator and applicable item.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVDelegatingPlaybackCoordinatorBufferingCommand](avdelegatingplaybackcoordinatorbufferingcommand.md), [AVDelegatingPlaybackCoordinatorPauseCommand](avdelegatingplaybackcoordinatorpausecommand.md), [AVDelegatingPlaybackCoordinatorPlayCommand](avdelegatingplaybackcoordinatorplaycommand.md), [AVDelegatingPlaybackCoordinatorSeekCommand](avdelegatingplaybackcoordinatorseekcommand.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing command details

- [expectedCurrentItemIdentifier](avdelegatingplaybackcoordinatorplaybackcontrolcommand/expectedcurrentitemidentifier.md) — An item identifier the coordinator issues the command for.
- [originator](avdelegatingplaybackcoordinatorplaybackcontrolcommand/originator.md) — The participant that causes the coordinator to issue the command.

## See Also

### Playback commands

- [AVDelegatingPlaybackCoordinatorPlayCommand](avdelegatingplaybackcoordinatorplaycommand.md) — A command that indicates to play at a specific rate and time.
- [AVDelegatingPlaybackCoordinatorPauseCommand](avdelegatingplaybackcoordinatorpausecommand.md) — A command that indicates to pause playback.
- [AVDelegatingPlaybackCoordinatorSeekCommand](avdelegatingplaybackcoordinatorseekcommand.md) — A command that indicates to seek to a new time in the item timeline.
- [AVDelegatingPlaybackCoordinatorBufferingCommand](avdelegatingplaybackcoordinatorbufferingcommand.md) — A command that indicates to start buffering data in preparation for playback.
