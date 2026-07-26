---
title: 'drawPatches(numberOfPatchControlPoints:patchIndexBuffer:patchIndexBufferOffset:indirectBuffer:indirectBufferOffset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/drawpatches(numberofpatchcontrolpoints:patchindexbuffer:patchindexbufferoffset:indirectbuffer:indirectbufferoffset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/drawpatches(numberofpatchcontrolpoints:patchindexbuffer:patchindexbufferoffset:indirectbuffer:indirectbufferoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/drawpatches%28numberofpatchcontrolpoints%3Apatchindexbuffer%3Apatchindexbufferoffset%3Aindirectbuffer%3Aindirectbufferoffset%3A%29.json'
content_hash: 'sha256:b2f4d2259c0f1459'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# drawPatches(numberOfPatchControlPoints:patchIndexBuffer:patchIndexBufferOffset:indirectBuffer:indirectBufferOffset:)

<sub>Instance Method</sub>

Encodes a draw command that renders multiple instances of tessellated patches with indirect arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func drawPatches(numberOfPatchControlPoints: Int, patchIndexBuffer: (any MTLBuffer)?, patchIndexBufferOffset: Int, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)
```

## Parameters

- `numberOfPatchControlPoints` — The number of control points for each patch, which needs to be in the range `[0, 32]`.

- `patchIndexBuffer` — An [MTLBuffer](../mtlbuffer.md) instance that contains the indices to patches.

- `patchIndexBufferOffset` — An integer that represents the location, in bytes, from the start of `patchIndexBuffer` where the patch indices begin.

- `indirectBuffer` — An [MTLBuffer](../mtlbuffer.md) instance with data that matches the layout of the [MTLDrawPatchIndirectArguments](../mtldrawpatchindirectarguments.md) structure.

- `indirectBufferOffset` — An integer that represents the location, in bytes, from the start of `indirectBuffer` where the indirect arguments structure begins. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.

## Discussion

Indirect drawing methods may help your app avoid expensive latency costs. This is because the command reads arguments from an [MTLBuffer](../mtlbuffer.md) instance instead of using the CPU to pass parameters to the command.

The method records the encoder’s current rendering state and resources the command needs as it runs. You can safely change the encoder’s render pipeline state to encode other commands after calling this method. Subsequent changes to the state don’t affect the commands already in the encoder’s [MTLCommandBuffer](../mtlcommandbuffer.md).

## See Also

### Drawing with tessellation patches

- [- drawPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:](<drawpatches(numberofpatchcontrolpoints_patchstart_patchcount_patchindexbuffer_patchindexbufferoffset_instancecount_baseinstance_).md>) — Encodes a draw command that renders multiple instances of tessellated patches.
