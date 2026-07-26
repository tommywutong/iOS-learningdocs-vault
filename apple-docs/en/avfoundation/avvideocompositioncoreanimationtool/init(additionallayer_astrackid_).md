---
title: 'init(additionalLayer:asTrackID:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositioncoreanimationtool/init(additionallayer:astrackid:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/init(additionallayer:astrackid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioncoreanimationtool/init%28additionallayer%3Aastrackid%3A%29.json'
content_hash: 'sha256:88ab83ed1f12c18e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionCoreAnimationTool](../avvideocompositioncoreanimationtool.md)

# init(additionalLayer:asTrackID:)

<sub>Initializer</sub>

Adds a Core Animation layer to the video composition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(additionalLayer layer: sending CALayer, asTrackID trackID: CMPersistentTrackID)
```

## Parameters

- `layer` — The Core Animation layer to add.

- `trackID` — A track ID to identify the track. `trackID` should not match any real trackID in the source.

## Return Value

A new Core Animation tool for the layer.

## Discussion

You use this method to include a Core Animation layer as an individual track input in video composition.

Video composition instructions should reference `trackID` where the rendered animation should be included.

## See Also

### Creating a composition tool

- [+ videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayer:inLayer:](<init(postprocessingasvideolayer_in_).md>) — Composes the composited video frame with a Core Animation layer. _(deprecated)_
- [+ videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayers:inLayer:](<init(postprocessingasvideolayers_in_).md>) — Composes the composited video frames with the Core Animation layer.
- [init(configuration:)](<init(configuration_).md>) — Compose the composited video frames with the Core Animation layer.
- [Configuration](configuration.md) — Configurable properties for initializing a new AVVideoCompositionCoreAnimationTool instance.
