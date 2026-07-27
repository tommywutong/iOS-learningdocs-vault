---
title: 优化纹理数据
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/optimizing-texture-data
source_url: 'https://developer.apple.com/documentation/metal/optimizing-texture-data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/optimizing-texture-data.json'
content_hash: 'sha256:151ac767b671d562'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [Textures](textures.md)

# 优化纹理数据

<sub>文章</sub>

优化纹理的数据以提升 GPU 或 CPU 的访问效率。

## 概述

默认情况下，Metal 会根据纹理的存储模式和使用选项，尝试针对 GPU 和 CPU 的内存操作对该纹理的数据进行优化。你可以针对某一种使用场景优化纹理数据，从而提升该纹理在 GPU 或 CPU 上的性能。你也可以完全选择不进行优化。为某一种用途优化纹理性能，可能会降低该纹理在另一种用途下的性能。

在优化纹理数据之前，请仔细考虑你纹理的存储模式和使用选项。有关资源存储模式的指导，请参阅[设置资源存储模式](setting-resource-storage-modes.md)。有关纹理使用选项的指导，请参阅 [MTLTextureUsage](mtltextureusage.md)。

> [!note] 注意
> 对于某些硬件，Metal 可能无法优化其中的某些纹理，并会忽略针对这些纹理的优化 API 调用。

### 为 GPU 访问优化纹理数据

默认情况下，如果满足以下任一条件，Metal 会尝试为 GPU 访问优化纹理数据：

- 你使用 [MTLStorageModePrivate](mtlstoragemode/private.md) 模式创建该纹理。
- 你使用 [MTLTextureUsageRenderTarget](mtltextureusage/rendertarget.md) 选项创建该纹理。

如果该纹理不满足以上任何条件，你可以显式地优化纹理数据。在创建纹理并填充其内容后，编码并提交一条 [- optimizeContentsForGPUAccess:](<mtlblitcommandencoder/optimizecontentsforgpuaccess(texture_).md>) 或 [- optimizeContentsForGPUAccess:slice:level:](<mtlblitcommandencoder/optimizecontentsforgpuaccess(texture_slice_level_).md>) 命令。

**Swift**

```swift
// Create the first texture.
let texture1GPUOptimized: MTLTexture! = nil
...

// Put content in the texture.
...

// Create a command buffer to submit work to the GPU.
let commandBuffer: MTLCommandBuffer! = commandQueue.makeCommandBuffer()

// Optimize the texture for GPU access by encoding a blit command.
let blitEncoder: MTLBlitCommandEncoder! = commandBuffer.makeBlitCommandEncoder()
blitEncoder.optimizeContentsForGPUAccess(texture: texture1GPUOptimized)

// End the encoding.
blitEncoder.endEncoding()

// Add a completion handler.
commandBuffer.addCompletedHandler {_ in
    // The GPU can now optimally access the contents of texture 1.
    ...
}

// Commit the command buffer to the command queue.
commandBuffer.commit()
```

**Objective-C**

```objective-c
// Create the first texture.
id <MTLTexture> texture1GPUOptimized;
...

// Put content in the texture.
...

// Create a command buffer to submit work to the GPU.
id <MTLCommandBuffer> commandBuffer = [commandQueue commandBuffer];

// Optimize the texture for GPU access by encoding a blit command.
id <MTLBlitCommandEncoder> blitEncoder = [commandBuffer blitCommandEncoder];
[blitEncoder optimizeContentsForGPUAccess:texture1GPUOptimized];

// End the encoding.
[blitEncoder endEncoding];

// Add a completion handler.
[commandBuffer addCompletedHandler:^(id<MTLCommandBuffer> commandBuffer) {
    // The GPU can now optimally access the contents of texture 1.
    ...
}];

// Commit the command buffer to the command queue.
[commandBuffer commit];
```

要为 GPU 访问优化来自 [MTKView](../metalkit/mtkview.md) 的可绘制对象，请将该视图的 [framebufferOnly](../metalkit/mtkview/framebufferonly.md) 属性设置为 [true](../swift/true.md)。此属性会将该纹理专门配置为渲染目标和可显示资源。

### 为 CPU 访问优化纹理数据

默认情况下，如果同时满足以下两个条件，Metal 会尝试为 CPU 访问优化纹理数据：

- 你使用 [MTLStorageModeShared](mtlstoragemode/shared.md) 或 [MTLStorageModeManaged](mtlstoragemode/managed.md) 模式创建该纹理。
- 你使用 [- replaceRegion:mipmapLevel:withBytes:bytesPerRow:](<mtltexture/replace(region_mipmaplevel_withbytes_bytesperrow_).md>) 或 [- replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:](<mtltexture/replace(region_mipmaplevel_slice_withbytes_bytesperrow_bytesperimage_).md>) 方法向该纹理写入数据。

如果这两个条件你都不满足，你可以显式地优化纹理数据。在创建纹理并填充其内容后，编码并提交一条 [- optimizeContentsForCPUAccess:](<mtlblitcommandencoder/optimizecontentsforcpuaccess(texture_).md>) 或 [- optimizeContentsForCPUAccess:slice:level:](<mtlblitcommandencoder/optimizecontentsforcpuaccess(texture_slice_level_).md>) 命令。

**Swift**

```swift
// Create a second texture.
let texture2CPUOptimized: MTLTexture! = nil
...

// Put content in the texture.
...

// Create a command buffer to submit work to the GPU.
let commandBuffer: MTLCommandBuffer! = commandQueue.makeCommandBuffer()

// Optimize the texture for CPU access by encoding a blit command.
let blitEncoder: MTLBlitCommandEncoder! = commandBuffer.makeBlitCommandEncoder()
blitEncoder.optimizeContentsForCPUAccess(texture: texture2CPUOptimized)

// End encoding and commit it to the command buffer with add a completion handler.
blitEncoder.endEncoding()
commandBuffer.addCompletedHandler {_ in
    // The CPU can now optimally access the contents of texture 2.
    ...
}

// Commit the command buffer to the command queue.
commandBuffer.commit()
```

**Objective-C**

```objective-c
// Create a second texture.
id <MTLTexture> texture2CPUOptimized;
...

// Put content in the texture.
...

// Create a command buffer to submit work to the GPU.
id <MTLCommandBuffer> commandBuffer = [commandQueue commandBuffer];

// Optimize the texture for CPU access by encoding a blit command.
id <MTLBlitCommandEncoder> blitEncoder = [commandBuffer blitCommandEncoder];
[blitEncoder optimizeContentsForCPUAccess:texture2CPUOptimized];

// End encoding and commit it to the command buffer with add a completion handler.
[blitEncoder endEncoding];
[commandBuffer addCompletedHandler:^(id<MTLCommandBuffer> commandBuffer) {
    // The CPU can now optimally access the contents of texture 2.
    ...
}];

// Commit the command buffer to the command queue.
[commandBuffer commit];
```

### 在 Apple GPU 上对纹理应用无损压缩

无损压缩是 Metal 对纹理施加的一种特定形式的 GPU 优化，不会丢弃该纹理的任何数据。对采用无损压缩的纹理执行内存操作时，所需的显存带宽通常低于对同一纹理不做压缩时执行等效内存操作所需的带宽。不过，采用无损压缩的纹理的总体内存占用空间可能会略有增加，因为它需要存储压缩元数据。在支持 [MTLGPUFamilyApple5](mtlgpufamily/apple5.md) 的设备上，如果满足以下条件，Metal 会尝试对纹理应用无损压缩：

- 该纹理的像素格式不采用块压缩，例如 PVRTC、ASTC 或 BC。
- 该纹理的使用选项不包含 [MTLTextureUsageUnknown](mtltextureusage/unknown.md)、[MTLTextureUsageShaderWrite](mtltextureusage/shaderwrite.md) 或 [MTLTextureUsagePixelFormatView](mtltextureusage/pixelformatview.md)。
- 该纹理不使用任何底层的 [MTLBuffer](mtlbuffer.md) 实例，例如通过某个缓冲区的 [- newTextureWithDescriptor:offset:bytesPerRow:](<mtlbuffer/maketexture(descriptor_offset_bytesperrow_).md>) 方法得到的纹理。

此外，如果你同时满足以下两个条件，也可以显式地优化纹理数据，让 Metal 能够应用无损压缩：

- 你使用 [MTLStorageModeShared](mtlstoragemode/shared.md) 模式创建该纹理。
- 你使用 [- replaceRegion:mipmapLevel:withBytes:bytesPerRow:](<mtltexture/replace(region_mipmaplevel_withbytes_bytesperrow_).md>) 或 [- replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:](<mtltexture/replace(region_mipmaplevel_slice_withbytes_bytesperrow_bytesperimage_).md>) 方法向该纹理写入数据。

有关指导，请参阅[为 GPU 访问优化纹理数据](optimizing-texture-data.md#Optimize-texture-data-for-GPU-access)。

### 为 GPU 访问退出纹理数据优化

在某些情况下，为 GPU 访问退出优化可能对你的纹理数据更有利，例如当优化导致你 App 的性能出现衰退时（尤其是在 CPU 上对渲染目标进行读回操作时）。

首先，创建一个纹理描述符，并将其 [allowGPUOptimizedContents](mtltexturedescriptor/allowgpuoptimizedcontents.md) 属性设置为 [false](../swift/false.md)。

**Swift**

```swift
let textureDescriptor = MTLTextureDescriptor.texture2DDescriptor(pixelFormat: .rgba8Unorm,
                                                                 width: 512,
                                                                 height: 512,
                                                                 mipmapped: false)

// Don't allow the the GPU to optimize the texture.
textureDescriptor.allowGPUOptimizedContents = false
```

**Objective-C**

```objective-c
MTLTextureDescriptor *textureDescriptor =
 [MTLTextureDescriptor texture2DDescriptorWithPixelFormat:MTLPixelFormatRGBA8Unorm
                                                    width:512
                                                   height:512
                                                mipmapped:NO];

// Don't allow the the GPU to optimize the texture.
textureDescriptor.allowGPUOptimizedContents = NO;
```

然后，将纹理描述符的 [storageMode](mtltexturedescriptor/storagemode.md) 属性设置为 [MTLStorageModeShared](mtlstoragemode/shared.md) 或 [MTLStorageModeManaged](mtlstoragemode/managed.md)。

**Swift**

```swift
// Set the texture descriptor's storage mode to `shared` or `managed` based on the GPU family.
if device.supportsFamily(.apple1) {
    textureDescriptor.storageMode = .shared
} else {
    textureDescriptor.storageMode = .managed
}
```

**Objective-C**

```objective-c
// Set the texture descriptor's storage mode to `shared` or `managed` based on the GPU family.

if ([device supportsFamily:MTLGPUFamilyApple1]) {
    textureDescriptor.storageMode = MTLStorageModeShared;
} else {
    textureDescriptor.storageMode = MTLStorageModeManaged;
}
```

最后，根据该纹理描述符创建一个纹理。

**Swift**

```swift
// Create a texture using the texture descriptor.
let texture = device.makeTexture(descriptor: textureDescriptor)
```

**Objective-C**

```objective-c
// Create a texture using the texture descriptor.
id <MTLTexture> texture = [device newTextureWithDescriptor:textureDescriptor];
```

## 另请参阅

### 纹理基础

- [了解可用作颜色渲染目标的像素格式尺寸](understanding-color-renderable-pixel-format-sizes.md) — 根据渲染目标的像素格式，了解 Apple GPU 中颜色渲染目标的尺寸限制。
- [MTLTexture](mtltexture.md) — 一种保存已格式化图像数据的资源。
- [MTLTextureCompressionType](mtltexturecompressiontype.md)
- [MTLTextureDescriptor](mtltexturedescriptor.md) — 用于配置新的 Metal 纹理实例的实例。
- [MTKTextureLoader](../metalkit/mtktextureloader.md) — 一种从常见图像格式的现有数据创建纹理的对象。
- [MTLSharedTextureHandle](mtlsharedtexturehandle.md) — 一种可以跨进程地址空间边界共享的纹理句柄。
- [MTLPixelFormat](mtlpixelformat.md) — 描述纹理中各个像素组织方式与特征的数据格式。
