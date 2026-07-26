---
title: MTLRenderPipelineFunctionsDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinefunctionsdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinefunctionsdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinefunctionsdescriptor.json'
content_hash: 'sha256:7b78dbdde4024f57'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLRenderPipelineFunctionsDescriptor

<sub>Class</sub>

A collection of functions for updating a render pipeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLRenderPipelineFunctionsDescriptor
```

## Overview

When you create a render pipeline that takes visible functions as parameters, you need to specify all possible functions that the render pipeline can call. If you already have a pipeline, you can create a new render pipeline with the same configuration but additional callable functions. To create the new pipeline state, configure an [MTLRenderPipelineFunctionsDescriptor](mtlrenderpipelinefunctionsdescriptor.md) instance with the additional callable functions to add, and then call the pipeline state’s [- newRenderPipelineStateWithAdditionalBinaryFunctions:error:](<mtlrenderpipelinestate/makerenderpipelinestate(additionalbinaryfunctions_)-84te1.md>) method, passing the descriptor.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the descriptor’s functions

- [vertexAdditionalBinaryFunctions](mtlrenderpipelinefunctionsdescriptor/vertexadditionalbinaryfunctions.md) — The vertex functions to add to the render pipeline.
- [fragmentAdditionalBinaryFunctions](mtlrenderpipelinefunctionsdescriptor/fragmentadditionalbinaryfunctions.md) — The fragment functions to add to the render pipeline.
- [tileAdditionalBinaryFunctions](mtlrenderpipelinefunctionsdescriptor/tileadditionalbinaryfunctions.md) — The tile functions to add to the render pipeline.

## See Also

### Render pipeline states

- [MTLRenderPipelineState](mtlrenderpipelinestate.md) — An interface that represents a graphics pipeline configuration for a render pass, which the pass applies to the draw commands you encode.
- [MTL4RenderPipelineDescriptor](mtl4renderpipelinedescriptor.md) — Groups together properties to create a render pipeline state object.
- [MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md) — An argument of options you pass to a GPU device to get a render pipeline state.
- [MTL4MeshRenderPipelineDescriptor](mtl4meshrenderpipelinedescriptor.md) — Groups together properties you use to create a mesh render pipeline state object.
- [MTLMeshRenderPipelineDescriptor](mtlmeshrenderpipelinedescriptor.md) — An object that configures new render pipeline state objects for mesh shading.
- [MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md) — The mutability options for a buffer that a render or compute pipeline uses.
- [MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md) — An array of pipeline buffer descriptors.
- [MTL4RenderPipelineColorAttachmentDescriptor](mtl4renderpipelinecolorattachmentdescriptor.md)
- [MTLRenderPipelineColorAttachmentDescriptor](mtlrenderpipelinecolorattachmentdescriptor.md) — A color render target that specifies the color configuration and color operations for a render pipeline.
- [MTLRenderPipelineColorAttachmentDescriptorArray](mtlrenderpipelinecolorattachmentdescriptorarray.md) — An array of render pipeline color attachment descriptor objects.
- [MTL4TileRenderPipelineDescriptor](mtl4tilerenderpipelinedescriptor.md) — Groups together properties you use to create a tile render pipeline state object.
- [MTLTileRenderPipelineDescriptor](mtltilerenderpipelinedescriptor.md) — An object that configures new render pipeline state objects for tile shading.
- [MTLTileRenderPipelineColorAttachmentDescriptor](mtltilerenderpipelinecolorattachmentdescriptor.md) — A description of a tile-shading render pipeline’s color render target.
- [MTLPipelineOption](mtlpipelineoption.md) — Options that determine how Metal prepares the pipeline.
- [MTL4RenderPipelineBinaryFunctionsDescriptor](mtl4renderpipelinebinaryfunctionsdescriptor.md) — Allows you to specify additional binary functions to link to each stage of a render pipeline.
