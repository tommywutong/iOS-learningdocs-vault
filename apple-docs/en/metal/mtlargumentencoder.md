---
title: MTLArgumentEncoder
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlargumentencoder
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder.json'
content_hash: 'sha256:1ac11174f599cc60'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLArgumentEncoder

<sub>Protocol</sub>

An interface you can use to encode argument data into an argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLArgumentEncoder : NSObjectProtocol
```

## Overview

An [MTLArgumentEncoder](mtlargumentencoder.md) instance encodes buffers, textures, samplers, and inlined constant data into an argument buffer. An [MTLBuffer](mtlbuffer.md) instance represents the argument buffer that you set as the encoding destination by calling the [- setArgumentBuffer:offset:](<mtlargumentencoder/setargumentbuffer(__offset_).md>) method.

The recommended way to declare an argument buffer is to define its structure in your Metal shading language code. You can assign the argument buffer to a function’s specific buffer index. To create an encoder for this type of argument buffer, call one of the following [MTLFunction](mtlfunction.md) methods:

- [- newArgumentEncoderWithBufferIndex:](<mtlfunction/makeargumentencoder(bufferindex_).md>)
- [- newArgumentEncoderWithBufferIndex:reflection:](<mtlfunction/makeargumentencoder(bufferindex_reflection_).md>)

If you construct your shaders dynamically at runtime, you can still construct argument buffers as parameters for the shader. Define each argument separately and then add it to an array of [MTLArgumentDescriptor](mtlargumentdescriptor.md) instances. To create an encoder for this type of argument buffer, call the [- newArgumentEncoderWithArguments:](<mtldevice/makeargumentencoder(arguments_).md>) method of the [MTLDevice](mtldevice.md) class.

> [!important] Important
> A runtime validation error occurs if you create a `MTLArgumentEncoder` instance using structures that don’t reference any other resources and don’t provide any `[[id()]]` annotation on any of their members.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an argument buffer

- [- setArgumentBuffer:offset:](<mtlargumentencoder/setargumentbuffer(__offset_).md>) — Specifies the position in a buffer where the encoder writes argument data.
- [- setArgumentBuffer:startOffset:arrayElement:](<mtlargumentencoder/setargumentbuffer(__startoffset_arrayelement_).md>) — Specifies an array element within a buffer where the encoder writes argument data.
- [encodedLength](mtlargumentencoder/encodedlength.md) — The number of bytes required to store the encoded resources of an argument buffer.

### Encoding buffers

- [- setBuffer:offset:atIndex:](<mtlargumentencoder/setbuffer(__offset_index_).md>) — Encodes a reference to a buffer into the argument buffer.
- [setBuffers(_:offsets:range:)](<mtlargumentencoder/setbuffers(__offsets_range_).md>) — Encodes references to an array of buffers into the argument buffer.

### Encoding textures

- [- setTexture:atIndex:](<mtlargumentencoder/settexture(__index_).md>) — Encodes a reference to a texture into the argument buffer.
- [setTextures(_:range:)](<mtlargumentencoder/settextures(__range_).md>) — Encodes references to an array of textures into the argument buffer.

### Encoding samplers

- [- setSamplerState:atIndex:](<mtlargumentencoder/setsamplerstate(__index_).md>) — Encodes a sampler into the argument buffer.
- [setSamplerStates(_:range:)](<mtlargumentencoder/setsamplerstates(__range_).md>) — Encodes an array of samplers into the argument buffer.

### Encoding pipeline states

- [- setRenderPipelineState:atIndex:](<mtlargumentencoder/setrenderpipelinestate(__index_).md>) — Encodes a reference to a render pipeline state into the argument buffer.
- [setRenderPipelineStates(_:range:)](<mtlargumentencoder/setrenderpipelinestates(__range_).md>) — Encodes references to an array of render pipeline states into the argument buffer.
- [- setComputePipelineState:atIndex:](<mtlargumentencoder/setcomputepipelinestate(__index_).md>) — Encodes a reference to a compute pipeline state into the argument buffer.
- [setComputePipelineStates(_:with:)](<mtlargumentencoder/setcomputepipelinestates(__with_).md>) — Encodes references to an array of compute pipeline states into the argument buffer.
- [setComputePipelineState(_:at:)](<mtlargumentencoder/setcomputepipelinestate(__at_).md>) — Encodes a reference to a compute pipeline state into the argument buffer.
- [setComputePipelineStates(_:range:)](<mtlargumentencoder/setcomputepipelinestates(__range_).md>) — Encodes references to an array of compute pipeline states into the argument buffer.

### Encoding inlined constant data

- [- constantDataAtIndex:](<mtlargumentencoder/constantdata(at_).md>) — Returns a pointer to an inline, constant-data argument within the argument buffer.

### Encoding indirect command buffers

- [- setIndirectCommandBuffer:atIndex:](<mtlargumentencoder/setindirectcommandbuffer(__index_).md>) — Encodes a reference to an indirect command buffer into the argument buffer.
- [setIndirectCommandBuffers(_:range:)](<mtlargumentencoder/setindirectcommandbuffers(__range_).md>) — Encodes an array of indirect command buffers into the argument buffer.

### Encoding acceleration structures

- [- setAccelerationStructure:atIndex:](<mtlargumentencoder/setaccelerationstructure(__index_).md>) — Encodes a reference to an acceleration structure into the argument buffer.

### Encoding function tables

- [- setVisibleFunctionTable:atIndex:](<mtlargumentencoder/setvisiblefunctiontable(__index_).md>) — Encodes a reference to a visible-function table into the argument buffer.
- [- setIntersectionFunctionTable:atIndex:](<mtlargumentencoder/setintersectionfunctiontable(__index_).md>) — Encodes a reference to a ray-tracing intersection-function table into the argument buffer.
- [setIntersectionFunctionTables(_:range:)](<mtlargumentencoder/setintersectionfunctiontables(__range_).md>) — Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.
- [setVisibleFunctionTables(_:range:)](<mtlargumentencoder/setvisiblefunctiontables(__range_).md>) — Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.

### Creating a nested argument encoder

- [- newArgumentEncoderForBufferAtIndex:](<mtlargumentencoder/makeargumentencoderforbuffer(atindex_).md>) — Creates a new argument encoder for a nested argument buffer.

### Querying alignment

- [alignment](mtlargumentencoder/alignment.md) — The alignment, in bytes, required for storing the encoded resources of an argument buffer.

### Identifying the argument encoder

- [label](mtlargumentencoder/label.md) — A string that identifies the argument buffer.
- [device](mtlargumentencoder/device.md) — The device object that created the argument encoder.

### Instance Methods

- [- setDepthStencilState:atIndex:](<mtlargumentencoder/setdepthstencilstate(__index_).md>)
- [setDepthStencilStates(_:range:)](<mtlargumentencoder/setdepthstencilstates(__range_).md>)

## See Also

### Argument buffers

- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md) — Optimize your app’s performance by grouping your resources into argument buffers.
- [Managing groups of resources with argument buffers](managing-groups-of-resources-with-argument-buffers.md) — Create argument buffers to organize related resources.
- [Tracking the resource residency of argument buffers](tracking-the-resource-residency-of-argument-buffers.md) — Optimize resource performance within an argument buffer.
- [Indexing argument buffers](indexing-argument-buffers.md) — Assign resource indices within an argument buffer.
- [Rendering terrain dynamically with argument buffers](rendering-terrain-dynamically-with-argument-buffers.md) — Use argument buffers to render terrain in real time with a GPU-driven pipeline.
- [Encoding argument buffers on the GPU](encoding-argument-buffers-on-the-gpu.md) — Use a compute pass to encode an argument buffer and access its arguments in a subsequent render pass.
- [Using argument buffers with resource heaps](using-argument-buffers-with-resource-heaps.md) — Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [MTLArgumentDescriptor](mtlargumentdescriptor.md) — A representation of an argument within an argument buffer.
- [MTLAttributeStrideStatic](mtlattributestridestatic.md)
