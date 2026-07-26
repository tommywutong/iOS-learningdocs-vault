---
title: AVPlayerLooper.Status
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerlooper/status-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlooper/status-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlooper/status-swift.enum.json'
content_hash: 'sha256:95c7e3f57727ae4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerLooper](../avplayerlooper.md)

# AVPlayerLooper.Status

<sub>Enumeration</sub>

Status constants that indicate whether a looper can successfully perform looping playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Status
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Status values

- [AVPlayerLooperStatusUnknown](status-swift.enum/unknown.md) — The status isn’t known.
- [AVPlayerLooperStatusReady](status-swift.enum/ready.md) — The looper is ready to perform looping playback.
- [AVPlayerLooperStatusFailed](status-swift.enum/failed.md) — The looper isn’t able to perform looping playback due to an error.
- [AVPlayerLooperStatusCancelled](status-swift.enum/cancelled.md) — The app canceled looping on the player.

### Initializers

- [init(rawValue:)](<status-swift.enum/init(rawvalue_).md>)

## See Also

### Observing looping state

- [loopCount](loopcount.md) — The number of times the object played the media.
- [status](status-swift.property.md) — A status that indicates the object’s ability to loop playback.
