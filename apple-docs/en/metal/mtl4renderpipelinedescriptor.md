---
title: MTL4RenderPipelineDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4renderpipelinedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpipelinedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpipelinedescriptor.json'
content_hash: 'sha256:34f539e2211081f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4RenderPipelineDescriptor

<sub>Class</sub>

Groups together properties to create a render pipeline state object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTL4RenderPipelineDescriptor
```

## Overview

Compared to [MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md), this interface doesn’t offer a mechanism to hint to Metal mutability of vertex and fragment buffers. Additionally, using this descriptor, you don’t specify binary archives.

## Relationships

- **Inherits From**: [MTL4PipelineDescriptor](mtl4pipelinedescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [alphaToCoverageState](mtl4renderpipelinedescriptor/alphatocoveragestate.md) — Indicates whether to read and use the alpha channel fragment output of color attachments to compute a sample coverage mask.
- [alphaToOneState](mtl4renderpipelinedescriptor/alphatoonestate.md) — Indicates whether the pipeline forces alpha channel values of color attachments to the largest representable value.
- [colorAttachmentMappingState](mtl4renderpipelinedescriptor/colorattachmentmappingstate.md) — Configures a logical-to-physical rendering remap state.
- [colorAttachments](mtl4renderpipelinedescriptor/colorattachments.md) — Accesses an array containing descriptions of the color attachments this pipeline writes to.
- [fragmentFunctionDescriptor](mtl4renderpipelinedescriptor/fragmentfunctiondescriptor.md) — Assigns the shader function that this pipeline executes for each fragment.
- [fragmentStaticLinkingDescriptor](mtl4renderpipelinedescriptor/fragmentstaticlinkingdescriptor.md) — Provides static linking information for the fragment stage of the render pipeline.
- [inputPrimitiveTopology](mtl4renderpipelinedescriptor/inputprimitivetopology.md) — Assigns type of primitive topology this pipeline renders.
- [rasterizationEnabled](mtl4renderpipelinedescriptor/israsterizationenabled.md) — Determines whether the pipeline rasterizes primitives.
- [maxVertexAmplificationCount](mtl4renderpipelinedescriptor/maxvertexamplificationcount.md) — Determines the maximum value that can you can pass as the pipeline’s amplification count.
- [rasterSampleCount](mtl4renderpipelinedescriptor/rastersamplecount.md) — Controls the number of samples this pipeline applies for each fragment.
- [supportFragmentBinaryLinking](mtl4renderpipelinedescriptor/supportfragmentbinarylinking.md) — Indicates whether you can use the pipeline to create new pipelines by adding binary functions to the fragment shader function’s callable functions list.
- [supportIndirectCommandBuffers](mtl4renderpipelinedescriptor/supportindirectcommandbuffers.md) — Indicates whether the pipeline supports indirect command buffers.
- [supportVertexBinaryLinking](mtl4renderpipelinedescriptor/supportvertexbinarylinking.md) — Indicates whether you can use the render pipeline to create new pipelines by adding binary functions to the vertex shader function’s callable functions list.
- [vertexDescriptor](mtl4renderpipelinedescriptor/vertexdescriptor.md) — Configures an optional vertex descriptor for the vertex input.
- [vertexFunctionDescriptor](mtl4renderpipelinedescriptor/vertexfunctiondescriptor.md) — Assigns the shader function that this pipeline executes for each vertex.
- [vertexStaticLinkingDescriptor](mtl4renderpipelinedescriptor/vertexstaticlinkingdescriptor.md) — Provides static linking information for the vertex stage of the render pipeline.

### Instance Methods

- [- reset](<mtl4renderpipelinedescriptor/reset().md>) — Resets this descriptor to its default state.

## See Also

### Render pipeline states

- [MTLRenderPipelineState](mtlrenderpipelinestate.md) — An interface that represents a graphics pipeline configuration for a render pass, which the pass applies to the draw commands you encode.
- [MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md) — An argument of options you pass to a GPU device to get a render pipeline state.
- [MTLRenderPipelineFunctionsDescriptor](mtlrenderpipelinefunctionsdescriptor.md) — A collection of functions for updating a render pipeline.
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
