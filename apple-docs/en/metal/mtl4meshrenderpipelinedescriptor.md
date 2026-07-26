---
title: MTL4MeshRenderPipelineDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4meshrenderpipelinedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4meshrenderpipelinedescriptor.json'
content_hash: 'sha256:5de39ef237474528'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4MeshRenderPipelineDescriptor

<sub>Class</sub>

Groups together properties you use to create a mesh render pipeline state object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTL4MeshRenderPipelineDescriptor
```

## Overview

Compared to [MTLMeshRenderPipelineDescriptor](mtlmeshrenderpipelinedescriptor.md), this interface doesn’t offer a mechanism to hint to Metal mutability of object, mesh, or fragment buffers. Additionally, when you use this descriptor, you don’t specify binary archives.

## Relationships

- **Inherits From**: [MTL4PipelineDescriptor](mtl4pipelinedescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [alphaToCoverageState](mtl4meshrenderpipelinedescriptor/alphatocoveragestate.md) — Indicates whether to read and use the alpha channel fragment output of color attachments to compute a sample coverage mask.
- [alphaToOneState](mtl4meshrenderpipelinedescriptor/alphatoonestate.md) — Indicates whether the pipeline forces alpha channel values of color attachments to the largest representable value.
- [colorAttachmentMappingState](mtl4meshrenderpipelinedescriptor/colorattachmentmappingstate.md) — Sets the logical-to-physical rendering remap state.
- [colorAttachments](mtl4meshrenderpipelinedescriptor/colorattachments.md) — Accesses an array containing descriptions of the color attachments this pipeline writes to.
- [fragmentFunctionDescriptor](mtl4meshrenderpipelinedescriptor/fragmentfunctiondescriptor.md) — Assigns a function descriptor representing the function this pipeline executes for each fragment.
- [fragmentStaticLinkingDescriptor](mtl4meshrenderpipelinedescriptor/fragmentstaticlinkingdescriptor.md) — Provides static linking information for the fragment stage of the render pipeline.
- [rasterizationEnabled](mtl4meshrenderpipelinedescriptor/israsterizationenabled.md) — Determines whether the pipeline rasterizes primitives.
- [maxTotalThreadgroupsPerMeshGrid](mtl4meshrenderpipelinedescriptor/maxtotalthreadgroupspermeshgrid.md) — Controls the largest number of threads the pipeline state can execute when the object stage of a mesh render pipeline you create from this descriptor dispatches its mesh stage.
- [maxTotalThreadsPerMeshThreadgroup](mtl4meshrenderpipelinedescriptor/maxtotalthreadspermeshthreadgroup.md) — Controls the largest number of threads the pipeline state can execute in a single mesh shader threadgroup dispatch.
- [maxTotalThreadsPerObjectThreadgroup](mtl4meshrenderpipelinedescriptor/maxtotalthreadsperobjectthreadgroup.md) — Controls the largest number of threads the pipeline state can execute in a single object shader threadgroup dispatch.
- [maxVertexAmplificationCount](mtl4meshrenderpipelinedescriptor/maxvertexamplificationcount.md) — Determines the maximum value that can you can pass as the pipeline’s amplification count.
- [meshFunctionDescriptor](mtl4meshrenderpipelinedescriptor/meshfunctiondescriptor.md) — Assigns a function descriptor representing the function this pipeline executes for each primitive in the mesh shader stage.
- [meshStaticLinkingDescriptor](mtl4meshrenderpipelinedescriptor/meshstaticlinkingdescriptor.md) — Provides static linking information for the mesh stage of the render pipeline.
- [meshThreadgroupSizeIsMultipleOfThreadExecutionWidth](mtl4meshrenderpipelinedescriptor/meshthreadgroupsizeismultipleofthreadexecutionwidth.md) — Provides a guarantee to Metal regarding the number of threadgroup threads for the mesh stage of a pipeline you create from this descriptor.
- [objectFunctionDescriptor](mtl4meshrenderpipelinedescriptor/objectfunctiondescriptor.md) — Assigns a function descriptor representing the function this pipeline executes for each _object_ in the object shader stage.
- [objectStaticLinkingDescriptor](mtl4meshrenderpipelinedescriptor/objectstaticlinkingdescriptor.md) — Provides static linking information for the object stage of the render pipeline.
- [objectThreadgroupSizeIsMultipleOfThreadExecutionWidth](mtl4meshrenderpipelinedescriptor/objectthreadgroupsizeismultipleofthreadexecutionwidth.md) — Provides a guarantee to Metal regarding the number of threadgroup threads for the object stage of a pipeline you create from this descriptor.
- [payloadMemoryLength](mtl4meshrenderpipelinedescriptor/payloadmemorylength.md) — Reserves storage for the object-to-mesh stage payload.
- [rasterSampleCount](mtl4meshrenderpipelinedescriptor/rastersamplecount.md) — Sets number of samples this pipeline applies for each fragment.
- [requiredThreadsPerMeshThreadgroup](mtl4meshrenderpipelinedescriptor/requiredthreadspermeshthreadgroup.md) — Controls the required number of mesh threads-per-threadgroup when drawing with a mesh shader pipeline you create from this descriptor.
- [requiredThreadsPerObjectThreadgroup](mtl4meshrenderpipelinedescriptor/requiredthreadsperobjectthreadgroup.md) — Controls the required number of object threads-per-threadgroup when drawing with a mesh shader pipeline you create from this descriptor.
- [supportFragmentBinaryLinking](mtl4meshrenderpipelinedescriptor/supportfragmentbinarylinking.md) — Indicates whether you can use the render pipeline to create new pipelines by adding binary functions to the fragment shader function’s callable functions list.
- [supportIndirectCommandBuffers](mtl4meshrenderpipelinedescriptor/supportindirectcommandbuffers.md) — Indicates whether the pipeline supports indirect command buffers.
- [supportMeshBinaryLinking](mtl4meshrenderpipelinedescriptor/supportmeshbinarylinking.md) — Indicates whether you can use the render pipeline to create new pipelines by adding binary functions to the mesh shader function’s callable functions list.
- [supportObjectBinaryLinking](mtl4meshrenderpipelinedescriptor/supportobjectbinarylinking.md) — Indicates whether you can use the render pipeline to create new pipelines by adding binary functions to the object shader function’s callable functions list.

### Instance Methods

- [- reset](<mtl4meshrenderpipelinedescriptor/reset().md>) — Resets this descriptor to its default state.

## See Also

### Render pipeline states

- [MTLRenderPipelineState](mtlrenderpipelinestate.md) — An interface that represents a graphics pipeline configuration for a render pass, which the pass applies to the draw commands you encode.
- [MTL4RenderPipelineDescriptor](mtl4renderpipelinedescriptor.md) — Groups together properties to create a render pipeline state object.
- [MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md) — An argument of options you pass to a GPU device to get a render pipeline state.
- [MTLRenderPipelineFunctionsDescriptor](mtlrenderpipelinefunctionsdescriptor.md) — A collection of functions for updating a render pipeline.
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
