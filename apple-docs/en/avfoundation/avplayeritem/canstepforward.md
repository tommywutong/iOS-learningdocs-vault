---
title: canStepForward
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/canstepforward
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/canstepforward'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/canstepforward.json'
content_hash: 'sha256:1a811db1ca2e233f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# canStepForward

<sub>Instance Property</sub>

A Boolean value that indicates whether the item supports stepping forward.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var canStepForward: Bool { get }
```

## Discussion

Once the item becomes ready to play, the value of this property does not change. This behavior applies even when boundary conditions, such as when the item’s current time is equal to its end time, have been reached.

## See Also

### Stepping through media

- [canStepBackward](canstepbackward.md) — A Boolean value that indicates whether the item supports stepping backward.
- [- stepByCount:](<step(bycount_).md>) — Moves the player item’s current time forward or backward by a specified number of steps.
