---
title: MTL4RenderCommandEncoder
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4rendercommandencoder
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder.json'
content_hash: 'sha256:ac79158fe63364be'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4RenderCommandEncoder

<sub>Protocol</sub>

Encodes configuration and draw commands for a single render pass into a command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTL4RenderCommandEncoder : MTL4CommandEncoder
```

## Overview

A render pass draws a scene, or a component within a scene, to its render _attachments_, the outputs of a render pass. You can render to those outputs with various approaches, including techniques that apply the following:

- Primitive drawing
- Mesh drawing
- Ray tracing
- Dispatching tile shaders

Create a render encoder by calling a factory method of an [MTL4CommandBuffer](mtl4commandbuffer.md) instance, such as [- renderCommandEncoderWithDescriptor:options:](<mtl4commandbuffer/makerendercommandencoder(descriptor_options_).md>).

To configure the render pass for your first drawing commands, start with a pipeline state by passing an [MTLRenderPipelineState](mtlrenderpipelinestate.md) instance to the encoder’s [- setRenderPipelineState:](<mtl4rendercommandencoder/setrenderpipelinestate(__).md>) method. You create the pipeline states your render pass needs, typically ahead of time, by calling one or more [MTLDevice](mtldevice.md) methods (see [Pipeline state creation](pipeline-state-creation.md)).

> [!tip] Tip
> Avoid visual stutter by creating pipeline states at a noncritical time, such as during launch, because of the time it can take to make them.

Configure other encoder settings by calling the methods in the configuration groups below, such as [- setViewport:](<mtl4rendercommandencoder/setviewport(__).md>) for the viewport, [- setScissorRect:](<mtl4rendercommandencoder/setscissorrect(__).md>) for the scissor rectangle, and [- setDepthStencilState:](<mtl4rendercommandencoder/setdepthstencilstate(__).md>) for depth and stencil tests.

Bind resources by calling [- setArgumentTable:atStages:](<mtl4rendercommandencoder/setargumenttable(__stages_).md>) with an [MTL4ArgumentTable](mtl4argumenttable.md) instance. This table contains the buffers, textures, and other resources your shaders depend on.

Encode drawing commands after you configure the state and resources the commands depend on. The encoder maintains its current state and applies it to all subsequent draw commands. For drawing commands that need different states or resources, reconfigure the render pass appropriately and then encode those draw commands. Repeat the process for each batch of drawing commands that depend on the same render pass configuration and resources.

When you finish encoding the render pass’s commands, finalize it into the command buffer by calling the encoder’s [- endEncoding](<mtl4commandencoder/endencoding().md>) method.

### Command stages

Most render commands apply to one or more stages within a pass. The following table shows which stages apply to each command:

| Function | MTLStages |
|---|---|
| [- drawPrimitives:vertexStart:vertexCount:](<mtl4rendercommandencoder/drawprimitives(primitivetype_vertexstart_vertexcount_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawPrimitives:vertexStart:vertexCount:instanceCount:](<mtl4rendercommandencoder/drawprimitives(primitivetype_vertexstart_vertexcount_instancecount_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:](<mtl4rendercommandencoder/drawprimitives(primitivetype_vertexstart_vertexcount_instancecount_baseinstance_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawPrimitives:indirectBuffer:](<mtl4rendercommandencoder/drawprimitives(primitivetype_indirectbuffer_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:](<mtl4rendercommandencoder/drawindexedprimitives(primitivetype_indexcount_indextype_indexbuffer_indexbufferlength_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:](<mtl4rendercommandencoder/drawindexedprimitives(primitivetype_indexcount_indextype_indexbuffer_indexbufferlength_instancecount_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:baseVertex:baseInstance:](<mtl4rendercommandencoder/drawindexedprimitives(primitivetype_indexcount_indextype_indexbuffer_indexbufferlength_instancecount_basevertex_baseinstance_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawIndexedPrimitives:indexType:indexBuffer:indexBufferLength:indirectBuffer:](<mtl4rendercommandencoder/drawindexedprimitives(primitivetype_indextype_indexbuffer_indexbufferlength_indirectbuffer_).md>) | [MTLStageVertex](mtlstages/vertex.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<mtl4rendercommandencoder/drawmeshthreads(threadspergrid_threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) | [MTLStageObject](mtlstages/object.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageMesh](mtlstages/mesh.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<mtl4rendercommandencoder/drawmeshthreadgroups(threadgroupspergrid_threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) | [MTLStageObject](mtlstages/object.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageMesh](mtlstages/mesh.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- drawMeshThreadgroupsWithIndirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<mtl4rendercommandencoder/drawmeshthreadgroups(indirectbuffer_threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) | [MTLStageObject](mtlstages/object.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageMesh](mtlstages/mesh.md)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[MTLStageFragment](mtlstages/fragment.md) |
| [- dispatchThreadsPerTile:](<mtl4rendercommandencoder/dispatchthreadspertile(__).md>) | [MTLStageTile](mtlstages/tile.md) |
| [executeCommands(buffer:range:)](<mtl4rendercommandencoder/executecommands(buffer_range_).md>)![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[executeCommandsInBuffer:withRange:](mtl4rendercommandencoder/executecommandsinbuffer_withrange_.md) | None |
| [- executeCommandsInBuffer:indirectBuffer:](<mtl4rendercommandencoder/executecommands(buffer_indirectbuffer_).md>) | None |
| [- writeTimestampWithGranularity:afterStage:intoHeap:atIndex:](<mtl4rendercommandencoder/writetimestamp(granularity_after_counterheap_index_).md>) | None |

Draw commands don’t apply to [MTLStageFragment](mtlstages/fragment.md) when the [MTLRenderPipelineState](mtlrenderpipelinestate.md) for the draw disables rasterization. See [rasterizationEnabled](mtl4renderpipelinedescriptor/israsterizationenabled.md).

Mesh draw commands don’t apply to [MTLStageObject](mtlstages/object.md) when the [MTLRenderPipelineState](mtlrenderpipelinestate.md) for the draw doesn’t have an object shader.

The [executeCommands(buffer:range:)](<mtl4rendercommandencoder/executecommands(buffer_range_).md>) and [- executeCommandsInBuffer:indirectBuffer:](<mtl4rendercommandencoder/executecommands(buffer_indirectbuffer_).md>) commands don’t apply to any stage, which means you can’t use a barrier to wait for all commands in an indirect command buffer to complete. However, each command within the [MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md) applies to the same stages as when you encode the equivalent command directly.

For more information about stages and synchronization, see [MTLStages](mtlstages.md) and [Resource synchronization](resource-synchronization.md).

## Relationships

- **Inherits From**: [MTL4CommandEncoder](mtl4commandencoder.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring pipeline state

- [- setRenderPipelineState:](<mtl4rendercommandencoder/setrenderpipelinestate(__).md>) — Configures this encoder with a render pipeline state that applies to your subsequent draw commands.

### Configuring the actions for attachments

- [- setColorStoreAction:atIndex:](<mtl4rendercommandencoder/setcolorstoreaction(__index_).md>) — Configures the store action for a color attachment.
- [- setDepthStoreAction:](<mtl4rendercommandencoder/setdepthstoreaction(__).md>) — Configures the store action for the depth attachment.
- [- setStencilStoreAction:](<mtl4rendercommandencoder/setstencilstoreaction(__).md>) — Configures the store action for the stencil attachment.

### Configuring blend behavior

- [- setBlendColorRed:green:blue:alpha:](<mtl4rendercommandencoder/setblendcolor(red_green_blue_alpha_).md>) — Configures each pixel component value, including alpha, for the render pipeline’s constant blend color.
- [- setColorAttachmentMap:](<mtl4rendercommandencoder/setcolorattachmentmap(__).md>) — Sets the mapping from logical shader color output to physical render pass color attachments.

### Configuring rendering behavior

- [- setTriangleFillMode:](<mtl4rendercommandencoder/settrianglefillmode(__).md>) — Configures how subsequent draw commands rasterize triangle and triangle strip primitives.
- [- setFrontFacingWinding:](<mtl4rendercommandencoder/setfrontfacing(__).md>) — Configures the vertex winding order that determines which face of a geometric primitive is the front one.
- [- setCullMode:](<mtl4rendercommandencoder/setcullmode(__).md>) — Controls whether Metal culls front facing primitives, back facing primitives, or culls no primitives at all.

### Configuring depth and stencil behavior

- [- setDepthStencilState:](<mtl4rendercommandencoder/setdepthstencilstate(__).md>) — Configures this encoder with a depth stencil state that applies to your subsequent draw commands.
- [- setDepthBias:slopeScale:clamp:](<mtl4rendercommandencoder/setdepthbias(__slopescale_clamp_).md>) — Configures the adjustments a render pass applies to depth values from fragment shader functions by a scaling factor and bias.
- [- setDepthClipMode:](<mtl4rendercommandencoder/setdepthclipmode(__).md>) — Controls the behavior for fragments outside of the near or far planes.
- [setDepthTestBounds(_:)](<mtl4rendercommandencoder/setdepthtestbounds(__).md>) — Configures the range for depth bounds testing.
- [- setStencilReferenceValue:](<mtl4rendercommandencoder/setstencilreferencevalue(__).md>) — Configures this encoder with a reference value for stencil testing.
- [- setStencilFrontReferenceValue:backReferenceValue:](<mtl4rendercommandencoder/setstencilreferencevalue(front_back_).md>) — Configures the encoder with different stencil test reference values for front-facing and back-facing primitives.

### Configuring viewport and scissor behavior

- [- setViewport:](<mtl4rendercommandencoder/setviewport(__).md>) — Sets the viewport which that transforms vertices from normalized device coordinates to window coordinates.
- [setViewports(_:)](<mtl4rendercommandencoder/setviewports(__).md>) — Sets an array of viewports to transform vertices from normalized device coordinates to window coordinates.
- [- setScissorRect:](<mtl4rendercommandencoder/setscissorrect(__).md>) — Sets a scissor rectangle to discard fragments outside a specific area.
- [setScissorRects(_:)](<mtl4rendercommandencoder/setscissorrects(__).md>) — Sets an array of scissor rectangles for a fragment scissor test.

### Configuring visibility testing

- [- setVisibilityResultMode:offset:](<mtl4rendercommandencoder/setvisibilityresultmode(__offset_).md>) — Configures a visibility test for Metal to run, and the destination for any results it generates.

### Configuring vertex amplification

- [setVertexAmplificationCount(_:)](<mtl4rendercommandencoder/setvertexamplificationcount(__)-85tu1.md>) — Sets the vertex amplification count and its view mapping for each amplification ID.
- [setVertexAmplificationCount(_:)](<mtl4rendercommandencoder/setvertexamplificationcount(__)-911ja.md>) — Sets the vertex amplification count and its view mapping for each amplification ID.

### Configuring persistent threadgroup memory

- [- setObjectThreadgroupMemoryLength:atIndex:](<mtl4rendercommandencoder/setobjectthreadgroupmemorylength(__index_).md>) — Configures the size of a threadgroup memory buffer for a threadgroup argument in the object shader function.
- [- setThreadgroupMemoryLength:offset:atIndex:](<mtl4rendercommandencoder/setthreadgroupmemorylength(__offset_index_).md>) — Configures the size of a threadgroup memory buffer for a threadgroup argument in the fragment and tile shader functions.

### Binding argument tables

- [- setArgumentTable:atStages:](<mtl4rendercommandencoder/setargumenttable(__stages_).md>) — Associates an argument table with a set of render stages.

### Drawing with vertices

- [- drawPrimitives:vertexStart:vertexCount:](<mtl4rendercommandencoder/drawprimitives(primitivetype_vertexstart_vertexcount_).md>) — Encodes a draw command that renders an instance of a geometric primitive.
- [- drawPrimitives:vertexStart:vertexCount:instanceCount:](<mtl4rendercommandencoder/drawprimitives(primitivetype_vertexstart_vertexcount_instancecount_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive.
- [- drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:](<mtl4rendercommandencoder/drawprimitives(primitivetype_vertexstart_vertexcount_instancecount_baseinstance_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive, starting with a custom instance identification number.
- [- drawPrimitives:indirectBuffer:](<mtl4rendercommandencoder/drawprimitives(primitivetype_indirectbuffer_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive with indirect arguments.

### Drawing with indexed vertices

- [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:](<mtl4rendercommandencoder/drawindexedprimitives(primitivetype_indexcount_indextype_indexbuffer_indexbufferlength_).md>) — Encodes a draw command that renders an instance of a geometric primitive with indexed vertices.
- [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:](<mtl4rendercommandencoder/drawindexedprimitives(primitivetype_indexcount_indextype_indexbuffer_indexbufferlength_instancecount_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices.
- [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:baseVertex:baseInstance:](<mtl4rendercommandencoder/drawindexedprimitives(primitivetype_indexcount_indextype_indexbuffer_indexbufferlength_instancecount_basevertex_baseinstance_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices, starting with a custom vertex and instance.
- [- drawIndexedPrimitives:indexType:indexBuffer:indexBufferLength:indirectBuffer:](<mtl4rendercommandencoder/drawindexedprimitives(primitivetype_indextype_indexbuffer_indexbufferlength_indirectbuffer_).md>) — Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices and indirect arguments.

### Drawing with meshes

- [- drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<mtl4rendercommandencoder/drawmeshthreads(threadspergrid_threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) — Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threads.
- [- drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<mtl4rendercommandencoder/drawmeshthreadgroups(threadgroupspergrid_threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) — Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threadgroups.
- [- drawMeshThreadgroupsWithIndirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<mtl4rendercommandencoder/drawmeshthreadgroups(indirectbuffer_threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>) — Encodes a draw command that invokes a mesh shader and, optionally, an object shader with indirect arguments.

### Drawing with tile shaders

- [- dispatchThreadsPerTile:](<mtl4rendercommandencoder/dispatchthreadspertile(__).md>) — Encodes a command that invokes a tile shader function from the encoder’s current tile render pipeline state.
- [tileWidth](mtl4rendercommandencoder/tilewidth.md) — Sets the width of a tile for this render pass.
- [tileHeight](mtl4rendercommandencoder/tileheight.md) — Sets the height of a tile for this render pass.

### Running commands from indirect command buffers

- [executeCommands(buffer:range:)](<mtl4rendercommandencoder/executecommands(buffer_range_).md>) — Encodes a command that runs a range of commands from an indirect command buffer.
- [- executeCommandsInBuffer:indirectBuffer:](<mtl4rendercommandencoder/executecommands(buffer_indirectbuffer_).md>) — Encodes a command that runs an indirect range of commands from an indirect command buffer.

### Sampling counters

- [- writeTimestampWithGranularity:afterStage:intoHeap:atIndex:](<mtl4rendercommandencoder/writetimestamp(granularity_after_counterheap_index_).md>) — Writes a GPU timestamp into the given [MTL4CounterHeap](mtl4counterheap.md) at `index` after `stage` completes.

## See Also

### Encoding a render pass

- [MTLRenderCommandEncoder](mtlrendercommandencoder.md) — Encodes configuration and draw commands for a single render pass into a command buffer.
- [MTL4RenderEncoderOptions](mtl4renderencoderoptions.md) — Custom render pass options you specify at encoder creation time.
- [MTLTriangleFillMode](mtltrianglefillmode.md) — Specifies how to rasterize triangle and triangle strip primitives.
- [MTLWinding](mtlwinding.md) — The vertex winding rule that determines a front-facing primitive.
- [MTLCullMode](mtlcullmode.md) — The mode that determines whether to perform culling and which type of primitive to cull.
- [MTLPrimitiveType](mtlprimitivetype.md) — The geometric primitive type for drawing commands.
- [MTLIndexType](mtlindextype.md) — The index type for an index buffer that references vertices of geometric primitives.
- [MTLDepthClipMode](mtldepthclipmode.md) — The mode that determines how to deal with fragments outside of the near or far planes.
- [MTLVisibilityResultMode](mtlvisibilityresultmode.md) — The mode that determines what, if anything, the GPU writes to the results buffer, after the GPU executes the render pass.
- [MTLVisibilityResultType](mtlvisibilityresulttype.md) — This enumeration controls if Metal accumulates visibility results between render encoders or resets them.
