---
title: 'add(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.3+, tvOS 9.2+, visionOS 1.0+, watchOS 2.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/add(_:)-9l3to'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/add(_:)-9l3to'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/add%28_%3A%29-9l3to.json'
content_hash: 'sha256:b678c4ad4c0919f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# add(_:)

<sub>Instance Method</sub>

Adds the specified media data collector to the player item’s collection of media collectors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func add(_ collector: AVPlayerItemMediaDataCollector)
```

## Parameters

- `collector` — An instance of [AVPlayerItemMediaDataCollector](../avplayeritemmediadatacollector.md).

## Discussion

This method may incur additional I/O to collect the requested media data asynchronously.

## See Also

### Managing player item data collectors

- [mediaDataCollectors](mediadatacollectors.md) — The collection of associated media data collectors.
- [- removeMediaDataCollector:](<remove(__)-29iuz.md>) — Removes the specified media data collector from the player item’s collection of media collectors.
