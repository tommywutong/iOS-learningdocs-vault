---
title: identifier
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcoordinatedplaybackparticipant/identifier
source_url: 'https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybackparticipant/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcoordinatedplaybackparticipant/identifier.json'
content_hash: 'sha256:20e69e2fef2b969f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCoordinatedPlaybackParticipant](../avcoordinatedplaybackparticipant.md)

# identifier

<sub>Instance Property</sub>

A unique identifier for the participant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var identifier: UUID { get }
```

## See Also

### Accessing participant status

- [readyToPlay](isreadytoplay.md) — A Boolean value that indicates whether the participant is ready to start coordinated playback.
- [suspensionReasons](suspensionreasons.md) — The reasons a participant isn’t currently participating in coordinated playback.
