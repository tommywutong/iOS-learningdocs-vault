---
title: 'init(for:prototypeInstruction:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocomposition/configuration/init(for:prototypeinstruction:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/configuration/init(for:prototypeinstruction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/configuration/init%28for%3Aprototypeinstruction%3A%29.json'
content_hash: 'sha256:f3664a2b8fbbc3cf'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVVideoComposition](../../avvideocomposition.md) · [Configuration](../configuration.md)

# init(for:prototypeInstruction:)

<sub>Initializer</sub>

Initializes a video composition configuration with the specified asset properties and optional prototype video composition instruction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated(nonsending) init(for asset: AVAsset, prototypeInstruction: AVVideoCompositionInstruction? = nil) async throws
```

## Parameters

- `asset` — Asset to use with the video composition

- `prototypeInstruction` — A video composition instruction to use as a prototype.

## See Also

### Creating a configuration

- [init(animationTool:colorPrimaries:colorTransferFunction:colorYCbCrMatrix:customVideoCompositorClass:frameDuration:instructions:outputBufferDescription:perFrameHDRDisplayMetadataPolicy:renderScale:renderSize:sourceSampleDataTrackIDs:sourceTrackIDForFrameTiming:spatialVideoConfigurations:)](<init(animationtool_colorprimaries_colortransferfunction_colorycbcrmatrix_customvideocompositorclass_frameduration_instructions_outputbufferdescription_perframeh-d13e75cb88.md>)
- [init(animationTool:colorPrimaries:colorTransferFunction:colorYCbCrMatrix:customVideoCompositorClass:frameDuration:instructions:outputBufferDescription:renderScale:renderSize:sourceSampleDataTrackIDs:sourceTrackIDForFrameTiming:spatialVideoConfigurations:)](<init(animationtool_colorprimaries_colortransferfunction_colorycbcrmatrix_customvideocompositorclass_frameduration_instructions_outputbufferdescription_rendersca-e67dc1c76a.md>)
