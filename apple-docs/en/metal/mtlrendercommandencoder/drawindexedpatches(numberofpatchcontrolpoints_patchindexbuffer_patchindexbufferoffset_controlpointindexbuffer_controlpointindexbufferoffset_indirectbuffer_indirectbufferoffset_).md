---
title: 'drawIndexedPatches(numberOfPatchControlPoints:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:indirectBuffer:indirectBufferOffset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/drawindexedpatches(numberofpatchcontrolpoints:patchindexbuffer:patchindexbufferoffset:controlpointindexbuffer:controlpointindexbufferoffset:indirectbuffer:indirectbufferoffset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/drawindexedpatches(numberofpatchcontrolpoints:patchindexbuffer:patchindexbufferoffset:controlpointindexbuffer:controlpointindexbufferoffset:indirectbuffer:indirectbufferoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/drawindexedpatches%28numberofpatchcontrolpoints%3Apatchindexbuffer%3Apatchindexbufferoffset%3Acontrolpointindexbuffer%3Acontrolpointindexbufferoffset%3Aindirectbuffer%3Aindirectbufferoffset%3A%29.json'
content_hash: 'sha256:3ae7b2c16fb0f4d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# drawIndexedPatches(numberOfPatchControlPoints:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:indirectBuffer:indirectBufferOffset:)

<sub>Instance Method</sub>

Encodes a draw command that renders multiple instances of tessellated patches with a control point index buffer and indirect arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func drawIndexedPatches(numberOfPatchControlPoints: Int, patchIndexBuffer: (any MTLBuffer)?, patchIndexBufferOffset: Int, controlPointIndexBuffer: any MTLBuffer, controlPointIndexBufferOffset: Int, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)
```

## Parameters

- `numberOfPatchControlPoints` — The number of control points for each patch, which needs to be in the range `[0, 32]`.

- `patchIndexBuffer` — An [MTLBuffer](../mtlbuffer.md) instance that contains the indices to patches.

- `patchIndexBufferOffset` — An integer that represents the location, in bytes, from the start of `patchIndexBuffer` where the patch indices begin.

- `controlPointIndexBuffer` — An [MTLBuffer](../mtlbuffer.md) instance that contains the indices to control points.

- `controlPointIndexBufferOffset` — An integer that represents the location, in bytes, from the start of `controlPointIndexBuffer` where the control point indices begin.

- `indirectBuffer` — An [MTLBuffer](../mtlbuffer.md) instance with data that matches the layout of the [MTLDrawPatchIndirectArguments](../mtldrawpatchindirectarguments.md) structure.

- `indirectBufferOffset` — An integer that represents the location, in bytes, from the start of `indirectBuffer` where the indirect arguments structure begins. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.

## Discussion

Indirect drawing methods may help your app avoid expensive latency costs. This is because the command reads arguments from an [MTLBuffer](../mtlbuffer.md) instance instead of using the CPU to pass parameters to the command.

The method records the encoder’s current rendering state and resources the command needs as it runs. You can safely change the encoder’s render pipeline state to encode other commands after calling this method. Subsequent changes to the state don’t affect the commands already in the encoder’s [MTLCommandBuffer](../mtlcommandbuffer.md).

## See Also

### Drawing with indexed tessellation patches

- [- drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:](<drawindexedpatches(numberofpatchcontrolpoints_patchstart_patchcount_patchindexbuffer_patchindexbufferoffset_controlpointindexbuffer_controlpointindexbufferoffse-12f3c1a50f.md>) — Encodes a draw command that renders multiple instances of tessellated patches with a control point index buffer.
