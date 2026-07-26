---
title: canStepBackward
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/canstepbackward
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/canstepbackward'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/canstepbackward.json'
content_hash: 'sha256:1e2a9ff9bc293cae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# canStepBackward

<sub>Instance Property</sub>

A Boolean value that indicates whether the item supports stepping backward.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var canStepBackward: Bool { get }
```

## Discussion

Once the item becomes ready to play, the value of this property does not change. This behavior applies even when boundary conditions, such as when the item’s current time is [zero](../../coremedia/cmtime/zero.md), have been reached.

## See Also

### Stepping through media

- [canStepForward](canstepforward.md) — A Boolean value that indicates whether the item supports stepping forward.
- [- stepByCount:](<step(bycount_).md>) — Moves the player item’s current time forward or backward by a specified number of steps.
