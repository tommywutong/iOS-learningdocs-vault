---
title: MTLIndirectCommandBufferDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectcommandbufferdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandbufferdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandbufferdescriptor.json'
content_hash: 'sha256:a9fd4545b1b2deb1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIndirectCommandBufferDescriptor

<sub>Class</sub>

A configuration you create to customize an indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLIndirectCommandBufferDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Declaring command types to encode

- [commandTypes](mtlindirectcommandbufferdescriptor/commandtypes.md) — The set of command types that you can encode into the indirect command buffer.

### Declaring command inheritance

- [inheritBuffers](mtlindirectcommandbufferdescriptor/inheritbuffers.md) — A Boolean value that determines where commands in the indirect command buffer get their buffer arguments from when you execute them.
- [inheritPipelineState](mtlindirectcommandbufferdescriptor/inheritpipelinestate.md) — A Boolean value that determines where commands in the indirect command buffer get their pipeline state from when you execute them.

### Declaring the maximum number of argument buffers per command

- [maxVertexBufferBindCount](mtlindirectcommandbufferdescriptor/maxvertexbufferbindcount.md) — The maximum number of buffers that you can set per command for the vertex stage.
- [maxFragmentBufferBindCount](mtlindirectcommandbufferdescriptor/maxfragmentbufferbindcount.md) — The maximum number of buffers that you can set per command for the fragment stage.
- [maxKernelBufferBindCount](mtlindirectcommandbufferdescriptor/maxkernelbufferbindcount.md) — The maximum number of buffers that you can set per command for the compute kernel.

### Instance Properties

- [inheritCullMode](mtlindirectcommandbufferdescriptor/inheritcullmode.md) — Configures whether the indirect command buffer inherits the cull mode from the encoder.
- [inheritDepthBias](mtlindirectcommandbufferdescriptor/inheritdepthbias.md) — Configures whether the indirect command buffer inherits the depth bias from the encoder.
- [inheritDepthClipMode](mtlindirectcommandbufferdescriptor/inheritdepthclipmode.md) — Configures whether the indirect command buffer inherits the depth clip mode from the encoder.
- [inheritDepthStencilState](mtlindirectcommandbufferdescriptor/inheritdepthstencilstate.md) — Configures whether the indirect command buffer inherits the depth stencil state from the encoder.
- [inheritFrontFacingWinding](mtlindirectcommandbufferdescriptor/inheritfrontfacingwinding.md) — Configures whether the indirect command buffer inherits the front facing winding from the encoder.
- [inheritTriangleFillMode](mtlindirectcommandbufferdescriptor/inherittrianglefillmode.md) — Configures whether the indirect command buffer inherits the triangle fill mode from the encoder.
- [maxKernelThreadgroupMemoryBindCount](mtlindirectcommandbufferdescriptor/maxkernelthreadgroupmemorybindcount.md)
- [maxMeshBufferBindCount](mtlindirectcommandbufferdescriptor/maxmeshbufferbindcount.md)
- [maxObjectBufferBindCount](mtlindirectcommandbufferdescriptor/maxobjectbufferbindcount.md)
- [maxObjectThreadgroupMemoryBindCount](mtlindirectcommandbufferdescriptor/maxobjectthreadgroupmemorybindcount.md)
- [supportColorAttachmentMapping](mtlindirectcommandbufferdescriptor/supportcolorattachmentmapping.md) — Specifies if the indirect command buffer should support color attachment mapping.
- [supportDynamicAttributeStride](mtlindirectcommandbufferdescriptor/supportdynamicattributestride.md)
- [supportRayTracing](mtlindirectcommandbufferdescriptor/supportraytracing.md)

## See Also

### Indirect command buffers

- [Creating an indirect command buffer](creating-an-indirect-command-buffer.md) — Configure a descriptor to specify the properties of an indirect command buffer.
- [Specifying drawing and dispatch arguments indirectly](specifying-drawing-and-dispatch-arguments-indirectly.md) — Use indirect commands if you don’t know your draw or dispatch call arguments when you encode the command.
- [Encoding indirect command buffers on the CPU](encoding-indirect-command-buffers-on-the-cpu.md) — Reduce CPU overhead and simplify your command execution by reusing commands.
- [Encoding indirect command buffers on the GPU](encoding-indirect-command-buffers-on-the-gpu.md) — Maximize CPU to GPU parallelization by generating render commands on the GPU.
- [MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md) — A command buffer containing reusable commands, encoded either on the CPU or GPU.
- [MTLIndirectCommandType](mtlindirectcommandtype.md) — The types of commands that you can encode into the indirect command buffer.
- [MTLIndirectCommandBufferExecutionRange](mtlindirectcommandbufferexecutionrange.md) — A range of commands in an indirect command buffer.
- [MTLIndirectCommandBufferExecutionRangeMake](<mtlindirectcommandbufferexecutionrangemake(____).md>) — Creates a command execution range.
