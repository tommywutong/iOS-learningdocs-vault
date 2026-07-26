---
title: MTLMeshRenderPipelineDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlmeshrenderpipelinedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlmeshrenderpipelinedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlmeshrenderpipelinedescriptor.json'
content_hash: 'sha256:5f6d89119681c6e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLMeshRenderPipelineDescriptor

<sub>Class</sub>

An object that configures new render pipeline state objects for mesh shading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLMeshRenderPipelineDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [binaryArchives](mtlmeshrenderpipelinedescriptor/binaryarchives.md)
- [colorAttachments](mtlmeshrenderpipelinedescriptor/colorattachments.md)
- [depthAttachmentPixelFormat](mtlmeshrenderpipelinedescriptor/depthattachmentpixelformat.md)
- [fragmentBuffers](mtlmeshrenderpipelinedescriptor/fragmentbuffers.md)
- [fragmentFunction](mtlmeshrenderpipelinedescriptor/fragmentfunction.md)
- [fragmentLinkedFunctions](mtlmeshrenderpipelinedescriptor/fragmentlinkedfunctions.md)
- [alphaToCoverageEnabled](mtlmeshrenderpipelinedescriptor/isalphatocoverageenabled.md)
- [alphaToOneEnabled](mtlmeshrenderpipelinedescriptor/isalphatooneenabled.md)
- [rasterizationEnabled](mtlmeshrenderpipelinedescriptor/israsterizationenabled.md)
- [label](mtlmeshrenderpipelinedescriptor/label.md)
- [maxTotalThreadgroupsPerMeshGrid](mtlmeshrenderpipelinedescriptor/maxtotalthreadgroupspermeshgrid.md)
- [maxTotalThreadsPerMeshThreadgroup](mtlmeshrenderpipelinedescriptor/maxtotalthreadspermeshthreadgroup.md)
- [maxTotalThreadsPerObjectThreadgroup](mtlmeshrenderpipelinedescriptor/maxtotalthreadsperobjectthreadgroup.md)
- [maxVertexAmplificationCount](mtlmeshrenderpipelinedescriptor/maxvertexamplificationcount.md)
- [meshBuffers](mtlmeshrenderpipelinedescriptor/meshbuffers.md)
- [meshFunction](mtlmeshrenderpipelinedescriptor/meshfunction.md)
- [meshLinkedFunctions](mtlmeshrenderpipelinedescriptor/meshlinkedfunctions.md)
- [meshThreadgroupSizeIsMultipleOfThreadExecutionWidth](mtlmeshrenderpipelinedescriptor/meshthreadgroupsizeismultipleofthreadexecutionwidth.md)
- [objectBuffers](mtlmeshrenderpipelinedescriptor/objectbuffers.md)
- [objectFunction](mtlmeshrenderpipelinedescriptor/objectfunction.md)
- [objectLinkedFunctions](mtlmeshrenderpipelinedescriptor/objectlinkedfunctions.md)
- [objectThreadgroupSizeIsMultipleOfThreadExecutionWidth](mtlmeshrenderpipelinedescriptor/objectthreadgroupsizeismultipleofthreadexecutionwidth.md)
- [payloadMemoryLength](mtlmeshrenderpipelinedescriptor/payloadmemorylength.md)
- [rasterSampleCount](mtlmeshrenderpipelinedescriptor/rastersamplecount.md)
- [requiredThreadsPerMeshThreadgroup](mtlmeshrenderpipelinedescriptor/requiredthreadspermeshthreadgroup.md)
- [requiredThreadsPerObjectThreadgroup](mtlmeshrenderpipelinedescriptor/requiredthreadsperobjectthreadgroup.md)
- [shaderValidation](mtlmeshrenderpipelinedescriptor/shadervalidation.md) — A value that enables or disables shader validation for the pipeline.
- [stencilAttachmentPixelFormat](mtlmeshrenderpipelinedescriptor/stencilattachmentpixelformat.md)
- [supportIndirectCommandBuffers](mtlmeshrenderpipelinedescriptor/supportindirectcommandbuffers.md)

### Instance Methods

- [- reset](<mtlmeshrenderpipelinedescriptor/reset().md>)

## See Also

### Render pipeline states

- [MTLRenderPipelineState](mtlrenderpipelinestate.md) — An interface that represents a graphics pipeline configuration for a render pass, which the pass applies to the draw commands you encode.
- [MTL4RenderPipelineDescriptor](mtl4renderpipelinedescriptor.md) — Groups together properties to create a render pipeline state object.
- [MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md) — An argument of options you pass to a GPU device to get a render pipeline state.
- [MTLRenderPipelineFunctionsDescriptor](mtlrenderpipelinefunctionsdescriptor.md) — A collection of functions for updating a render pipeline.
- [MTL4MeshRenderPipelineDescriptor](mtl4meshrenderpipelinedescriptor.md) — Groups together properties you use to create a mesh render pipeline state object.
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
