---
title: Resource loading
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/resource-loading
source_url: 'https://developer.apple.com/documentation/metal/resource-loading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/resource-loading.json'
content_hash: 'sha256:45ba3bb1d8ab7df5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# Resource loading

<sub>API Collection</sub>

Load assets in your games and apps quickly by running a dedicated input/output queue alongside your GPU tasks.

## Overview

Metal 3 adds input/output command queues and buffers that make the most of a device’s storage hardware, including flash storage and the unified memory architecture of Apple silicon, when available. When you run a dedicated input/output queue alongside your GPU tasks, you can synchronize them with Metal shared events. With this approach, you can minimize load screen times by fetching the essential assets first and streaming the rest as you need them. You can also start multiple input/output command buffers to load different asset batches and later cancel the ones you don’t need. Ensure that time-sensitive assets, such as sound effects, load with lower latency by running those command buffers on higher-priority queues that you create.

First, create [MTLIOCommandQueue](mtliocommandqueue.md) instances by configuring an [MTLIOCommandQueueDescriptor](mtliocommandqueuedescriptor.md) instance and passing it to an [MTLDevice](mtldevice.md) instance’s [- newIOCommandQueueWithDescriptor:error:](<mtldevice/makeiocommandqueue(descriptor_).md>) method.

**Swift**

```swift
// Create a Metal I/O command queue.
let commandQueueDescriptor = MTLIOCommandQueueDescriptor()

commandQueueDescriptor.type = .concurrent
commandQueueDescriptor.priority = .normal

let ioCommandQueue = try device.makeIOCommandQueue(descriptor:
                                                    commandQueueDescriptor)
```

**Objective-C**

```objective-c
// Create a Metal I/O command queue.
MTLIOCommandQueueDescriptor *commandQueueDescriptor;
commandQueueDescriptor = [[MTLIOCommandQueueDescriptor alloc] init];

commandQueueDescriptor.type = MTLIOCommandQueueTypeConcurrent;
commandQueueDescriptor.priority = MTLIOPriorityNormal;

NSError *error = nil;
id<MTLIOCommandQueue> ioCommandQueue;
ioCommandQueue = [device newIOCommandQueueWithDescriptor:commandQueueDescriptor
                                                   error:&error];

if (error != nil) {
        // Report the error.
        ...
}
```

For each queue, create one or more [MTLIOCommandBuffer](mtliocommandbuffer.md) instances by calling the queue’s [- commandBuffer](<mtliocommandqueue/makecommandbuffer().md>) or [- commandBufferWithUnretainedReferences](<mtliocommandqueue/makecommandbufferwithunretainedreferences().md>) method. For each command buffer, load the assets you want by calling any of the [MTLIOCommandBuffer](mtliocommandbuffer.md) protocol’s load methods. For example:

- The [- loadBuffer:offset:size:sourceHandle:sourceHandleOffset:](<mtliocommandbuffer/load(__offset_size_sourcehandle_sourcehandleoffset_).md>) method loads an asset into an [MTLBuffer](mtlbuffer.md).
- The [- loadTexture:slice:level:size:sourceBytesPerRow:sourceBytesPerImage:destinationOrigin:sourceHandle:sourceHandleOffset:](<mtliocommandbuffer/load(__slice_level_size_sourcebytesperrow_sourcebytesperimage_destinationorigin_sourcehandle_sourcehandleoffset_).md>) method loads an asset into an [MTLTexture](mtltexture.md).
- The [- loadBytes:size:sourceHandle:sourceHandleOffset:](<mtliocommandbuffer/loadbytes(__size_sourcehandle_sourcehandleoffset_).md>) method loads an asset, such as an audio file, into a CPU-accessible memory buffer.

**Swift**

```swift
// Create a Metal I/O command buffer.
let ioCommandBuffer = ioCommandQueue.makeCommandBuffer()

// Encode a command that loads a texture.
ioCommandBuffer.load(texture,
                     slice: 0,
                     level: 0,
                     size: textureSize,
                     sourceBytesPerRow: bytesPerRow,
                     sourceBytesPerImage: bytesPerImage,
                     destinationOrigin: origin,
                     sourceHandle: fileHandle,
                     sourceHandleOffset: 0)

// Encode a command that loads a buffer.
ioCommandBuffer.load(buffer,
                     offset: 0,
                     size: bufferSize,
                     sourceHandle: fileHandle,
                     sourceHandleOffset: 0)

// Submit the command buffer to run.
ioCommandBuffer.commit()
```

**Objective-C**

```objective-c
// Create a Metal I/O command buffer.
id<MTLIOCommandBuffer> ioCommandBuffer = [ioCommandQueue commandBuffer];

// Encode a command that loads a texture.
[ioCommandBuffer loadTexture:texture
                       slice:0
                       level:0
                        size:textureSize
           sourceBytesPerRow:bytesPerRow
         sourceBytesPerImage:bytesPerImage
           destinationOrigin:origin
                sourceHandle:textureAssetHandle
          sourceHandleOffset:0];

// Encode a command that loads a buffer.
[ioCommandBuffer loadBuffer:buffer
                     offset:0
                       size:bufferSize
               sourceHandle:bufferAssetHandle
         sourceHandleOffset:0];

// Submit the command buffer to run.
[ioCommandBuffer commit];
```

For each asset, create an [MTLIOFileHandle](mtliofilehandle.md) instance using the input/output command buffer’s load methods. To create a file handle for your asset, call an [MTLDevice](mtldevice.md) instance’s [- newIOHandleWithURL:error:](<mtldevice/makeiohandle(url_).md>) or [- newIOHandleWithURL:compressionMethod:error:](<mtldevice/makeiohandle(url_compressionmethod_).md>) method.

**Swift**

```swift
func createHandleForFile(at url: URL, with device: MTLDevice) -> MTLIOFileHandle? {
    return try? device.makeIOHandle(url: url)
}
```

**Objective-C**

```objective-c
id<MTLIOFileHandle> createHandleForFile(NSURL *url, id<MTLDevice> device)
{
    NSError *error = nil;
    id<MTLIOFileHandle> assetHandle = [device newIOHandleWithURL:url error:&error];

    if (error != nil) {
        // Report the error.
        ...
    }

    return assetHandle;
}
```

> [!note] Note
> You need to create each file handle using the same [MTLDevice](mtldevice.md) instance that created the [MTLIOCommandQueue](mtliocommandqueue.md) and [MTLIOCommandBuffer](mtliocommandbuffer.md) instances that load the files.

To help minimize your appʼs storage footprint, compress your assets at development time. First, create a new compression context with the [MTLIOCreateCompressionContext](mtliocreatecompressioncontext.md) function. Then, add data for an asset to the compression context using the [MTLIOCompressionContextAppendData](<mtliocompressioncontextappenddata(______).md>) function. Finally, call the  [MTLIOFlushAndDestroyCompressionContext](<mtlioflushanddestroycompressioncontext(__).md>) function to save the context to a compressed file that you add to your project.

## Topics

### I/O command queues

- [MTLIOCommandQueue](mtliocommandqueue.md) — A command queue that schedules input/output commands for reading files in the file system, and writing to GPU resources and memory.
- [MTLIOCommandQueueDescriptor](mtliocommandqueuedescriptor.md) — A configuration template you use to create a new input/output command queue.
- [MTLIOPriority](mtliopriority.md) — Designates the priority for a new input/output command queue.
- [MTLIOCommandQueueType](mtliocommandqueuetype.md) — Designates the queue type for a new input/output command queue.
- [MTLIOScratchBufferAllocator](mtlioscratchbufferallocator.md) — A protocol your app implements to provide scratch memory to an input/output command queue.
- [MTLIOScratchBuffer](mtlioscratchbuffer.md) — A protocol your app implements that wraps a Metal buffer instance to serve as scratch memory for an input/output command queue.

### I/O command buffers

- [MTLIOCommandBuffer](mtliocommandbuffer.md) — A command buffer that contains input/output commands that work with files in the file systems and Metal resources.
- [MTLIOFileHandle](mtliofilehandle.md) — Represents a raw or compressed file, such as a resource asset file in your app’s bundle.
- [MTLIOCommandBufferHandler](mtliocommandbufferhandler.md) — A convenience type that defines the signature of an input/output command buffer’s completion handler.
- [MTLIOStatus](mtliostatus.md) — Represents the state of an input/output command buffer.
- [Code](mtlioerror-swift.struct/code.md) — The error codes for creating an input/output file handle.
- [MTLIOErrorDomain](mtlioerrordomain.md) — The domain for input/output command queue errors.

### Asset compression

- [MTLIOCreateCompressionContext(_:_:_:)](<mtliocreatecompressioncontext(______).md>) — Creates a compression context that you use to compress data into a single file.
- [MTLIOCompressionMethod](mtliocompressionmethod.md) — The compression codecs that Metal supports for input/output handles.
- [MTLIOCompressionContextDefaultChunkSize](<mtliocompressioncontextdefaultchunksize().md>) — Returns a compression chunk size you can use as a default for creating a compression context.
- [MTLIOCompressionContext](mtliocompressioncontext.md) — A pointer that represents the state of a file compression session in progress.
- [MTLIOCompressionContextAppendData](<mtliocompressioncontextappenddata(______).md>) — Adds data to a compression context.
- [MTLIOFlushAndDestroyCompressionContext](<mtlioflushanddestroycompressioncontext(__).md>) — Finishes compressing and saves the file that a compression context represents.
- [MTLIOCompressionStatus](mtliocompressionstatus.md) — Represents the final state of a compression context.

## See Also

### Resources

- [Resource fundamentals](resource-fundamentals.md) — Control the common attributes of all Metal memory resources, including buffers and textures, and how to configure their underlying memory.
- [Buffers](buffers.md) — Create and manage untyped data your app uses to exchange information with its shader functions.
- [Textures](textures.md) — Create and manage typed data your app uses to exchange information with its shader functions.
- [Memory heaps](memory-heaps.md) — Take control of your app’s GPU memory management by creating a large memory allocation for various buffers, textures, and other resources.
- [Resource synchronization](resource-synchronization.md) — Prevent multiple commands that can access the same resources simultaneously by coordinating those reads and writes with barriers, fences, or events.
