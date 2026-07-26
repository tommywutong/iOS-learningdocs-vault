---
title: Setting resource storage modes
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/setting-resource-storage-modes
source_url: 'https://developer.apple.com/documentation/metal/setting-resource-storage-modes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/setting-resource-storage-modes.json'
content_hash: 'sha256:804f8f6ba1eb926b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Resource fundamentals](resource-fundamentals.md)

# Setting resource storage modes

<sub>Article</sub>

Set a storage mode that defines the memory location and access permissions of a resource.

## Overview

Storage modes are only set when creating an instance, and the system default allows for access to memory from both the CPU and GPU. Metal selects the default mode for resources depending on hardware.

- For Apple silicon GPUs the default is [MTLStorageModeShared](mtlstoragemode/shared.md).
- For Intel-based Mac computers, the default is [MTLStorageModeManaged](mtlstoragemode/managed.md) for all [MTLTexture](mtltexture.md) instances and [MTLBuffer](mtlbuffer.md) instances attached to discrete GPUs. [MTLBuffer](mtlbuffer.md) instances using the integrated GPU have [MTLStorageModeShared](mtlstoragemode/shared.md) as their default.

> [!important] Important
> Use the system default if your data is available to both the CPU and GPU. When you manually select shared or managed mode, your app may not run on some hardware.

You perform the same synchronization tasks to ensure GPU and CPU memory coherency in both default modes. To check for GPU architecture and capabilities, use the [- supportsFamily:](<mtldevice/supportsfamily(__).md>) method instead of the [storageMode](mtlresource/storagemode.md) property. See [Detecting GPU features and Metal software versions](detecting-gpu-features-and-metal-software-versions.md) for more information.

Use [MTLStorageModeMemoryless](mtlstoragemode/memoryless.md), only available on Apple silicon, when you manage your own storage, or want to run a GPU task that requires temporary resources. For tasks that share memory on the GPU, use [MTLStorageModePrivate](mtlstoragemode/private.md) storage. This article includes examples of how to set the storage mode for a buffer or texture.

For more guidance on which mode to choose, see [Choosing a resource storage mode for Apple GPUs](choosing-a-resource-storage-mode-for-apple-gpus.md) and [Choosing a resource storage mode for Intel and AMD GPUs](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md).

### Set a storage mode for a buffer

Create a new [MTLBuffer](mtlbuffer.md) with the [- newBufferWithLength:options:](<mtldevice/makebuffer(length_options_).md>) method and set its storage mode in the method’s `options` parameter.

**Swift**

```swift
let bufferOptions = MTLResourceOptions.storageModePrivate
let buffer = device.makeBuffer(length: 256,
                               options: bufferOptions)
```

**Objective-C**

```objective-c
MTLResourceOptions bufferOptions = MTLResourceStorageModePrivate;
id <MTLBuffer> buffer = [_device newBufferWithLength:256
                                             options:bufferOptions];
```

> [!note] Note
> The storage mode options in [MTLResourceOptions](mtlresourceoptions.md) are equivalent to the storage mode values in [MTLStorageMode](mtlstoragemode.md). When you create a new buffer, you can combine multiple resource options but you can set only one storage mode.

### Set a storage mode for a texture

Create a new [MTLTextureDescriptor](mtltexturedescriptor.md) and set its storage mode in the descriptor’s [storageMode](mtlresource/storagemode.md) property. Then create a new [MTLTexture](mtltexture.md) with the [- newTextureWithDescriptor:](<mtldevice/maketexture(descriptor_).md>) method.

**Swift**

```swift
let textureDescriptor = MTLTextureDescriptor.texture2DDescriptor(pixelFormat: .bgra8Unorm,
                                                                 width: 256,
                                                                 height: 256,
                                                                 mipmapped: true)
textureDescriptor.storageMode = .private
let texture = device.makeTexture(descriptor: textureDescriptor)
```

**Objective-C**

```objective-c
MTLTextureDescriptor *textureDescriptor = [MTLTextureDescriptor texture2DDescriptorWithPixelFormat:MTLPixelFormatBGRA8Unorm
                                                                                             width:256
                                                                                            height:256
                                                                                         mipmapped:YES];
textureDescriptor.storageMode = MTLStorageModePrivate;
id <MTLTexture> texture = [_device newTextureWithDescriptor:textureDescriptor];
```

## See Also

### Resource management

- [Choosing a resource storage mode for Apple GPUs](choosing-a-resource-storage-mode-for-apple-gpus.md) — Select an appropriate storage mode for your textures and buffers on Apple GPUs.
- [Choosing a resource storage mode for Intel and AMD GPUs](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md) — Select an appropriate storage mode for your textures and buffers on AMD and Intel GPUs.
- [Copying data to a private resource](copying-data-to-a-private-resource.md) — Use a blit command encoder to copy buffer or texture data to a private resource.
- [Synchronizing a managed resource in macOS](synchronizing-a-managed-resource-in-macos.md) — Manually synchronize memory for a Metal resource in apps.
- [Transferring data between connected GPUs](transferring-data-between-connected-gpus.md) — Use high-speed connections between GPUs to transfer data quickly.
- [Reducing the memory footprint of Metal apps](reducing-the-memory-footprint-of-metal-apps.md) — Learn best practices for using memory efficiently in iOS and tvOS.
