---
title: canPlayFastForward
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/canplayfastforward
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/canplayfastforward'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/canplayfastforward.json'
content_hash: 'sha256:d1e500643c1b9f6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# canPlayFastForward

<sub>Instance Property</sub>

A Boolean value that indicates whether the item can be fast forwarded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var canPlayFastForward: Bool { get }
```

## Discussion

An item can be fast forwarded if its rate can be greater than `1.0`.

## See Also

### Determining playback capabilities

- [canPlayReverse](canplayreverse.md) — A Boolean value that indicates whether the item can play in reverse.
- [canPlayFastReverse](canplayfastreverse.md) — A Boolean value that indicates whether the item can be quickly reversed.
- [canPlaySlowForward](canplayslowforward.md) — A Boolean value that indicates whether the item can play slower than normal.
- [canPlaySlowReverse](canplayslowreverse.md) — A Boolean value that indicates whether the item can play slowly backward.
