---
title: outputs
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/outputs
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/outputs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/outputs.json'
content_hash: 'sha256:e63eb83634b2d473'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# outputs

<sub>Instance Property</sub>

An array of outputs associated with the player item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var outputs: [AVPlayerItemOutput] { get }
```

## Discussion

This property contains the collection of [AVPlayerItemOutput](../avplayeritemoutput.md) objects used to transfer media data to the player object.

## See Also

### Managing player item outputs

- [- addOutput:](<add(__)-16ctk.md>) — Adds the specified player item output object to the receiver.
- [- removeOutput:](<remove(__)-46b1r.md>) — Removes the specified player item output object from the receiver.
