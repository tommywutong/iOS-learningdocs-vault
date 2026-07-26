---
title: suspensionReasonsThatTriggerWaiting
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplaybackcoordinator/suspensionreasonsthattriggerwaiting
source_url: 'https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/suspensionreasonsthattriggerwaiting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplaybackcoordinator/suspensionreasonsthattriggerwaiting.json'
content_hash: 'sha256:c15e670449481db3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlaybackCoordinator](../avplaybackcoordinator.md)

# suspensionReasonsThatTriggerWaiting

<sub>Instance Property</sub>

The reasons that cause a coordinator to suspend playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var suspensionReasonsThatTriggerWaiting: [AVCoordinatedPlaybackSuspension.Reason] { get set }
```

## See Also

### Configuring playback policies

- [- participantLimitForWaitingOutSuspensionsWithReason:](<participantlimitforwaitingoutsuspensions(withreason_).md>) — Returns the limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.
- [- setParticipantLimit:forWaitingOutSuspensionsWithReason:](<setparticipantlimit(__forwaitingoutsuspensionswithreason_).md>) — Sets a limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.
- [pauseSnapsToMediaTimeOfOriginator](pausesnapstomediatimeoforiginator.md) — A Boolean value that indicates whether participants mirror the originator’s stop time when they pause.
