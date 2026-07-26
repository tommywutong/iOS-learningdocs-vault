---
title: 'step(byCount:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/step(bycount:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/step(bycount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/step%28bycount%3A%29.json'
content_hash: 'sha256:ac7d59de4e5ecf5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# step(byCount:)

<sub>Instance Method</sub>

Moves the player item’s current time forward or backward by a specified number of steps.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func step(byCount stepCount: Int)
```

## Parameters

- `stepCount` — The number of steps by which to move. A positive number steps forward, a negative number steps backward.

## Discussion

The size of each step depends on the receiver’s enabled `AVPlayerItemTrack` objects (see [tracks](tracks.md)).

## See Also

### Stepping through media

- [canStepForward](canstepforward.md) — A Boolean value that indicates whether the item supports stepping forward.
- [canStepBackward](canstepbackward.md) — A Boolean value that indicates whether the item supports stepping backward.
