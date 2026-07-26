---
title: 'init(animationTool:colorPrimaries:colorTransferFunction:colorYCbCrMatrix:customVideoCompositorClass:frameDuration:instructions:outputBufferDescription:perFrameHDRDisplayMetadataPolicy:renderScale:renderSize:sourceSampleDataTrackIDs:sourceTrackIDForFrameTiming:spatialVideoConfigurations:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocomposition/configuration/init(animationtool:colorprimaries:colortransferfunction:colorycbcrmatrix:customvideocompositorclass:frameduration:instructions:outputbufferdescription:perframehdrdisplaymetadatapolicy:renderscale:rendersize:sourcesampledatatrackids:sourcetr-2lwnx'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/configuration/init(animationtool:colorprimaries:colortransferfunction:colorycbcrmatrix:customvideocompositorclass:frameduration:instructions:outputbufferdescription:perframehdrdisplaymetadatapolicy:renderscale:rendersize:sourcesampledatatrackids:sourcetr-2lwnx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/configuration/init%28animationtool%3Acolorprimaries%3Acolortransferfunction%3Acolorycbcrmatrix%3Acustomvideocompositorclass%3Aframeduration%3Ainstructions%3Aoutputbufferdescription%3Aperframehdrdisplaymetadatapolicy%3Arenderscale%3Arendersize%3Asourcesampledatatrackids%3Asourcetr-2lwnx.json'
content_hash: 'sha256:1c3d25a58d93ba2b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVVideoComposition](../../avvideocomposition.md) · [Configuration](../configuration.md)

# init(animationTool:colorPrimaries:colorTransferFunction:colorYCbCrMatrix:customVideoCompositorClass:frameDuration:instructions:outputBufferDescription:perFrameHDRDisplayMetadataPolicy:renderScale:renderSize:sourceSampleDataTrackIDs:sourceTrackIDForFrameTiming:spatialVideoConfigurations:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
init(animationTool: AVVideoCompositionCoreAnimationTool? = nil, colorPrimaries: String? = nil, colorTransferFunction: String? = nil, colorYCbCrMatrix: String? = nil, customVideoCompositorClass: (any AVVideoCompositing.Type)? = nil, frameDuration: CMTime = CMTime.zero, instructions: [any AVVideoCompositionInstructionProtocol] = [any AVVideoCompositionInstructionProtocol](), outputBufferDescription: [[CMTag]]? = nil, perFrameHDRDisplayMetadataPolicy: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy = .propagate, renderScale: Float = 1.0, renderSize: CGSize = .zero, sourceSampleDataTrackIDs: [CMPersistentTrackID] = [CMPersistentTrackID](), sourceTrackIDForFrameTiming: Int32 = CMPersistentTrackID.zero, spatialVideoConfigurations: [AVSpatialVideoConfiguration] = [])
```

## See Also

### Creating a configuration

- [init(for:prototypeInstruction:)](<init(for_prototypeinstruction_).md>) — Initializes a video composition configuration with the specified asset properties and optional prototype video composition instruction.
- [init(animationTool:colorPrimaries:colorTransferFunction:colorYCbCrMatrix:customVideoCompositorClass:frameDuration:instructions:outputBufferDescription:renderScale:renderSize:sourceSampleDataTrackIDs:sourceTrackIDForFrameTiming:spatialVideoConfigurations:)](<init(animationtool_colorprimaries_colortransferfunction_colorycbcrmatrix_customvideocompositorclass_frameduration_instructions_outputbufferdescription_rendersca-e67dc1c76a.md>)
