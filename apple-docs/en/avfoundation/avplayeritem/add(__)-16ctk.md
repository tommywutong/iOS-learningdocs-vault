---
title: 'add(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/add(_:)-16ctk'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/add(_:)-16ctk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/add%28_%3A%29-16ctk.json'
content_hash: 'sha256:77cef73be1b209f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# add(_:)

<sub>Instance Method</sub>

Adds the specified player item output object to the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func add(_ output: AVPlayerItemOutput)
```

## Parameters

- `output` — The player item output object to associate with the item.

## Discussion

When you add an [AVPlayerItemOutput](../avplayeritemoutput.md) object to an item, the samples associated with that output object are processed according to the rules for mixing, composing, or excluding content that the [AVPlayer](../avplayer.md) object honors for the specific media type. For example, video media is composed according to the instructions provided by the player item’s video composition object and audio media is mixed according to the parameters of its audio mix object.

## See Also

### Related Documentation

- [audioMix](audiomix.md) — The audio mix parameters to be applied during playback.
- [videoComposition](videocomposition.md) — The video composition settings to be applied during playback.

### Managing player item outputs

- [outputs](outputs.md) — An array of outputs associated with the player item.
- [- removeOutput:](<remove(__)-46b1r.md>) — Removes the specified player item output object from the receiver.
