---
title: AVPlayerItem.Status
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/status-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/status-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/status-swift.enum.json'
content_hash: 'sha256:93fc89adb2c1020c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# AVPlayerItem.Status

<sub>Enumeration</sub>

The statuses for a player item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Status
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Player item statuses

- [AVPlayerItemStatusUnknown](status-swift.enum/unknown.md) — The item’s status is unknown.
- [AVPlayerItemStatusReadyToPlay](status-swift.enum/readytoplay.md) — The item is ready to play.
- [AVPlayerItemStatusFailed](status-swift.enum/failed.md) — The item no longer plays due to an error.

### Initializers

- [init(rawValue:)](<status-swift.enum/init(rawvalue_).md>)

## See Also

### Determining readiness

- [status](status-swift.property.md) — The status of the player item.
- [error](error.md) — The error that caused the player item to fail.
