---
title: timeJumpedOriginatingParticipantKey
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/timejumpedoriginatingparticipantkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/timejumpedoriginatingparticipantkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/timejumpedoriginatingparticipantkey.json'
content_hash: 'sha256:be002fdd458b218b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# timeJumpedOriginatingParticipantKey

<sub>Type Property</sub>

A key to retrieve a unique identifier of the participant that caused the time jump.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class let timeJumpedOriginatingParticipantKey: String
```

## Discussion

Use this key to retrieve a UUID value for the participant in a coordinated playback session that caused the time jump. The returned UUID reresents a value in the playback coordinator’s [otherParticipants](../avplaybackcoordinator/otherparticipants.md) array.
