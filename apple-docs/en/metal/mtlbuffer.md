---
title: MTLBuffer
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtlbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbuffer.json'
content_hash: 'sha256:46e4b539a40ccf42'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLBuffer

<sub>Protocol</sub>

A resource that stores data in a format defined by your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLBuffer : MTLResource
```

## Overview

An [MTLBuffer](mtlbuffer.md) instance can be used only with the [MTLDevice](mtldevice.md) that created it. Don’t implement this protocol yourself; instead, use the following [MTLDevice](mtldevice.md) methods to create `MTLBuffer` instances:

- [- newBufferWithLength:options:](<mtldevice/makebuffer(length_options_).md>) creates a `MTLBuffer` instance with a new storage allocation.
- [- newBufferWithBytes:length:options:](<mtldevice/makebuffer(bytes_length_options_).md>) creates a `MTLBuffer` instance by copying data from an existing storage allocation into a new allocation.
- [- newBufferWithBytesNoCopy:length:options:deallocator:](<mtldevice/makebuffer(bytesnocopy_length_options_deallocator_).md>) creates a `MTLBuffer` instance that reuses an existing storage allocation and does not allocate any new storage.

The Metal framework doesn’t know anything about the contents of an [MTLBuffer](mtlbuffer.md), just its size. You define the format of the data in the buffer and ensure that your app and your shaders know how to read and write the data. For example, you might create a struct in your shader that defines the data you want to store in the buffer and its memory layout.

If you create a buffer with a managed resource storage mode ([MTLStorageModeManaged](mtlstoragemode/managed.md)), you need to call [didModifyRange:](mtlbuffer/didmodifyrange_.md) to tell Metal to copy any changes to the GPU.

## Relationships

- **Inherits From**: [MTLAllocation](mtlallocation.md), [MTLResource](mtlresource.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a texture that shares buffer data

- [- newTextureWithDescriptor:offset:bytesPerRow:](<mtlbuffer/maketexture(descriptor_offset_bytesperrow_).md>) — Creates a texture that shares its storage with the buffer.

### Reading the buffer’s data on the CPU

- [- contents](<mtlbuffer/contents().md>) — Gets the system address of the buffer’s storage allocation.

### Synchronizing data to the GPU for managed buffers

- [didModifyRange(_:)](<mtlbuffer/didmodifyrange(__).md>) — Informs the GPU that the CPU has modified a section of the buffer.

### Debugging buffers

- [addDebugMarker(_:range:)](<mtlbuffer/adddebugmarker(__range_).md>) — Adds a debug marker string to a specific buffer range.
- [- removeAllDebugMarkers](<mtlbuffer/removealldebugmarkers().md>) — Removes all debug marker strings from the buffer.

### Reading buffer length

- [length](mtlbuffer/length.md) — The logical size of the buffer, in bytes.

### Creating views of buffers on other GPUs

- [- newRemoteBufferViewForDevice:](<mtlbuffer/makeremotebufferview(__).md>) — Creates a remote view of the buffer for another GPU in the same peer group. _(deprecated)_
- [remoteStorageBuffer](mtlbuffer/remotestoragebuffer.md) — The buffer on another GPU that the buffer was created from, if any. _(deprecated)_

### Instance Properties

- [gpuAddress](mtlbuffer/gpuaddress.md)
- [sparseBufferTier](mtlbuffer/sparsebuffertier.md)

### Instance Methods

- [- newTensorWithDescriptor:offset:error:](<mtlbuffer/maketensor(descriptor_offset_).md>) — Creates a single-plane tensor with the specified descriptor that shares storage with this buffer.
