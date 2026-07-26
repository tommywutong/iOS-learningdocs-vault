---
title: 'setParticipantLimit(_:forWaitingOutSuspensionsWithReason:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplaybackcoordinator/setparticipantlimit(_:forwaitingoutsuspensionswithreason:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/setparticipantlimit(_:forwaitingoutsuspensionswithreason:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplaybackcoordinator/setparticipantlimit%28_%3Aforwaitingoutsuspensionswithreason%3A%29.json'
content_hash: 'sha256:3aff5ac44dbc4740'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlaybackCoordinator](../avplaybackcoordinator.md)

# setParticipantLimit(_:forWaitingOutSuspensionsWithReason:)

<sub>Instance Method</sub>

Sets a limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setParticipantLimit(_ participantLimit: Int, forWaitingOutSuspensionsWithReason reason: AVCoordinatedPlaybackSuspension.Reason)
```

## Parameters

- `participantLimit` — The number of participants.

- `reason` — The suspension reason to set a limit for.

## Discussion

This method provides additional configuration of the values your app sets for the [suspensionReasonsThatTriggerWaiting](suspensionreasonsthattriggerwaiting.md) property. When a coordinator decides whether one participant’s suspensions cause others to wait, it also considers any participant limits that you set on the group.

## See Also

### Configuring playback policies

- [- participantLimitForWaitingOutSuspensionsWithReason:](<participantlimitforwaitingoutsuspensions(withreason_).md>) — Returns the limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.
- [suspensionReasonsThatTriggerWaiting](suspensionreasonsthattriggerwaiting.md) — The reasons that cause a coordinator to suspend playback.
- [pauseSnapsToMediaTimeOfOriginator](pausesnapstomediatimeoforiginator.md) — A Boolean value that indicates whether participants mirror the originator’s stop time when they pause.
