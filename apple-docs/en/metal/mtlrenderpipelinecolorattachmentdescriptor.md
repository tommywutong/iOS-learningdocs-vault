---
title: MTLRenderPipelineColorAttachmentDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinecolorattachmentdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor.json'
content_hash: 'sha256:682b80fe5ae9ca2a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLRenderPipelineColorAttachmentDescriptor

<sub>Class</sub>

A color render target that specifies the color configuration and color operations for a render pipeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLRenderPipelineColorAttachmentDescriptor
```

## Overview

An [MTLRenderPipelineColorAttachmentDescriptor](mtlrenderpipelinecolorattachmentdescriptor.md) instance defines the configuration of a color attachment associated with a rendering pipeline.

The [pixelFormat](mtlrenderpipelinecolorattachmentdescriptor/pixelformat.md) property needs to be specified for the rendering pipeline state at the color attachment.

Blend operations determine how a source fragment is combined with a destination value in a color attachment to determine the pixel value to be written. The following properties define whether and how blending is performed:

- The [blendingEnabled](mtlrenderpipelinecolorattachmentdescriptor/isblendingenabled.md) property enables blending. The default value is [false](../swift/false.md).
- The [writeMask](mtlrenderpipelinecolorattachmentdescriptor/writemask.md) property identifies which color channels are blended. The default value is [MTLColorWriteMaskAll](mtlcolorwritemask/all.md), which allows all color channels to be blended.
- The [rgbBlendOperation](mtlrenderpipelinecolorattachmentdescriptor/rgbblendoperation.md) and [alphaBlendOperation](mtlrenderpipelinecolorattachmentdescriptor/alphablendoperation.md) properties assign the blend operations for RGB and alpha pixel data. The default value for both properties is [MTLBlendOperationAdd](mtlblendoperation/add.md).
- The [sourceRGBBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/sourcergbblendfactor.md), [sourceAlphaBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/sourcealphablendfactor.md), [destinationRGBBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/destinationrgbblendfactor.md), and [destinationAlphaBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/destinationalphablendfactor.md) properties assign the source and destination blend factors. The default value for [sourceRGBBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/sourcergbblendfactor.md) and [sourceAlphaBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/sourcealphablendfactor.md) is [MTLBlendFactorOne](mtlblendfactor/one.md). The default value for [destinationRGBBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/destinationrgbblendfactor.md) and [destinationAlphaBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/destinationalphablendfactor.md) is [MTLBlendFactorZero](mtlblendfactor/zero.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring render pipeline states

- [pixelFormat](mtlrenderpipelinecolorattachmentdescriptor/pixelformat.md) — The pixel format of the color attachment’s texture.
- [writeMask](mtlrenderpipelinecolorattachmentdescriptor/writemask.md) — A bitmask that restricts which color channels are written into the texture.
- [MTLColorWriteMask](mtlcolorwritemask.md) — Values used to specify a mask to permit or restrict writing to color channels of a color value.

### Controlling blend operations

- [blendingEnabled](mtlrenderpipelinecolorattachmentdescriptor/isblendingenabled.md) — A Boolean value that determines whether blending is enabled.
- [alphaBlendOperation](mtlrenderpipelinecolorattachmentdescriptor/alphablendoperation.md) — The blend operation assigned for the alpha data.
- [rgbBlendOperation](mtlrenderpipelinecolorattachmentdescriptor/rgbblendoperation.md) — The blend operation assigned for the RGB data.
- [MTLBlendOperation](mtlblendoperation.md) — For every pixel, `MTLBlendOperation` determines how to combine and weight the source fragment values with the destination values. Some blend operations multiply the source values by a source blend factor (SBF), multiply the destination values by a destination blend factor (DBF), and then combine the results using addition or subtraction. Other blend operations use either a minimum or maximum function to determine the result.

### Configuring blend factors

- [destinationAlphaBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/destinationalphablendfactor.md) — The destination blend factor (DBF) used by the alpha blend operation.
- [destinationRGBBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/destinationrgbblendfactor.md) — The destination blend factor (DBF) used by the RGB blend operation.
- [sourceAlphaBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/sourcealphablendfactor.md) — The source blend factor (SBF) used by the alpha blend operation.
- [sourceRGBBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/sourcergbblendfactor.md) — The source blend factor (SBF) used by the RGB blend operation.
- [MTLBlendFactor](mtlblendfactor.md) — The source and destination blend factors are often needed to complete specification of a blend operation. In most cases, the blend factor for both RGB values (_F(rgb)_) and alpha values (_F(a)_) are similar to one another, but in some cases, such as `MTLBlendFactorSourceAlphaSaturated`, the blend factor is slightly different. Four blend factors (`MTLBlendFactorBlendColor`, `MTLBlendFactorOneMinusBlendColor`, `MTLBlendFactorBlendAlpha`, and `MTLBlendFactorOneMinusBlendAlpha`) refer to a constant blend color value that is set by the [- setBlendColorRed:green:blue:alpha:](<mtlrendercommandencoder/setblendcolor(red_green_blue_alpha_).md>) method of `MTLRenderCommandEncoder`.

## See Also

### Render pipeline states

- [MTLRenderPipelineState](mtlrenderpipelinestate.md) — An interface that represents a graphics pipeline configuration for a render pass, which the pass applies to the draw commands you encode.
- [MTL4RenderPipelineDescriptor](mtl4renderpipelinedescriptor.md) — Groups together properties to create a render pipeline state object.
- [MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md) — An argument of options you pass to a GPU device to get a render pipeline state.
- [MTLRenderPipelineFunctionsDescriptor](mtlrenderpipelinefunctionsdescriptor.md) — A collection of functions for updating a render pipeline.
- [MTL4MeshRenderPipelineDescriptor](mtl4meshrenderpipelinedescriptor.md) — Groups together properties you use to create a mesh render pipeline state object.
- [MTLMeshRenderPipelineDescriptor](mtlmeshrenderpipelinedescriptor.md) — An object that configures new render pipeline state objects for mesh shading.
- [MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md) — The mutability options for a buffer that a render or compute pipeline uses.
- [MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md) — An array of pipeline buffer descriptors.
- [MTL4RenderPipelineColorAttachmentDescriptor](mtl4renderpipelinecolorattachmentdescriptor.md)
- [MTLRenderPipelineColorAttachmentDescriptorArray](mtlrenderpipelinecolorattachmentdescriptorarray.md) — An array of render pipeline color attachment descriptor objects.
- [MTL4TileRenderPipelineDescriptor](mtl4tilerenderpipelinedescriptor.md) — Groups together properties you use to create a tile render pipeline state object.
- [MTLTileRenderPipelineDescriptor](mtltilerenderpipelinedescriptor.md) — An object that configures new render pipeline state objects for tile shading.
- [MTLTileRenderPipelineColorAttachmentDescriptor](mtltilerenderpipelinecolorattachmentdescriptor.md) — A description of a tile-shading render pipeline’s color render target.
- [MTLPipelineOption](mtlpipelineoption.md) — Options that determine how Metal prepares the pipeline.
- [MTL4RenderPipelineBinaryFunctionsDescriptor](mtl4renderpipelinebinaryfunctionsdescriptor.md) — Allows you to specify additional binary functions to link to each stage of a render pipeline.
