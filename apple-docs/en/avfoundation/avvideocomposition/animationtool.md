---
title: animationTool
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocomposition/animationtool
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/animationtool'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/animationtool.json'
content_hash: 'sha256:b307810354e2263e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoComposition](../avvideocomposition.md)

# animationTool

<sub>Instance Property</sub>

A video composition tool to use with Core Animation in offline rendering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var animationTool: AVVideoCompositionCoreAnimationTool? { get }
```

## Discussion

This attribute may be `nil`. Set an animation tool if you’re using the composition in conjunction with [AVAssetExportSession](../avassetexportsession.md) for offline rendering, rather than with [AVPlayer](../avplayer.md).

## See Also

### Inspecting the video composition

- [renderSize](rendersize.md) — The size at which the video composition should render.
- [renderScale](renderscale.md) — The scale at which the video composition should render.
- [frameDuration](frameduration.md) — A time interval for which the video composition should render composed video frames.
- [colorPrimaries](colorprimaries.md) — The color primaries used for video composition.
- [colorTransferFunction](colortransferfunction.md) — The transfer function used for video composition.
- [colorYCbCrMatrix](colorycbcrmatrix.md) — The YCbCr matrix used for video composition.
- [customVideoCompositorClass](customvideocompositorclass.md) — A custom compositor class to use.
- [outputBufferDescription](outputbufferdescription-3ayt8.md) — The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of an array of CMTag objects that describes the output buffers.
- [spatialVideoConfigurations](spatialvideoconfigurations-80iab.md) — Indicates the spatial configurations that are available to associate with the output of the video composition.
- [AVSpatialVideoConfiguration](../avspatialvideoconfiguration-swift.struct.md)
