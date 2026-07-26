---
title: MTLIOCommandBuffer
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocommandbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandbuffer.json'
content_hash: 'sha256:afaacc80ee2278f0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOCommandBuffer

<sub>Protocol</sub>

A command buffer that contains input/output commands that work with files in the file systems and Metal resources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLIOCommandBuffer : NSObjectProtocol
```

## Overview

Add commands an input/output command buffer to load assets from the file system directly into Metal resources. Your app can then use those resources with other commands it submits to [MTLCommandQueue](mtlcommandqueue.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Loading assets

- [- loadBuffer:offset:size:sourceHandle:sourceHandleOffset:](<mtliocommandbuffer/load(__offset_size_sourcehandle_sourcehandleoffset_).md>) — Encodes a command that loads data from a file handle into a GPU buffer.
- [- loadTexture:slice:level:size:sourceBytesPerRow:sourceBytesPerImage:destinationOrigin:sourceHandle:sourceHandleOffset:](<mtliocommandbuffer/load(__slice_level_size_sourcebytesperrow_sourcebytesperimage_destinationorigin_sourcehandle_sourcehandleoffset_).md>) — Encodes a command that loads data from a file handle into a GPU texture.
- [- loadBytes:size:sourceHandle:sourceHandleOffset:](<mtliocommandbuffer/loadbytes(__size_sourcehandle_sourcehandleoffset_).md>) — Encodes a command that loads data from a file handle into CPU-accessible memory buffer.

### Adding a barrier

- [- addBarrier](<mtliocommandbuffer/addbarrier().md>) — Encodes a barrier into the command buffer.

### Synchronizing a command buffer

- [- signalEvent:value:](<mtliocommandbuffer/signalevent(__value_).md>) — Encodes a command that signals a shared event to other parts of your app.
- [- waitForEvent:value:](<mtliocommandbuffer/waitforevent(__value_).md>) — Encodes a command that pauses the command buffer’s execution until another part of your app signals a shared event.

### Adding final commands

- [- copyStatusToBuffer:offset:](<mtliocommandbuffer/copystatus(buffer_offset_).md>) — Encodes a command that writes the input/output command buffer’s status to a buffer.
- [- addCompletedHandler:](<mtliocommandbuffer/addcompletedhandler(__).md>) — Adds a closure that Metal calls immediately after the GPU finishes executing the commands in the input/output command buffer.

### Submitting a command buffer

- [- commit](<mtliocommandbuffer/commit().md>) — Submits the command buffer to the queue for execution on the GPU.
- [- enqueue](<mtliocommandbuffer/enqueue().md>) — Reserves a place for the input/output command buffer in the input/output command queue without committing the command buffer.

### Canceling a command buffer

- [- tryCancel](<mtliocommandbuffer/trycancel().md>) — Submits a request to abandon a command buffer the queue is currently running.

### Waiting for a command buffer

- [- waitUntilCompleted](<mtliocommandbuffer/waituntilcompleted().md>) — Blocks the current thread until the GPU finishes executing the input/output command buffer and all of its completion handlers.

### Checking the state of a command buffer

- [status](mtliocommandbuffer/status.md) — Represents the state of the input/output command buffer.
- [error](mtliocommandbuffer/error.md) — Stores the details of an error when the GPU experienced a problem with the input/output command buffer.

### Debugging a command buffer

- [label](mtliocommandbuffer/label.md) — An optional name for the input/output command buffer.
- [- pushDebugGroup:](<mtliocommandbuffer/pushdebuggroup(__).md>) — Sets the current name for this input/output command encoder by adding it to the top of the debug name stack.
- [- popDebugGroup](<mtliocommandbuffer/popdebuggroup().md>) — Restores the previous name for this input/output command encoder by removing the top item of the debug name stack.

## See Also

### I/O command buffers

- [MTLIOFileHandle](mtliofilehandle.md) — Represents a raw or compressed file, such as a resource asset file in your app’s bundle.
- [MTLIOCommandBufferHandler](mtliocommandbufferhandler.md) — A convenience type that defines the signature of an input/output command buffer’s completion handler.
- [MTLIOStatus](mtliostatus.md) — Represents the state of an input/output command buffer.
- [Code](mtlioerror-swift.struct/code.md) — The error codes for creating an input/output file handle.
- [MTLIOErrorDomain](mtlioerrordomain.md) — The domain for input/output command queue errors.
