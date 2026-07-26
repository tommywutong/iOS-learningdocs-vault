---
title: pauseSnapsToMediaTimeOfOriginator
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplaybackcoordinator/pausesnapstomediatimeoforiginator
source_url: 'https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/pausesnapstomediatimeoforiginator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplaybackcoordinator/pausesnapstomediatimeoforiginator.json'
content_hash: 'sha256:5b96367921da3fc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlaybackCoordinator](../avplaybackcoordinator.md)

# pauseSnapsToMediaTimeOfOriginator

<sub>Instance Property</sub>

A Boolean value that indicates whether participants mirror the originator’s stop time when they pause.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var pauseSnapsToMediaTimeOfOriginator: Bool { get set }
```

## Discussion

If this value is [true](../../swift/true.md), all participants seek to the originator’s stop time after they pause. Use this setting if it counteracts network delays that result from communicating the originator’s pause state to the other participants.

If this value is [false](../../swift/false.md), it’s acceptable for participants to stop at slightly different times, and a pause doesn’t cause the time of other participants to jump back.

## See Also

### Configuring playback policies

- [- participantLimitForWaitingOutSuspensionsWithReason:](<participantlimitforwaitingoutsuspensions(withreason_).md>) — Returns the limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.
- [- setParticipantLimit:forWaitingOutSuspensionsWithReason:](<setparticipantlimit(__forwaitingoutsuspensionswithreason_).md>) — Sets a limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.
- [suspensionReasonsThatTriggerWaiting](suspensionreasonsthattriggerwaiting.md) — The reasons that cause a coordinator to suspend playback.
