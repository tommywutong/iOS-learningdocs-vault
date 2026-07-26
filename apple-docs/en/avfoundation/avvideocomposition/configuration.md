---
title: AVVideoComposition.Configuration
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocomposition/configuration
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/configuration.json'
content_hash: 'sha256:0c9f4216894e4378'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoComposition](../avvideocomposition.md)

# AVVideoComposition.Configuration

<sub>Structure</sub>

Configurable properties for initializing a new AVVideoComposition instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct Configuration
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a configuration

- [init(for:prototypeInstruction:)](<configuration/init(for_prototypeinstruction_).md>) — Initializes a video composition configuration with the specified asset properties and optional prototype video composition instruction.
- [init(animationTool:colorPrimaries:colorTransferFunction:colorYCbCrMatrix:customVideoCompositorClass:frameDuration:instructions:outputBufferDescription:perFrameHDRDisplayMetadataPolicy:renderScale:renderSize:sourceSampleDataTrackIDs:sourceTrackIDForFrameTiming:spatialVideoConfigurations:)](<configuration/init(animationtool_colorprimaries_colortransferfunction_colorycbcrmatrix_customvideocompositorclass_frameduration_instructions_outputbufferdescription_perframeh-d13e75cb88.md>)
- [init(animationTool:colorPrimaries:colorTransferFunction:colorYCbCrMatrix:customVideoCompositorClass:frameDuration:instructions:outputBufferDescription:renderScale:renderSize:sourceSampleDataTrackIDs:sourceTrackIDForFrameTiming:spatialVideoConfigurations:)](<configuration/init(animationtool_colorprimaries_colortransferfunction_colorycbcrmatrix_customvideocompositorclass_frameduration_instructions_outputbufferdescription_rendersca-e67dc1c76a.md>)

### Inspecting the configuration

- [renderSize](configuration/rendersize.md) — The size at which the video composition should render.
- [renderScale](configuration/renderscale.md) — The scale at which the video composition should render.
- [frameDuration](configuration/frameduration.md) — A time interval for which the video composition should render composed video frames.
- [animationTool](configuration/animationtool.md) — A video composition tool to use with Core Animation in offline rendering.
- [colorPrimaries](configuration/colorprimaries.md) — The color primaries used for video composition.
- [colorTransferFunction](configuration/colortransferfunction.md) — The transfer function used for video composition.
- [colorYCbCrMatrix](configuration/colorycbcrmatrix.md) — The YCbCr matrix used for video composition.
- [customVideoCompositorClass](configuration/customvideocompositorclass.md) — A custom compositor class to use.
- [outputBufferDescription](configuration/outputbufferdescription.md) — The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of an array of CMTag objects that describes the output buffers.
- [instructions](configuration/instructions.md) — The video composition instructions.
- [spatialVideoConfigurations](configuration/spatialvideoconfigurations.md) — Indicates the spatial configurations that are available to associate with the output of the video composition.
- [perFrameHDRDisplayMetadataPolicy](configuration/perframehdrdisplaymetadatapolicy.md) — The policy for display of HDR display metadata on the rendered frame.
- [sourceSampleDataTrackIDs](configuration/sourcesampledatatrackids.md) — The identifiers of source sample data tracks in the composition that the object requires to compose frames.
- [sourceTrackIDForFrameTiming](configuration/sourcetrackidforframetiming.md) — An identifier of the source track from which the video composition derives frame timing.

## See Also

### Creating a video composition

- [init(configuration:)](<init(configuration_).md>) — Initialize an AVVideoComposition with a configuration.
- [init(applyingFiltersTo:applier:)](<init(applyingfiltersto_applier_).md>) — Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:completionHandler:](<videocomposition(with_applyingcifilterswithhandler_completionhandler_).md>) — Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
- [AVAsynchronousCIImageFilteringRequest](../avasynchronousciimagefilteringrequest.md) — An object that supports using Core Image filters to process an individual video frame in a video composition. _(deprecated)_
- [AVCIImageFilteringParameters](../avciimagefilteringparameters.md)
- [AVCIImageFilteringResult](../avciimagefilteringresult.md) — An output video frame processed with Core Image filtering.
- [+ videoCompositionWithPropertiesOfAsset:completionHandler:](<videocomposition(withpropertiesof_completionhandler_).md>) — Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [+ videoCompositionWithPropertiesOfAsset:](<init(propertiesof_).md>) — Creates a video composition object configured to present the video tracks of the specified asset. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:](<init(asset_applyingcifilterswithhandler_).md>) — Creates a video composition configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
