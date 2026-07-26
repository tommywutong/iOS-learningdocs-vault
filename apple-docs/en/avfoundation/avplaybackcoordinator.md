---
title: AVPlaybackCoordinator
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplaybackcoordinator
source_url: 'https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplaybackcoordinator.json'
content_hash: 'sha256:25d48fb26ecf0cbd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlaybackCoordinator

<sub>Class</sub>

An object that coordinates the playback of players in a connected group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVPlaybackCoordinator
```

## Overview

The framework provides two playback coordinator subclasses that manage different types of player objects:

- [AVPlayerPlaybackCoordinator](avplayerplaybackcoordinator.md) coordinates the state of [AVPlayer](avplayer.md) objects. If your app uses [AVPlayer](avplayer.md), continue to use its standard interfaces to control playback. The coordinator intercepts changes to the player’s rate and time, and propagates them to other players in the group.
- [AVDelegatingPlaybackCoordinator](avdelegatingplaybackcoordinator.md) coordinates the state of custom player objects. If your app uses a custom player, such as one that renders media using [AVSampleBufferDisplayLayer](avsamplebufferdisplaylayer.md) and [AVSampleBufferAudioRenderer](avsamplebufferaudiorenderer.md), use this object to coordinate group playback. Adopt the coordinator’s delegate protocol so that your player responds to the commands that the coordinator issues.

> [!note] Note
> Use the [Group Activities](../groupactivities.md) framework to connect a playback coordinator to its peers.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVDelegatingPlaybackCoordinator](avdelegatingplaybackcoordinator.md), [AVPlayerPlaybackCoordinator](avplayerplaybackcoordinator.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring playback policies

- [- participantLimitForWaitingOutSuspensionsWithReason:](<avplaybackcoordinator/participantlimitforwaitingoutsuspensions(withreason_).md>) — Returns the limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.
- [- setParticipantLimit:forWaitingOutSuspensionsWithReason:](<avplaybackcoordinator/setparticipantlimit(__forwaitingoutsuspensionswithreason_).md>) — Sets a limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.
- [suspensionReasonsThatTriggerWaiting](avplaybackcoordinator/suspensionreasonsthattriggerwaiting.md) — The reasons that cause a coordinator to suspend playback.
- [pauseSnapsToMediaTimeOfOriginator](avplaybackcoordinator/pausesnapstomediatimeoforiginator.md) — A Boolean value that indicates whether participants mirror the originator’s stop time when they pause.

### Suspending state coordination

- [- beginSuspensionForReason:](<avplaybackcoordinator/beginsuspension(for_).md>) — Tells the coordinator to stop sending playback commands temporarily when the playback object disconnects from the group activity.
- [AVCoordinatedPlaybackSuspension](avcoordinatedplaybacksuspension.md) — An object that represents a temporary suspension of coordinated playback.
- [- expectedItemTimeAtHostTime:](<avplaybackcoordinator/expecteditemtime(athosttime_).md>) — Returns a time in the current item’s timeline that the coordinator expects to play at the specified host time.

### Observing suspension reasons

- [suspensionReasons](avplaybackcoordinator/suspensionreasons.md) — The reasons a coordinator is currently unable to participate in a group playback activity.
- [AVPlaybackCoordinatorSuspensionReasonsDidChangeNotification](avplaybackcoordinator/suspensionreasonsdidchangenotification.md) — A notification that the coordinator posts when its suspension reasons change.

### Observing other participants

- [otherParticipants](avplaybackcoordinator/otherparticipants.md) — The identifiers of the other participants in a group.
- [AVCoordinatedPlaybackParticipant](avcoordinatedplaybackparticipant.md) — An object that represents a participant in a coordinated playback session.
- [AVPlaybackCoordinatorOtherParticipantsDidChangeNotification](avplaybackcoordinator/otherparticipantsdidchangenotification.md) — A notification that the coordinator posts when its other participants change.

### Coordinating with group sessions

- [coordinateWithSession(_:)](<avplaybackcoordinator/coordinatewithsession(__).md>) — Begins coordination of a player with a group session.

## See Also

### SharePlay

- [Destination Video](../visionos/destination-video.md) — Leverage SwiftUI to build an immersive media experience in a multiplatform app.
- [Supporting coordinated media playback](supporting-coordinated-media-playback.md) — Create synchronized media experiences that enable users to watch and listen across devices.
- [AVPlayerPlaybackCoordinator](avplayerplaybackcoordinator.md) — A playback coordinator subclass that coordinates the playback of player objects in a connected group.
- [AVDelegatingPlaybackCoordinator](avdelegatingplaybackcoordinator.md) — A playback coordinator subclass that coordinates the playback of custom player objects in a connected group.
- [AVPlaybackCoordinationMedium](avplaybackcoordinationmedium.md) — The AVPlaybackCoordinationMedium passes states and messages between its connected playback coordinators.
