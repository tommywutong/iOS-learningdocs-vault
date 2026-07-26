---
title: MTLTileRenderPipelineColorAttachmentDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltilerenderpipelinecolorattachmentdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtltilerenderpipelinecolorattachmentdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltilerenderpipelinecolorattachmentdescriptor.json'
content_hash: 'sha256:5ac3697aabb9512c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTileRenderPipelineColorAttachmentDescriptor

<sub>Class</sub>

A description of a tile-shading render pipeline’s color render target.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLTileRenderPipelineColorAttachmentDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Specifying pixel format

- [pixelFormat](mtltilerenderpipelinecolorattachmentdescriptor/pixelformat.md) — The pixel format associated with the tile shading render pipeline.

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
- [MTLPipelineOption](mtlpipelineoption.md) — Options that determine how Metal prepares the pipeline.
- [MTL4RenderPipelineBinaryFunctionsDescriptor](mtl4renderpipelinebinaryfunctionsdescriptor.md) — Allows you to specify additional binary functions to link to each stage of a render pipeline.
