---
title: error
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/error
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/error.json'
content_hash: 'sha256:cd1ad75d1f1bc3d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# error

<sub>Instance Property</sub>

The error that caused the player item to fail.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var error: (any Error)? { get }
```

## Discussion

The value of this property is an error that describes what caused the player item to no longer be able to be played.

If the receiver’s status is not [AVPlayerItemStatusFailed](status-swift.enum/failed.md), the value of this property is `nil`.

## See Also

### Determining readiness

- [status](status-swift.property.md) — The status of the player item.
- [Status](status-swift.enum.md) — The statuses for a player item.
