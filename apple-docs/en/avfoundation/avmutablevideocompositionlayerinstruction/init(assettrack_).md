---
title: 'init(assetTrack:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+（26.0 起废弃）, iPadOS 4.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.7+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avmutablevideocompositionlayerinstruction/init(assettrack:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/init(assettrack:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocompositionlayerinstruction/init%28assettrack%3A%29.json'
content_hash: 'sha256:d571bd9f8d5a8bcb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoCompositionLayerInstruction](../avmutablevideocompositionlayerinstruction.md)

# init(assetTrack:)

<sub>Initializer</sub>

Creates a new mutable video composition layer instruction for the given track.

> [!warning] Deprecated
> Use AVVideoCompositionLayerInstruction.Configuration instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(assetTrack track: AVAssetTrack)
```

## Parameters

- `track` — The asset track to which to apply the instruction.

## Return Value

A new mutable video composition layer instruction with no transform or opacity ramps and [trackID](trackid.md) initialized to the track ID of `track`.
