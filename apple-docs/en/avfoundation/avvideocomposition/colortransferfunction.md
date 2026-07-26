---
title: colorTransferFunction
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocomposition/colortransferfunction
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/colortransferfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/colortransferfunction.json'
content_hash: 'sha256:53d9e8f14131aba1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoComposition](../avvideocomposition.md)

# colorTransferFunction

<sub>Instance Property</sub>

The transfer function used for video composition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var colorTransferFunction: String? { get }
```

## Discussion

The default value is `nil`. When the value of this property is `nil`, the source’s transfer function is propagated and used. Valid values are those suitable for [AVVideoTransferFunctionKey](../avvideotransferfunctionkey.md).

## See Also

### Inspecting the video composition

- [renderSize](rendersize.md) — The size at which the video composition should render.
- [renderScale](renderscale.md) — The scale at which the video composition should render.
- [frameDuration](frameduration.md) — A time interval for which the video composition should render composed video frames.
- [animationTool](animationtool.md) — A video composition tool to use with Core Animation in offline rendering.
- [colorPrimaries](colorprimaries.md) — The color primaries used for video composition.
- [colorYCbCrMatrix](colorycbcrmatrix.md) — The YCbCr matrix used for video composition.
- [customVideoCompositorClass](customvideocompositorclass.md) — A custom compositor class to use.
- [outputBufferDescription](outputbufferdescription-3ayt8.md) — The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of an array of CMTag objects that describes the output buffers.
- [spatialVideoConfigurations](spatialvideoconfigurations-80iab.md) — Indicates the spatial configurations that are available to associate with the output of the video composition.
- [AVSpatialVideoConfiguration](../avspatialvideoconfiguration-swift.struct.md)
