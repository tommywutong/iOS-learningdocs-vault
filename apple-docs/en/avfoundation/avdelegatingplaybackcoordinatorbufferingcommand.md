---
title: AVDelegatingPlaybackCoordinatorBufferingCommand
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdelegatingplaybackcoordinatorbufferingcommand
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorbufferingcommand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinatorbufferingcommand.json'
content_hash: 'sha256:436388e43280a38c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVDelegatingPlaybackCoordinatorBufferingCommand

<sub>Class</sub>

A command that indicates to start buffering data in preparation for playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVDelegatingPlaybackCoordinatorBufferingCommand
```

## Overview

When your app receives this command, update its user interface to indicate that playback is buffering.

## Relationships

- **Inherits From**: [AVDelegatingPlaybackCoordinatorPlaybackControlCommand](avdelegatingplaybackcoordinatorplaybackcontrolcommand.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing command details

- [anticipatedPlaybackRate](avdelegatingplaybackcoordinatorbufferingcommand/anticipatedplaybackrate.md) — The rate at which the coordinator expects the current item to play.
- [completionDueDate](avdelegatingplaybackcoordinatorbufferingcommand/completionduedate.md) — The deadline by which the coordinator expects the delegate to complete execution of a command.

## See Also

### Playback commands

- [AVDelegatingPlaybackCoordinatorPlaybackControlCommand](avdelegatingplaybackcoordinatorplaybackcontrolcommand.md) — An abstract superclass for playback commands.
- [AVDelegatingPlaybackCoordinatorPlayCommand](avdelegatingplaybackcoordinatorplaycommand.md) — A command that indicates to play at a specific rate and time.
- [AVDelegatingPlaybackCoordinatorPauseCommand](avdelegatingplaybackcoordinatorpausecommand.md) — A command that indicates to pause playback.
- [AVDelegatingPlaybackCoordinatorSeekCommand](avdelegatingplaybackcoordinatorseekcommand.md) — A command that indicates to seek to a new time in the item timeline.
