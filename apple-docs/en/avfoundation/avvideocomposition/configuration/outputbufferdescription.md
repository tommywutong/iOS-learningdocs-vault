---
title: outputBufferDescription
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocomposition/configuration/outputbufferdescription
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/configuration/outputbufferdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/configuration/outputbufferdescription.json'
content_hash: 'sha256:d1fd7bb7b342311d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVVideoComposition](../../avvideocomposition.md) · [Configuration](../configuration.md)

# outputBufferDescription

<sub>Instance Property</sub>

The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of an array of CMTag objects that describes the output buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var outputBufferDescription: [[CMTag]]? { get set }
```

## Discussion

If the video composition will output tagged buffers, the details of those buffers should be specified with CMTags. Specifically, the StereoView (eyes) and ProjectionKind must be specified. The behavior is undefined if the output buffers do not match the outputBufferDescription. The default is nil, which means monoscopic output. Note that an empty array is not valid. Note that tagged buffers are only supported for custom compositors.

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
- [instructions](instructions.md) — The video composition instructions.
- [spatialVideoConfigurations](spatialvideoconfigurations.md) — Indicates the spatial configurations that are available to associate with the output of the video composition.
- [perFrameHDRDisplayMetadataPolicy](perframehdrdisplaymetadatapolicy.md) — The policy for display of HDR display metadata on the rendered frame.
- [sourceSampleDataTrackIDs](sourcesampledatatrackids.md) — The identifiers of source sample data tracks in the composition that the object requires to compose frames.
- [sourceTrackIDForFrameTiming](sourcetrackidforframetiming.md) — An identifier of the source track from which the video composition derives frame timing.
