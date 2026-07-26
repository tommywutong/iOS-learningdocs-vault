---
title: MTL4RenderPipelineDynamicLinkingDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4renderpipelinedynamiclinkingdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpipelinedynamiclinkingdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpipelinedynamiclinkingdescriptor.json'
content_hash: 'sha256:590f07a3f66e8d34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4RenderPipelineDynamicLinkingDescriptor

<sub>Class</sub>

Groups together properties that provide linking properties for render pipelines.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTL4RenderPipelineDynamicLinkingDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [fragmentLinkingDescriptor](mtl4renderpipelinedynamiclinkingdescriptor/fragmentlinkingdescriptor.md) — Controls properties for linking the fragment stage of the render pipeline.
- [meshLinkingDescriptor](mtl4renderpipelinedynamiclinkingdescriptor/meshlinkingdescriptor.md) — Controls properties for linking the mesh stage of the render pipeline.
- [objectLinkingDescriptor](mtl4renderpipelinedynamiclinkingdescriptor/objectlinkingdescriptor.md) — Controls properties for link the object stage of the render pipeline.
- [tileLinkingDescriptor](mtl4renderpipelinedynamiclinkingdescriptor/tilelinkingdescriptor.md) — Controls properties for linking the tile stage of the render pipeline.
- [vertexLinkingDescriptor](mtl4renderpipelinedynamiclinkingdescriptor/vertexlinkingdescriptor.md) — Controls properties for linking the vertex stage of the render pipeline.

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
- [MTLRenderPipelineColorAttachmentDescriptor](mtlrenderpipelinecolorattachmentdescriptor.md) — A color render target that specifies the color configuration and color operations for a render pipeline.
- [MTLRenderPipelineColorAttachmentDescriptorArray](mtlrenderpipelinecolorattachmentdescriptorarray.md) — An array of render pipeline color attachment descriptor objects.
- [MTL4TileRenderPipelineDescriptor](mtl4tilerenderpipelinedescriptor.md) — Groups together properties you use to create a tile render pipeline state object.
- [MTLTileRenderPipelineDescriptor](mtltilerenderpipelinedescriptor.md) — An object that configures new render pipeline state objects for tile shading.
- [MTLTileRenderPipelineColorAttachmentDescriptor](mtltilerenderpipelinecolorattachmentdescriptor.md) — A description of a tile-shading render pipeline’s color render target.
- [MTLPipelineOption](mtlpipelineoption.md) — Options that determine how Metal prepares the pipeline.
