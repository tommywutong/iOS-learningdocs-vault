---
title: AVVideoComposition
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocomposition
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition.json'
content_hash: 'sha256:6e89669dbe4813e6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoComposition

<sub>Class</sub>

An object that describes how to compose video frames at particular points in time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVVideoComposition
```

## Overview

If you use the built-in video compositor, the instructions a video composition contain can specify a spatial transformation, an opacity value, and a cropping rectangle for each video source. This values can vary over time by applying linear ramping functions.

You can create a custom video compositor by implementing the [AVVideoCompositing](avvideocompositing.md) protocol. The system provides the custom video compositor with pixel buffers for each of its video sources during playback, and can perform arbitrary graphical operations on them to produce visual output.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVMutableVideoComposition](avmutablevideocomposition.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a video composition

- [init(configuration:)](<avvideocomposition/init(configuration_).md>) — Initialize an AVVideoComposition with a configuration.
- [Configuration](avvideocomposition/configuration.md) — Configurable properties for initializing a new AVVideoComposition instance.
- [init(applyingFiltersTo:applier:)](<avvideocomposition/init(applyingfiltersto_applier_).md>) — Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:completionHandler:](<avvideocomposition/videocomposition(with_applyingcifilterswithhandler_completionhandler_).md>) — Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
- [AVAsynchronousCIImageFilteringRequest](avasynchronousciimagefilteringrequest.md) — An object that supports using Core Image filters to process an individual video frame in a video composition. _(deprecated)_
- [AVCIImageFilteringParameters](avciimagefilteringparameters.md)
- [AVCIImageFilteringResult](avciimagefilteringresult.md) — An output video frame processed with Core Image filtering.
- [+ videoCompositionWithPropertiesOfAsset:completionHandler:](<avvideocomposition/videocomposition(withpropertiesof_completionhandler_).md>) — Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [+ videoCompositionWithPropertiesOfAsset:](<avvideocomposition/init(propertiesof_).md>) — Creates a video composition object configured to present the video tracks of the specified asset. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:](<avvideocomposition/init(asset_applyingcifilterswithhandler_).md>) — Creates a video composition configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_

### Inspecting the video composition

- [renderSize](avvideocomposition/rendersize.md) — The size at which the video composition should render.
- [renderScale](avvideocomposition/renderscale.md) — The scale at which the video composition should render.
- [frameDuration](avvideocomposition/frameduration.md) — A time interval for which the video composition should render composed video frames.
- [animationTool](avvideocomposition/animationtool.md) — A video composition tool to use with Core Animation in offline rendering.
- [colorPrimaries](avvideocomposition/colorprimaries.md) — The color primaries used for video composition.
- [colorTransferFunction](avvideocomposition/colortransferfunction.md) — The transfer function used for video composition.
- [colorYCbCrMatrix](avvideocomposition/colorycbcrmatrix.md) — The YCbCr matrix used for video composition.
- [customVideoCompositorClass](avvideocomposition/customvideocompositorclass.md) — A custom compositor class to use.
- [outputBufferDescription](avvideocomposition/outputbufferdescription-3ayt8.md) — The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of an array of CMTag objects that describes the output buffers.
- [spatialVideoConfigurations](avvideocomposition/spatialvideoconfigurations-80iab.md) — Indicates the spatial configurations that are available to associate with the output of the video composition.
- [AVSpatialVideoConfiguration](avspatialvideoconfiguration-swift.struct.md)

### Validating the time range

- [- isValidForTracks:assetDuration:timeRange:validationDelegate:](<avvideocomposition/isvalid(for_assetduration_timerange_validationdelegate_).md>) — Indicates whether the time ranges of the composition’s instructions conform to validation requirements.
- [AVVideoCompositionValidationHandling](avvideocompositionvalidationhandling.md) — Methods you can implement to indicate whether validation of a video composition should continue after specific errors are found.
- [- determineValidityForAsset:timeRange:validationDelegate:completionHandler:](<avvideocomposition/determinevalidity(for_timerange_validationdelegate_completionhandler_).md>) — Determines whether the time ranges of the composition’s instructions conform to validation requirements. _(deprecated)_
- [- isValidForAsset:timeRange:validationDelegate:](<avvideocomposition/isvalid(for_timerange_validationdelegate_).md>) — Indicates whether the time ranges of the composition’s instructions conform to validation requirements. _(deprecated)_

### Reading instructions

- [instructions](avvideocomposition/instructions.md) — The video composition instructions.
- [AVVideoCompositionInstructionProtocol](avvideocompositioninstructionprotocol.md) — A protocol that defines the interface for a video composition instruction.

### Identifying source tracks

- [sourceTrackIDForFrameTiming](avvideocomposition/sourcetrackidforframetiming.md) — An identifier of the source track from which the video composition derives frame timing.
- [sourceSampleDataTrackIDs](avvideocomposition/sourcesampledatatrackids-2hgue.md) — The identifiers of source sample data tracks in the composition that the object requires to compose frames.

### Configuring HDR metadata

- [perFrameHDRDisplayMetadataPolicy](avvideocomposition/perframehdrdisplaymetadatapolicy-swift.property.md) — The policy for display of HDR display metadata on the rendered frame.
- [PerFrameHDRDisplayMetadataPolicy](avvideocomposition/perframehdrdisplaymetadatapolicy-swift.struct.md) — A type that defines the policy for handling of per frame HDR metadata.

### Initializers

- [init(propertiesOfAsset:)](<avvideocomposition/init(propertiesofasset_).md>) _(deprecated)_

## See Also

### Built-in video compositing

- [Editing and playing HDR video](editing-and-playing-hdr-video.md) — Support high-dynamic-range (HDR) video content in your app by using the HDR editing and playback capabilities of AVFoundation.
- [Debugging AVFoundation audio mixes, compositions, and video compositions](debugging-avfoundation-audio-mixes-compositions-and-video-compositions.md) — Resolve common problems when creating compositions, video compositions, and audio mixes.
- [AVVideoCompositionInstruction](avvideocompositioninstruction-swift.class.md) — An operation that a compositor performs.
- [AVVideoCompositionLayerInstruction](avvideocompositionlayerinstruction.md) — An object used to modify the transform, cropping, and opacity ramps applied to a given track in a composition.
- [AVMutableVideoComposition](avmutablevideocomposition.md) — A mutable video composition subclass. _(deprecated)_
- [AVMutableVideoCompositionInstruction](avmutablevideocompositioninstruction.md) — A mutable video composition instruction subclass. _(deprecated)_
- [AVMutableVideoCompositionLayerInstruction](avmutablevideocompositionlayerinstruction.md) — An object used to modify the transform, cropping, and opacity ramps applied to a given track in a mutable composition. _(deprecated)_
