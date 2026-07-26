---
title: 'participantLimitForWaitingOutSuspensions(withReason:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplaybackcoordinator/participantlimitforwaitingoutsuspensions(withreason:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/participantlimitforwaitingoutsuspensions(withreason:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplaybackcoordinator/participantlimitforwaitingoutsuspensions%28withreason%3A%29.json'
content_hash: 'sha256:d03079b88c658fb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlaybackCoordinator](../avplaybackcoordinator.md)

# participantLimitForWaitingOutSuspensions(withReason:)

<sub>Instance Method</sub>

Returns the limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func participantLimitForWaitingOutSuspensions(withReason reason: AVCoordinatedPlaybackSuspension.Reason) -> Int
```

## Parameters

- `reason` — The suspension reason to find a participant limit for.

## Return Value

The participant limit.

## See Also

### Configuring playback policies

- [- setParticipantLimit:forWaitingOutSuspensionsWithReason:](<setparticipantlimit(__forwaitingoutsuspensionswithreason_).md>) — Sets a limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.
- [suspensionReasonsThatTriggerWaiting](suspensionreasonsthattriggerwaiting.md) — The reasons that cause a coordinator to suspend playback.
- [pauseSnapsToMediaTimeOfOriginator](pausesnapstomediatimeoforiginator.md) — A Boolean value that indicates whether participants mirror the originator’s stop time when they pause.
