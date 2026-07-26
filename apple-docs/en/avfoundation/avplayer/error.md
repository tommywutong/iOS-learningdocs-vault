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
doc_path: /documentation/avfoundation/avplayer/error
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/error.json'
content_hash: 'sha256:c1e4ec243c1c3a83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# error

<sub>Instance Property</sub>

An error that caused a failure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var error: (any Error)? { get }
```

## Discussion

By default, this value is `nil`. If a player reaches a [AVPlayerStatusFailed](status-swift.enum/failed.md), the system populates this value with an error that describes the failure.

## See Also

### Determining player readiness

- [status](status-swift.property.md) — A value that indicates the readiness of a player object for playback.
- [Status](status-swift.enum.md) — Status values that indicate whether a player can successfully play media.
