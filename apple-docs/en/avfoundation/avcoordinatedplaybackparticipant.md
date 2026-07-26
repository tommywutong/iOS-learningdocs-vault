---
title: AVCoordinatedPlaybackParticipant
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcoordinatedplaybackparticipant
source_url: 'https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybackparticipant'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcoordinatedplaybackparticipant.json'
content_hash: 'sha256:1330133fc9bd245d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCoordinatedPlaybackParticipant

<sub>Class</sub>

An object that represents a participant in a coordinated playback session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVCoordinatedPlaybackParticipant
```

## Overview

Access the other participants in a session through the playback coordinator’s [otherParticipants](avplaybackcoordinator/otherparticipants.md) property to determine their playback readiness and suspension reasons.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing participant status

- [identifier](avcoordinatedplaybackparticipant/identifier.md) — A unique identifier for the participant.
- [readyToPlay](avcoordinatedplaybackparticipant/isreadytoplay.md) — A Boolean value that indicates whether the participant is ready to start coordinated playback.
- [suspensionReasons](avcoordinatedplaybackparticipant/suspensionreasons.md) — The reasons a participant isn’t currently participating in coordinated playback.

## See Also

### Observing other participants

- [otherParticipants](avplaybackcoordinator/otherparticipants.md) — The identifiers of the other participants in a group.
- [AVPlaybackCoordinatorOtherParticipantsDidChangeNotification](avplaybackcoordinator/otherparticipantsdidchangenotification.md) — A notification that the coordinator posts when its other participants change.
