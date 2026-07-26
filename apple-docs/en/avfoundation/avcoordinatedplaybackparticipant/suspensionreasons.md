---
title: suspensionReasons
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcoordinatedplaybackparticipant/suspensionreasons
source_url: 'https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybackparticipant/suspensionreasons'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcoordinatedplaybackparticipant/suspensionreasons.json'
content_hash: 'sha256:a801b41443f553fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCoordinatedPlaybackParticipant](../avcoordinatedplaybackparticipant.md)

# suspensionReasons

<sub>Instance Property</sub>

The reasons a participant isn’t currently participating in coordinated playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var suspensionReasons: [AVCoordinatedPlaybackSuspension.Reason] { get }
```

## Discussion

This value is empty if the participant’s playback isn’t in a suspended state.

## See Also

### Accessing participant status

- [identifier](identifier.md) — A unique identifier for the participant.
- [readyToPlay](isreadytoplay.md) — A Boolean value that indicates whether the participant is ready to start coordinated playback.
