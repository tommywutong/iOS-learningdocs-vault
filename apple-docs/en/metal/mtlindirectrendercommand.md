---
title: MTLIndirectRenderCommand
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectrendercommand
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectrendercommand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectrendercommand.json'
content_hash: 'sha256:a9d88f4865807e92'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIndirectRenderCommand

<sub>Protocol</sub>

A render command in an indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLIndirectRenderCommand : NSObjectProtocol
```

## Overview

Don’t implement this protocol; you get instances of this type by asking an [MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md) for them.

Use this instance to reset or encode a command. You need to reset a command before encoding a new command.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Setting command arguments

- [- setRenderPipelineState:](<mtlindirectrendercommand/setrenderpipelinestate(__).md>) — Sets the render pipeline state for the command.
- [- setVertexBuffer:offset:atIndex:](<mtlindirectrendercommand/setvertexbuffer(__offset_at_).md>) — Sets a vertex buffer argument for the command.
- [- setFragmentBuffer:offset:atIndex:](<mtlindirectrendercommand/setfragmentbuffer(__offset_at_).md>) — Sets a fragment buffer argument for the command.

### Encoding a drawing command

- [- drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:](<mtlindirectrendercommand/drawprimitives(__vertexstart_vertexcount_instancecount_baseinstance_).md>) — Encodes a command to render a number of instances of primitives using vertex data in contiguous array elements, starting from the base instance.
- [- drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:](<mtlindirectrendercommand/drawindexedprimitives(__indexcount_indextype_indexbuffer_indexbufferoffset_instancecount_basevertex_baseinstance_).md>) — Encodes a command to render a number of instances of primitives using an index list specified in a buffer, starting from the base vertex of the base instance.
- [- drawPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:tessellationFactorBuffer:tessellationFactorBufferOffset:tessellationFactorBufferInstanceStride:](<mtlindirectrendercommand/drawpatches(__patchstart_patchcount_patchindexbuffer_patchindexbufferoffset_instancecount_baseinstance_tessellationfactorbuffer_tessellationfactorbufferoffset_t-ba3eb562c3.md>) — Encodes a command to render a number of instances of tessellated patches.
- [- drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:tessellationFactorBuffer:tessellationFactorBufferOffset:tessellationFactorBufferInstanceStride:](<mtlindirectrendercommand/drawindexedpatches(__patchstart_patchcount_patchindexbuffer_patchindexbufferoffset_controlpointindexbuffer_controlpointindexbufferoffset_instancecount_baseinsta-1368a335e3.md>) — Encodes a command to render a number of instances of tessellated patches, using a control point index buffer.

### Resetting a command

- [- reset](<mtlindirectrendercommand/reset().md>) — Resets the command to its default state.

### Instance Methods

- [- clearBarrier](<mtlindirectrendercommand/clearbarrier().md>)
- [- drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<mtlindirectrendercommand/drawmeshthreadgroups(__threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>)
- [- drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:](<mtlindirectrendercommand/drawmeshthreads(__threadsperobjectthreadgroup_threadspermeshthreadgroup_).md>)
- [- setBarrier](<mtlindirectrendercommand/setbarrier().md>)
- [- setCullMode:](<mtlindirectrendercommand/setcullmode(__).md>)
- [- setDepthBias:slopeScale:clamp:](<mtlindirectrendercommand/setdepthbias(__slopescale_clamp_).md>)
- [- setDepthClipMode:](<mtlindirectrendercommand/setdepthclipmode(__).md>)
- [- setDepthStencilState:](<mtlindirectrendercommand/setdepthstencilstate(__).md>)
- [- setFrontFacingWinding:](<mtlindirectrendercommand/setfrontfacing(__).md>)
- [- setMeshBuffer:offset:atIndex:](<mtlindirectrendercommand/setmeshbuffer(__offset_at_).md>)
- [- setObjectBuffer:offset:atIndex:](<mtlindirectrendercommand/setobjectbuffer(__offset_at_).md>)
- [- setObjectThreadgroupMemoryLength:atIndex:](<mtlindirectrendercommand/setobjectthreadgroupmemorylength(__index_).md>)
- [- setTriangleFillMode:](<mtlindirectrendercommand/settrianglefillmode(__).md>)
- [- setVertexBuffer:offset:attributeStride:atIndex:](<mtlindirectrendercommand/setvertexbuffer(__offset_attributestride_at_).md>)

## See Also

### Render compute commands

- [MTLDrawPatchIndirectArguments](mtldrawpatchindirectarguments.md) — The data layout required for drawing patches via indirect buffer calls.
- [MTLDrawPrimitivesIndirectArguments](mtldrawprimitivesindirectarguments.md) — The data layout required for drawing primitives via indirect buffer calls.
- [MTLDrawIndexedPrimitivesIndirectArguments](mtldrawindexedprimitivesindirectarguments.md) — The data layout required for drawing indexed primitives via indirect buffer calls.
