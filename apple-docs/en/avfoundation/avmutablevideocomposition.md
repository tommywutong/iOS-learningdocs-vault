---
title: AVMutableVideoComposition
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+（26.0 起废弃）, iPadOS 4.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.7+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avmutablevideocomposition
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocomposition.json'
content_hash: 'sha256:edb33436df3fcb26'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMutableVideoComposition

<sub>Class</sub>

A mutable video composition subclass.

> [!warning] Deprecated
> Use [Configuration](avvideocomposition/configuration.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVMutableVideoComposition
```

## Overview

If you use the built-in video compositor, the instructions a video composition contain can specify a spatial transformation, an opacity value, and a cropping rectangle for each video source. This values can vary over time by applying linear ramping functions.

You can create a custom video compositor by implementing the [AVVideoCompositing](avvideocompositing.md) protocol. The system provides the custom video compositor with pixel buffers for each of its video sources during playback, and can perform arbitrary graphical operations on them to produce visual output.

## Relationships

- **Inherits From**: [AVVideoComposition](avvideocomposition.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a video composition

- [+ videoCompositionWithPropertiesOfAsset:completionHandler:](<avmutablevideocomposition/videocomposition(withpropertiesof_completionhandler_).md>) — Returns a new video composition that’s configured to present the video tracks of the specified asset. _(deprecated)_
- [+ videoCompositionWithPropertiesOfAsset:prototypeInstruction:completionHandler:](<avmutablevideocomposition/videocomposition(withpropertiesof_prototypeinstruction_completionhandler_).md>) — Returns a new mutable video composition with the specified asset properties and a prototype video composition instruction. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:completionHandler:](<avmutablevideocomposition/videocomposition(with_applyingcifilterswithhandler_completionhandler_).md>) — Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [+ videoCompositionWithPropertiesOfAsset:](<avmutablevideocomposition/init(propertiesof_).md>) — Creates a mutable video composition with the specified asset properties. _(deprecated)_
- [+ videoCompositionWithPropertiesOfAsset:prototypeInstruction:](<avmutablevideocomposition/init(propertiesof_prototypeinstruction_).md>) — Creates a mutable video composition with the specified asset properties and a prototype video composition instruction. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:](<avmutablevideocomposition/init(asset_applyingcifilterswithhandler_).md>) — Creates a mutable video composition configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_

### Configuring video composition properties

- [frameDuration](avmutablevideocomposition/frameduration.md) — A time interval for which the video composition should render composed video frames. _(deprecated)_
- [renderSize](avmutablevideocomposition/rendersize.md) — The size at which the video composition should render. _(deprecated)_
- [renderScale](avmutablevideocomposition/renderscale.md) — The scale at which the video composition should render. _(deprecated)_
- [animationTool](avmutablevideocomposition/animationtool.md) — A video composition tool to use with Core Animation in offline rendering. _(deprecated)_

### Specifying composition instructions

- [instructions](avmutablevideocomposition/instructions.md) — The video composition instructions. _(deprecated)_
- [AVVideoCompositionInstructionProtocol](avvideocompositioninstructionprotocol.md) — A protocol that defines the interface for a video composition instruction.

### Configuring HDR metadata

- [perFrameHDRDisplayMetadataPolicy](avmutablevideocomposition/perframehdrdisplaymetadatapolicy.md) — Configures the policy for display of HDR display metadata on the rendered frame.
- [PerFrameHDRDisplayMetadataPolicy](avvideocomposition/perframehdrdisplaymetadatapolicy-swift.struct.md) — A type that defines the policy for handling of per frame HDR metadata.

### Configuring color

- [colorPrimaries](avmutablevideocomposition/colorprimaries.md) — The color primaries used for video composition.
- [colorTransferFunction](avmutablevideocomposition/colortransferfunction.md) — The transfer function used for video composition.
- [colorYCbCrMatrix](avmutablevideocomposition/colorycbcrmatrix.md) — The YCbCr matrix used for video composition.

### Identifying source tracks

- [sourceTrackIDForFrameTiming](avmutablevideocomposition/sourcetrackidforframetiming.md) — An identifier of the source track from which the video composition derives frame timing. _(deprecated)_
- [sourceSampleDataTrackIDs](avmutablevideocomposition/sourcesampledatatrackids-7i02t.md) — The identifiers of source sample data tracks in the composition that the object requires to compose frames.

### Specifying a custom compositor

- [customVideoCompositorClass](avmutablevideocomposition/customvideocompositorclass.md) — The custom compositor class to use. _(deprecated)_

### Initializers

- [init(propertiesOfAsset:prototypeInstruction:)](<avmutablevideocomposition/init(propertiesofasset_prototypeinstruction_).md>) _(deprecated)_

## See Also

### Built-in video compositing

- [Editing and playing HDR video](editing-and-playing-hdr-video.md) — Support high-dynamic-range (HDR) video content in your app by using the HDR editing and playback capabilities of AVFoundation.
- [Debugging AVFoundation audio mixes, compositions, and video compositions](debugging-avfoundation-audio-mixes-compositions-and-video-compositions.md) — Resolve common problems when creating compositions, video compositions, and audio mixes.
- [AVVideoComposition](avvideocomposition.md) — An object that describes how to compose video frames at particular points in time.
- [AVVideoCompositionInstruction](avvideocompositioninstruction-swift.class.md) — An operation that a compositor performs.
- [AVVideoCompositionLayerInstruction](avvideocompositionlayerinstruction.md) — An object used to modify the transform, cropping, and opacity ramps applied to a given track in a composition.
- [AVMutableVideoCompositionInstruction](avmutablevideocompositioninstruction.md) — A mutable video composition instruction subclass. _(deprecated)_
- [AVMutableVideoCompositionLayerInstruction](avmutablevideocompositionlayerinstruction.md) — An object used to modify the transform, cropping, and opacity ramps applied to a given track in a mutable composition. _(deprecated)_
