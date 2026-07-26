---
title: MTLRenderCommandEncoder
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrendercommandencoder
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder.json'
content_hash: 'sha256:50e110dc8654622f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLRenderCommandEncoder

<sub>Protocol</sub>

Encodes configuration and draw commands for a single render pass into a command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLRenderCommandEncoder : MTLCommandEncoder
```

## Overview

A render pass draws a scene, or a component within a scene, to its render _attachments_, the outputs of a render pass. You can render to those outputs with various approaches, including techniques that apply the following:

- Primitive drawing
- Mesh drawing
- Ray tracing
- Dispatching tile shaders

To create an [MTLRenderCommandEncoder](mtlrendercommandencoder.md) instance, call the [- renderCommandEncoderWithDescriptor:](<mtlcommandbuffer/makerendercommandencoder(descriptor_).md>) method of an [MTLCommandBuffer](mtlcommandbuffer.md) instance, or the [- renderCommandEncoder](<mtlparallelrendercommandencoder/makerendercommandencoder().md>) method of an [MTLParallelRenderCommandEncoder](mtlparallelrendercommandencoder.md) instance.

To configure the render pass for your first drawing commands, start with a pipeline state by passing an [MTLRenderPipelineState](mtlrenderpipelinestate.md) instance to the encoder’s [- setRenderPipelineState:](<mtlrendercommandencoder/setrenderpipelinestate(__).md>) method. You create the pipeline states your render pass needs, typically ahead of time, by calling one or more [MTLDevice](mtldevice.md) methods (see [Pipeline state creation](pipeline-state-creation.md)).

> [!tip] Tip
> Avoid visual stutter by creating pipeline states at a noncritical time, such as during launch, because of the time it can take to make them.

Configure other encoder settings by calling the methods on the [Render pass configuration](render-pass-configuration.md) page. For example, you may need to configure the pass’s viewport, its scissor rectangle, and the settings for depth and stencil tests.

Assign resources, such as buffers and textures, for the shaders that depend on them. For more information, see the shader-specific pages in the resource preparation section, such as [Vertex shader resource preparation commands](vertex-shader-resource-preparation-commands.md) and [Fragment shader resource preparation commands](fragment-shader-resource-preparation-commands.md). If your shaders access resources through an argument buffer, make those resources _resident_ in GPU memory by calling the methods on the [Argument buffer resource preparation commands](argument-buffer-resource-preparation-commands.md) page.

Encode drawing commands after you configure the state and resources the commands depend on. The encoder maintains its current state and applies it to all subsequent draw commands. For drawing commands that need different states or resources, reconfigure the render pass appropriately and then encode those draw commands. Repeat the process for each batch of drawing commands that depend on the same render pass configuration and resources.

When you finish encoding the render pass’s commands, finalize it into the command buffer by calling the encoder’s [- endEncoding](<mtlcommandencoder/endencoding().md>) method.

### Command stages

Most render commands apply to one or more stages within a pass. The following table shows which stages apply to each command:

| Function | MTLStages |
|---|---|
| [- drawPrimitives:vertexStart:vertexCount:](<mtlrendercommandencoder/drawprimitives(type_vertexstart_vertexcount_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawPrimitives:vertexStart:vertexCount:instanceCount:](<mtlrendercommandencoder/drawprimitives(type_vertexstart_vertexcount_instancecount_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:](<mtlrendercommandencoder/drawprimitives(type_vertexstart_vertexcount_instancecount_baseinstance_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawPrimitives:indirectBuffer:indirectBufferOffset:](<mtlrendercommandencoder/drawprimitives(type_indirectbuffer_indirectbufferoffset_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:](<mtlrendercommandencoder/drawindexedprimitives(type_indexcount_indextype_indexbuffer_indexbufferoffset_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:](<mtlrendercommandencoder/drawindexedprimitives(type_indexcount_indextype_indexbuffer_indexbufferoffset_instancecount_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:](<mtlrendercommandencoder/drawindexedprimitives(type_indexcount_indextype_indexbuffer_indexbufferoffset_instancecount_basevertex_baseinstance_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawIndexedPrimitives:indexType:indexBuffer:indexBufferOffset:indirectBuffer:indirectBufferOffset:](<mtlrendercommandencoder/drawindexedprimitives(type_indextype_indexbuffer_indexbufferoffset_indirectbuffer_indirectbufferoffset_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<mtlrendercommandencoder/drawmeshthreads(__threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) | [MTLStageObject](mtlstages/object.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageMesh](mtlstages/mesh.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<mtlrendercommandencoder/drawmeshthreadgroups(__threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) | [MTLStageObject](mtlstages/object.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageMesh](mtlstages/mesh.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawMeshThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<mtlrendercommandencoder/drawmeshthreadgroups(indirectbuffer_indirectbufferoffset_threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) | [MTLStageObject](mtlstages/object.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageMesh](mtlstages/mesh.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:](<mtlrendercommandencoder/drawpatches(numberofpatchcontrolpoints_patchstart_patchcount_patchindexbuffer_patchindexbufferoffset_instancecount_baseinstance_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawPatches:patchIndexBuffer:patchIndexBufferOffset:indirectBuffer:indirectBufferOffset:](<mtlrendercommandencoder/drawpatches(numberofpatchcontrolpoints_patchindexbuffer_patchindexbufferoffset_indirectbuffer_indirectbufferoffset_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:](<mtlrendercommandencoder/drawindexedpatches(numberofpatchcontrolpoints_patchstart_patchcount_patchindexbuffer_patchindexbufferoffset_controlpointindexbuffer_controlpointindexbufferoffse-12f3c1a50f.md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawIndexedPatches:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:indirectBuffer:indirectBufferOffset:](<mtlrendercommandencoder/drawindexedpatches(numberofpatchcontrolpoints_patchindexbuffer_patchindexbufferoffset_controlpointindexbuffer_controlpointindexbufferoffset_indirectbuffer_indirectbufferoffset_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- dispatchThreadsPerTile:](<mtlrendercommandencoder/dispatchthreadspertile(__).md>) | [MTLStageTile](mtlstages/tile.md) |
| [executeCommandsInBuffer(_:range:)](<mtlrendercommandencoder/executecommandsinbuffer(__range_).md>)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[executeCommandsInBuffer:withRange:](mtlrendercommandencoder/executecommandsinbuffer_withrange_.md) | None |
| [executeCommandsInBuffer(_:indirectBuffer:offset:)](<mtlrendercommandencoder/executecommandsinbuffer(__indirectbuffer_offset_).md>)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:](mtlrendercommandencoder/executecommandsinbuffer_indirectbuffer_indirectbufferoffset_.md) | None |
| [- sampleCountersInBuffer:atSampleIndex:withBarrier:](<mtlrendercommandencoder/samplecounters(samplebuffer_sampleindex_barrier_).md>) | None |

Draw commands don’t apply to [MTLStageFragment](mtlstages/fragment.md) when the [MTLRenderPipelineState](mtlrenderpipelinestate.md) for the draw disables rasterization. See [rasterizationEnabled](mtlrenderpipelinedescriptor/israsterizationenabled.md).

Mesh draw commands don’t apply to [MTLStageObject](mtlstages/object.md) when the [MTLRenderPipelineState](mtlrenderpipelinestate.md) for the draw doesn’t have an object shader.

The [executeCommandsInBuffer(_:range:)](<mtlrendercommandencoder/executecommandsinbuffer(__range_).md>) and [executeCommandsInBuffer(_:indirectBuffer:offset:)](<mtlrendercommandencoder/executecommandsinbuffer(__indirectbuffer_offset_).md>) commands don’t apply to any stage, which means you can’t use a barrier to wait for all commands in an indirect command buffer to complete. However, each command within the [MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md) applies to the same stages as when you encode the equivalent command directly.

> [!note] Note
> [MTLRenderStages](mtlrenderstages.md) and its values have the same functionality as [MTLStages](mtlstages.md) and its corresponding stage values.

For more information about stages and synchronization, see [MTLStages](mtlstages.md) and [Resource synchronization](resource-synchronization.md).

## Relationships

- **Inherits From**: [MTLCommandEncoder](mtlcommandencoder.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuration commands

- [Render pass configuration](render-pass-configuration.md) — Set a render pass’s pipeline state, attachment actions, viewports, and so on, that affect subsequent drawing commands.

### Resource preparation commands

- [Mesh and object shader resource preparation commands](mesh-and-object-shader-resource-preparation-commands.md) — Assign resources to mesh and object shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Vertex shader resource preparation commands](vertex-shader-resource-preparation-commands.md) — Assign resources to vertex shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Fragment shader resource preparation commands](fragment-shader-resource-preparation-commands.md) — Assign resources to fragment shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Tile shaders resource preparation commands](tile-shaders-resource-preparation-commands.md) — Assign resources to tile shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Argument buffer resource preparation commands](argument-buffer-resource-preparation-commands.md) — Load individual resources and multiple resources within a heap into GPU memory so that they’re available to shaders through argument buffers.

### Drawing with vertices

- [- drawPrimitives:vertexStart:vertexCount:](<mtlrendercommandencoder/drawprimitives(type_vertexstart_vertexcount_).md>) — Encodes a draw command that renders an instance of a geometric primitive.
- [- drawPrimitives:vertexStart:vertexCount:instanceCount:](<mtlrendercommandencoder/drawprimitives(type_vertexstart_vertexcount_instancecount_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive.
- [- drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:](<mtlrendercommandencoder/drawprimitives(type_vertexstart_vertexcount_instancecount_baseinstance_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive that starts with a custom instance identification number.
- [- drawPrimitives:indirectBuffer:indirectBufferOffset:](<mtlrendercommandencoder/drawprimitives(type_indirectbuffer_indirectbufferoffset_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive with indirect arguments.

### Drawing with indexed vertices

- [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:](<mtlrendercommandencoder/drawindexedprimitives(type_indexcount_indextype_indexbuffer_indexbufferoffset_).md>) — Encodes a draw command that renders an instance of a geometric primitive with indexed vertices.
- [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:](<mtlrendercommandencoder/drawindexedprimitives(type_indexcount_indextype_indexbuffer_indexbufferoffset_instancecount_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices.
- [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:](<mtlrendercommandencoder/drawindexedprimitives(type_indexcount_indextype_indexbuffer_indexbufferoffset_instancecount_basevertex_baseinstance_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices, starting with a custom vertex and instance.
- [- drawIndexedPrimitives:indexType:indexBuffer:indexBufferOffset:indirectBuffer:indirectBufferOffset:](<mtlrendercommandencoder/drawindexedprimitives(type_indextype_indexbuffer_indexbufferoffset_indirectbuffer_indirectbufferoffset_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices and indirect arguments.

### Drawing with meshes

- [- drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<mtlrendercommandencoder/drawmeshthreads(__threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) — Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threads.
- [- drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<mtlrendercommandencoder/drawmeshthreadgroups(__threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) — Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threadgroups.
- [- drawMeshThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<mtlrendercommandencoder/drawmeshthreadgroups(indirectbuffer_indirectbufferoffset_threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) — Encodes a draw command that invokes a mesh shader and, optionally, an object shader with indirect arguments.

### Drawing with tessellation patches

- [- drawPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:](<mtlrendercommandencoder/drawpatches(numberofpatchcontrolpoints_patchstart_patchcount_patchindexbuffer_patchindexbufferoffset_instancecount_baseinstance_).md>) — Encodes a draw command that renders multiple instances of tessellated patches.
- [- drawPatches:patchIndexBuffer:patchIndexBufferOffset:indirectBuffer:indirectBufferOffset:](<mtlrendercommandencoder/drawpatches(numberofpatchcontrolpoints_patchindexbuffer_patchindexbufferoffset_indirectbuffer_indirectbufferoffset_).md>) — Encodes a draw command that renders multiple instances of tessellated patches with indirect arguments.

### Drawing with indexed tessellation patches

- [- drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:](<mtlrendercommandencoder/drawindexedpatches(numberofpatchcontrolpoints_patchstart_patchcount_patchindexbuffer_patchindexbufferoffset_controlpointindexbuffer_controlpointindexbufferoffse-12f3c1a50f.md>) — Encodes a draw command that renders multiple instances of tessellated patches with a control point index buffer.
- [- drawIndexedPatches:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:indirectBuffer:indirectBufferOffset:](<mtlrendercommandencoder/drawindexedpatches(numberofpatchcontrolpoints_patchindexbuffer_patchindexbufferoffset_controlpointindexbuffer_controlpointindexbufferoffset_indirectbuffer_indirectbufferoffset_).md>) — Encodes a draw command that renders multiple instances of tessellated patches with a control point index buffer and indirect arguments.

### Drawing with tile shaders

- [- dispatchThreadsPerTile:](<mtlrendercommandencoder/dispatchthreadspertile(__).md>) — Encodes a command that invokes GPU functions from the encoder’s current tile render pipeline state.
- [tileWidth](mtlrendercommandencoder/tilewidth.md) — The width of the tiles, in pixels, for the render command encoder.
- [tileHeight](mtlrendercommandencoder/tileheight.md) — The height of the tiles, in pixels, for the render command encoder.

### Preventing resource access conflicts

- [- waitForFence:beforeStages:](<mtlrendercommandencoder/waitforfence(__before_).md>) — Encodes a command that instructs the GPU to pause before starting one or more stages of the render pass until a pass updates a fence.
- [- updateFence:afterStages:](<mtlrendercommandencoder/updatefence(__after_).md>) — Encodes a command that instructs the GPU to update a fence after one or more stages, which can unblock other passes waiting for the fence.
- [memoryBarrier(resources:after:before:)](<mtlrendercommandencoder/memorybarrier(resources_after_before_).md>) — Creates a memory barrier that enforces the order of write and read operations for specific resources.
- [- memoryBarrierWithScope:afterStages:beforeStages:](<mtlrendercommandencoder/memorybarrier(scope_after_before_).md>) — Creates a memory barrier that enforces the order of write and read operations for specific resource types.

### Running commands from indirect command buffers

- [executeCommandsInBuffer(_:range:)](<mtlrendercommandencoder/executecommandsinbuffer(__range_).md>) — Encodes a command that runs a range of commands from an indirect command buffer (ICB).
- [executeCommandsInBuffer(_:indirectBuffer:offset:)](<mtlrendercommandencoder/executecommandsinbuffer(__indirectbuffer_offset_).md>) — Encodes a command that runs an indirect range of commands from an indirect command buffer (ICB).

### Sampling counters

- [- sampleCountersInBuffer:atSampleIndex:withBarrier:](<mtlrendercommandencoder/samplecounters(samplebuffer_sampleindex_barrier_).md>) — Encodes a command that samples hardware counters during the render pass and stores the data into a counter sample buffer.

### Deprecated

- [Deprecated symbols](deprecated-symbols.md) — Review unsupported symbols and their replacements.

## See Also

### Encoding a render pass

- [MTL4RenderCommandEncoder](mtl4rendercommandencoder.md) — Encodes configuration and draw commands for a single render pass into a command buffer.
- [MTL4RenderEncoderOptions](mtl4renderencoderoptions.md) — Custom render pass options you specify at encoder creation time.
- [MTLTriangleFillMode](mtltrianglefillmode.md) — Specifies how to rasterize triangle and triangle strip primitives.
- [MTLWinding](mtlwinding.md) — The vertex winding rule that determines a front-facing primitive.
- [MTLCullMode](mtlcullmode.md) — The mode that determines whether to perform culling and which type of primitive to cull.
- [MTLPrimitiveType](mtlprimitivetype.md) — The geometric primitive type for drawing commands.
- [MTLIndexType](mtlindextype.md) — The index type for an index buffer that references vertices of geometric primitives.
- [MTLDepthClipMode](mtldepthclipmode.md) — The mode that determines how to deal with fragments outside of the near or far planes.
- [MTLVisibilityResultMode](mtlvisibilityresultmode.md) — The mode that determines what, if anything, the GPU writes to the results buffer, after the GPU executes the render pass.
- [MTLVisibilityResultType](mtlvisibilityresulttype.md) — This enumeration controls if Metal accumulates visibility results between render encoders or resets them.
