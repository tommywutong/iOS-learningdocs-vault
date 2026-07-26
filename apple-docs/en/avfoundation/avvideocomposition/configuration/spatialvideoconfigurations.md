---
title: spatialVideoConfigurations
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocomposition/configuration/spatialvideoconfigurations
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/configuration/spatialvideoconfigurations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/configuration/spatialvideoconfigurations.json'
content_hash: 'sha256:19e1bac4b2997473'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVVideoComposition](../../avvideocomposition.md) · [Configuration](../configuration.md)

# spatialVideoConfigurations

<sub>Instance Property</sub>

Indicates the spatial configurations that are available to associate with the output of the video composition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var spatialVideoConfigurations: [AVSpatialVideoConfiguration] { get set }
```

## Discussion

A custom compositor can output spatial video by specifying one of these spatial configurations. A spatial configuration with all nil values indicates the video is not spatial. A nil spatial configuration also indicates the video is not spatial. The value can be nil, which indicates the output will not be spatial. NOTE: If this property is not empty, then the client must attach one of the spatial configurations in this array to all of the pixel buffers, otherwise an exception will be thrown.

## See Also

### Inspecting the configuration

- [renderSize](rendersize.md) — The size at which the video composition should render.
- [renderScale](renderscale.md) — The scale at which the video composition should render.
- [frameDuration](frameduration.md) — A time interval for which the video composition should render composed video frames.
- [animationTool](animationtool.md) — A video composition tool to use with Core Animation in offline rendering.
- [colorPrimaries](colorprimaries.md) — The color primaries used for video composition.
- [colorTransferFunction](colortransferfunction.md) — The transfer function used for video composition.
- [colorYCbCrMatrix](colorycbcrmatrix.md) — The YCbCr matrix used for video composition.
- [customVideoCompositorClass](customvideocompositorclass.md) — A custom compositor class to use.
- [outputBufferDescription](outputbufferdescription.md) — The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of an array of CMTag objects that describes the output buffers.
- [instructions](instructions.md) — The video composition instructions.
- [perFrameHDRDisplayMetadataPolicy](perframehdrdisplaymetadatapolicy.md) — The policy for display of HDR display metadata on the rendered frame.
- [sourceSampleDataTrackIDs](sourcesampledatatrackids.md) — The identifiers of source sample data tracks in the composition that the object requires to compose frames.
- [sourceTrackIDForFrameTiming](sourcetrackidforframetiming.md) — An identifier of the source track from which the video composition derives frame timing.
