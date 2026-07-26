---
title: MTLRenderPipelineState
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinestate
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate.json'
content_hash: 'sha256:954657448da08e25'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLRenderPipelineState

<sub>Protocol</sub>

An interface that represents a graphics pipeline configuration for a render pass, which the pass applies to the draw commands you encode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLRenderPipelineState : MTLAllocation, Sendable
```

## Overview

The [MTLRenderPipelineState](mtlrenderpipelinestate.md) protocol is an interface that represents a specific configuration for the graphics-rendering pipeline, including which shaders it uses. Use a pipeline state to configure a render pass by calling the [- setRenderPipelineState:](<mtlrendercommandencoder/setrenderpipelinestate(__).md>) method of an [MTLRenderCommandEncoder](mtlrendercommandencoder.md) instance.

To create a pipeline state, call the appropriate [MTLDevice](mtldevice.md) method (see [Pipeline state creation](pipeline-state-creation.md)). You typically make pipeline states at a noncritical time, like when the app first launches. This is because graphics drivers may need time to evaluate and build each pipeline state. However, you can quickly use and reuse each pipeline state throughout your app’s lifetime.

## Relationships

- **Inherits From**: [MTLAllocation](mtlallocation.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying a pipeline state

- [device](mtlrenderpipelinestate/device.md) — The device instance that creates the pipeline state.
- [label](mtlrenderpipelinestate/label.md) — A string that helps you identify the render pipeline state during debugging.
- [gpuResourceID](mtlrenderpipelinestate/gpuresourceid.md) — An unique identifier that represents the pipeline state, which you can add to an argument buffer.

### Checking object shader memory requirements

- [maxTotalThreadsPerObjectThreadgroup](mtlrenderpipelinestate/maxtotalthreadsperobjectthreadgroup.md) — The largest number of threads the pipeline state can have in a single object shader threadgroup.
- [objectThreadExecutionWidth](mtlrenderpipelinestate/objectthreadexecutionwidth.md) — The number of threads the render pass applies to a SIMD group for an object shader.

### Checking mesh shader memory requirements

- [maxTotalThreadsPerMeshThreadgroup](mtlrenderpipelinestate/maxtotalthreadspermeshthreadgroup.md) — The largest number of threads the pipeline state can have in a single mesh shader threadgroup.
- [maxTotalThreadgroupsPerMeshGrid](mtlrenderpipelinestate/maxtotalthreadgroupspermeshgrid.md) — The largest number of threadgroups the pipeline state can have in a single mesh shader grid.
- [meshThreadExecutionWidth](mtlrenderpipelinestate/meshthreadexecutionwidth.md) — The number of threads the render pass applies to a SIMD group for a mesh shader.

### Checking tile shader memory requirements

- [maxTotalThreadsPerThreadgroup](mtlrenderpipelinestate/maxtotalthreadsperthreadgroup.md) — The largest number of threads the pipeline state can have in a single tile shader threadgroup.
- [threadgroupSizeMatchesTileSize](mtlrenderpipelinestate/threadgroupsizematchestilesize.md) — A Boolean value that indicates whether the pipeline state needs a threadgroup’s size to equal a tile’s size.
- [imageblockSampleLength](mtlrenderpipelinestate/imageblocksamplelength.md) — The memory size, in byes, of the render pipeline’s imageblock for a single sample.
- [- imageblockMemoryLengthForDimensions:](<mtlrenderpipelinestate/imageblockmemorylength(fordimensions_).md>) — Returns the length of an imageblock’s memory for the specified imageblock dimensions.

### Checking feature support

- [supportIndirectCommandBuffers](mtlrenderpipelinestate/supportindirectcommandbuffers.md) — A Boolean value that indicates whether the render pipeline supports encoding commands into an indirect command buffer.

### Checking shader validation

- [shaderValidation](mtlrenderpipelinestate/shadervalidation.md) — The current state of shader validation for the pipeline.

### Creating function handles and tables

- [- functionHandleWithFunction:stage:](<mtlrenderpipelinestate/functionhandle(function_stage_)-7uvul.md>) — Creates a function handle for a shader.
- [- newVisibleFunctionTableWithDescriptor:stage:](<mtlrenderpipelinestate/makevisiblefunctiontable(descriptor_stage_).md>) — Creates a new visible function table.
- [- newIntersectionFunctionTableWithDescriptor:stage:](<mtlrenderpipelinestate/makeintersectionfunctiontable(descriptor_stage_).md>) — Creates a new intersection function table.

### Creating modified clones of the render pipeline

- [- newRenderPipelineStateWithAdditionalBinaryFunctions:error:](<mtlrenderpipelinestate/makerenderpipelinestate(additionalbinaryfunctions_)-84te1.md>) — Creates a new pipeline state that’s a copy of the current pipeline state with additional shaders.

### Instance Properties

- [reflection](mtlrenderpipelinestate/reflection.md) — The render pipeline’s reflection information, if available.
- [requiredThreadsPerMeshThreadgroup](mtlrenderpipelinestate/requiredthreadspermeshthreadgroup.md)
- [requiredThreadsPerObjectThreadgroup](mtlrenderpipelinestate/requiredthreadsperobjectthreadgroup.md)
- [requiredThreadsPerTileThreadgroup](mtlrenderpipelinestate/requiredthreadspertilethreadgroup.md)

### Instance Methods

- [- functionHandleWithBinaryFunction:stage:](<mtlrenderpipelinestate/functionhandle(function_stage_)-1pgxo.md>) — Obtains the function handle for a specific function this pipeline state links at the binary level.
- [- functionHandleWithName:stage:](<mtlrenderpipelinestate/functionhandle(withname_stage_).md>) — Obtains a function handle for the a specific function this pipeline links at the Metal IR level.
- [- newRenderPipelineDescriptorForSpecialization](<mtlrenderpipelinestate/makerenderpipelinedescriptorforspecialization().md>) — Creates a render pipeline descriptor from this pipeline that you can use for pipeline specialization.
- [- newRenderPipelineStateWithBinaryFunctions:error:](<mtlrenderpipelinestate/makerenderpipelinestate(additionalbinaryfunctions_)-49r1w.md>) — Creates a new render pipeline state by adding binary functions to each stage of this pipeline state.

## See Also

### Render pipeline states

- [MTL4RenderPipelineDescriptor](mtl4renderpipelinedescriptor.md) — Groups together properties to create a render pipeline state object.
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
