---
title: otherParticipants
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplaybackcoordinator/otherparticipants
source_url: 'https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/otherparticipants'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplaybackcoordinator/otherparticipants.json'
content_hash: 'sha256:31c79510ba17d1a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlaybackCoordinator](../avplaybackcoordinator.md)

# otherParticipants

<sub>Instance Property</sub>

The identifiers of the other participants in a group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var otherParticipants: [AVCoordinatedPlaybackParticipant] { get }
```

## Discussion

Use this property value to create a user interface that informs the user about the state of other participants in the group.

> [!note] Note
> To observe changes to this property value, register for notifications of type [AVPlaybackCoordinatorOtherParticipantsDidChangeNotification](otherparticipantsdidchangenotification.md).

## See Also

### Observing other participants

- [AVCoordinatedPlaybackParticipant](../avcoordinatedplaybackparticipant.md) — An object that represents a participant in a coordinated playback session.
- [AVPlaybackCoordinatorOtherParticipantsDidChangeNotification](otherparticipantsdidchangenotification.md) — A notification that the coordinator posts when its other participants change.
