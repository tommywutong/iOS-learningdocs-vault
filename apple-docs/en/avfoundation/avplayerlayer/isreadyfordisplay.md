---
title: isReadyForDisplay
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerlayer/isreadyfordisplay
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlayer/isreadyfordisplay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlayer/isreadyfordisplay.json'
content_hash: 'sha256:120fbc6b999d6489'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerLayer](../avplayerlayer.md)

# isReadyForDisplay

<sub>Instance Property</sub>

A Boolean value that indicates whether the first video frame of the player’s current item is ready for display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isReadyForDisplay: Bool { get }
```

## Discussion

Use this property to determine when to show or animate a player layer into view. You can display a player layer while this property value is [false](../../swift/false.md), but the layer doesn’t present any content until the value becomes [true](../../swift/true.md).

This property remains [false](../../swift/false.md) for a player when its [currentItem](../avplayer/currentitem.md) contains no enabled video tracks.

This property is key-value observable.
