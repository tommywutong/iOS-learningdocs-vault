---
title: 在 macOS 中同步受管理资源
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/synchronizing-a-managed-resource-in-macos
source_url: 'https://developer.apple.com/documentation/metal/synchronizing-a-managed-resource-in-macos'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/synchronizing-a-managed-resource-in-macos.json'
content_hash: 'sha256:3e26f03956602f39'
translated: true
---

> 导航：[技术](../technologies.md) · [Metal](../metal.md) · [资源基础](resource-fundamentals.md)

# 在 macOS 中同步受管理资源

<sub>文章</sub>

在 App 中手动同步 Metal 资源的内存。

## 概述

对于采用 Intel 或外部 GPU 的 Mac 电脑，Metal 提供_受管理资源_。受管理资源是 [MTLResource](mtlresource.md) 实例，例如 [MTLTexture](mtltexture.md) 或 [MTLBuffer](mtlbuffer.md)，它们使用的内存可以在 CPU 和 GPU 之间进行复制。受管理资源使用的 [storageMode](mtlresource/storagemode.md) 为 [MTLStorageModeManaged](mtlstoragemode/managed.md)。

你需要手动同步受管理资源，在 CPU 和 GPU 之间复制已更改的内存。这与 Apple 系列 GPU 不同，后者对于 CPU 和 GPU 都可以访问的资源使用 [MTLStorageModeShared](mtlstoragemode/shared.md)。在你的代码完成内存写入后进行同步。数据同步后，你就可以在你的 App 和 GPU 函数中安全地读取它。

作为最佳实践，请尽量减少数据同步点的数量。即使是不复制数据的同步调用，也可能导致轻微的性能损失。

> [!note] 注意
> 受管理资源是 Metal 中 Intel 和外部 GPU 设备的默认内存存储类型。有关 macOS 资源存储模式及其选择方法的更多信息，请参阅[为 Intel 和 AMD GPU 选择资源存储模式](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md)。

### 同步受管理缓冲区

首先，使用选项 [MTLStorageModeManaged](mtlstoragemode/managed.md) 创建一个 [MTLBuffer](mtlbuffer.md)，这会告诉 Metal 为该资源保留受管理内存空间：

**Swift**

```swift
// 创建一个矩阵数据结构。
struct MatrixData {
    var modelMatrix = matrix_float4x4()
    var viewMatrix = matrix_float4x4()
    var projectionMatrix = matrix_float4x4()
}

// 创建一个受管理缓冲区。
guard let matrixBuffer = device.makeBuffer(length: MemoryLayout<MatrixData>.size, options: .storageModeManaged) else { return }
```

**Objective-C**

```objective-c
// 创建一个矩阵数据结构。
id <MTLBuffer> _matrixBuffer;
typedef struct
{
    matrix_float4x4 modelMatrix;
    matrix_float4x4 viewMatrix;
    matrix_float4x4 projectionMatrix;
} MatrixData;

// 创建一个受管理缓冲区。
_matrixBuffer = [_device newBufferWithLength:sizeof(MatrixData)
                                     options:MTLResourceStorageModeManaged];
```

接下来，在 CPU 上修改缓冲区数据：

**Swift**

```swift
// 使用 CPU 修改受管理缓冲区的数据。
var matrixData = MatrixData()
matrixData.modelMatrix = updatedModelMatrix
matrixBuffer.contents().storeBytes(of: matrixData, as: MatrixData.self)
```

**Objective-C**

```objective-c
// 使用 CPU 修改受管理缓冲区的数据。
MatrixData *matrixData = (MatrixData*)_matrixBuffer.contents;
matrixData->modelMatrix = updatedModelMatrix;
```

完成 CPU 修改后，调用 [didModifyRange:](mtlbuffer/didmodifyrange_.md) 方法。此方法更新指定的数据范围并保持缓冲区同步。在调用此方法之前，GPU 上修改后的缓冲区数据处于未定义状态。

**Swift**

```swift
// 同步受管理缓冲区。
matrixBuffer.didModifyRange(0..<MemoryLayout<matrix_float4x4>.size)
```

**Objective-C**

```objective-c
// 同步受管理缓冲区。
[_matrixBuffer didModifyRange:NSMakeRange(0, sizeof(matrixData->modelMatrix))];
```

在编码 GPU 修改之后，编码一条 [- synchronizeResource:](<mtlblitcommandencoder/synchronize(resource_).md>) 命令。此命令更新整个缓冲区并保持同步。在执行此命令之前，CPU 上修改后的缓冲区数据处于未定义状态。

**Swift**

```swift
// 为 GPU 工作创建命令缓冲区。
if let commandBuffer = commandQueue.makeCommandBuffer() {
    // 创建一个计算命令编码器。
    guard let computeCommandEncoder =
            commandBuffer.makeComputeCommandEncoder(dispatchType: MTLDispatchType.serial)
    else { return }
    
    // 编码一个计算 pass，使用 GPU 修改受管理缓冲区的数据。
    computeCommandEncoder.setComputePipelineState(computePipelineStateObject)
    computeCommandEncoder.setBuffer(matrixBuffer, offset: 0, index: 0)
    computeCommandEncoder.dispatchThreads(gridSize, threadsPerThreadgroup: threadgroupSize)
    computeCommandEncoder.endEncoding()
    
    // 添加一个完成处理程序并提交命令缓冲区。
    let commandBufferHandler: MTLCommandBufferHandler
    commandBuffer.addCompletedHandler(commandBufferHandler)
    commandBuffer.commit()
}
```

**Objective-C**

```objective-c
// 为 GPU 工作创建命令缓冲区。
id <MTLCommandBuffer> commandBuffer = [_commandQueue commandBuffer];

// 编码一个计算 pass，使用 GPU 修改受管理缓冲区的数据。
id <MTLComputeCommandEncoder> computeCommandEncoder = [commandBuffer computeCommandEncoderWithDispatchType:MTLDispatchTypeSerial];
[computeCommandEncoder setComputePipelineState:computePipelineStateObject];
[computeCommandEncoder setBuffer:_matrixBuffer
                          offset:0
                         atIndex:0];
[computeCommandEncoder dispatchThreads:gridSize
                 threadsPerThreadgroup:threadgroupSize];
[computeCommandEncoder endEncoding];

// 同步受管理缓冲区。
id <MTLBlitCommandEncoder> blitCommandEncoder = [commandBuffer blitCommandEncoder];
[blitCommandEncoder synchronizeResource:_matrixBuffer];
[blitCommandEncoder endEncoding];

// 添加一个完成处理程序并提交命令缓冲区。
[commandBuffer addCompletedHandler:^(id<MTLCommandBuffer> cb) {
    // 在此代码块中，命令缓冲区 `cb` 已更新并同步，可以安全地读取或写入。
}];
[commandBuffer commit];
```

### 同步受管理纹理

首先，根据 [MTLTextureDescriptor](mtltexturedescriptor.md)（其存储模式设置为 [MTLStorageModeManaged](mtlstoragemode/managed.md)）在受管理内存中创建一个 [MTLTexture](mtltexture.md)：

**Swift**

```swift
// 创建一个纹理描述符。
let textureDescriptor = MTLTextureDescriptor.texture2DDescriptor(pixelFormat: .rgba8Unorm,
                                                                 width: textureSize.width,
                                                                 height: textureSize.height,
                                                                 mipmapped: false)

// 设置描述符的存储模式和用途。
textureDescriptor.storageMode = MTLStorageMode.managed
textureDescriptor.usage = [.shaderRead, .shaderWrite]

// 创建一个受管理纹理。
let imageTexture = device.makeTexture(descriptor: textureDescriptor)
```

**Objective-C**

```objective-c
id <MTLTexture> _imageTexture;
// 创建一个纹理描述符。
MTLTextureDescriptor *textureDescriptor = [MTLTextureDescriptor texture2DDescriptorWithPixelFormat:MTLPixelFormatRGBA8Unorm
                                                                                             width:textureSize.width
                                                                                            height:textureSize.height
                                                                                         mipmapped:NO];

// 设置描述符的存储模式和用途。
textureDescriptor.storageMode = MTLStorageModeManaged;
textureDescriptor.usage = MTLTextureUsageShaderRead | MTLTextureUsageShaderWrite;

// 创建一个受管理纹理。
_imageTexture = [_device newTextureWithDescriptor:textureDescriptor];
```

要执行 CPU 修改并同时通知 Metal 此更改，请调用 [- replaceRegion:mipmapLevel:withBytes:bytesPerRow:](<mtltexture/replace(region_mipmaplevel_withbytes_bytesperrow_).md>) 方法。此方法更新指定的数据区域并保持纹理同步。要更新特定的纹理切片，请改用 [- replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:](<mtltexture/replace(region_mipmaplevel_slice_withbytes_bytesperrow_bytesperimage_).md>) 方法。在调用这些方法之一之前，GPU 上修改后的纹理数据处于未定义状态。

**Swift**

```swift
// 同时使用 CPU 修改并同步受管理纹理的数据。
let region = MTLRegionMake2D(textureOrigin.x, textureOrigin.y, textureSize.width, textureSize.height)
let bytesPerRow = pixelSize * textureSize.width
imageTexture.replace(region: region, mipmapLevel: 0, withBytes: textureData, bytesPerRow: bytesPerRow)
```

**Objective-C**

```objective-c
// 同时使用 CPU 修改并同步受管理纹理的数据。
[_imageTexture replaceRegion:MTLRegionMake2D(textureOrigin.x, textureOrigin.y, textureSize.width, textureSize.height)
                 mipmapLevel:0
                   withBytes:textureData
                 bytesPerRow:pixelSize*textureSize.width];
```

在编码 GPU 修改之后，编码一条 [- synchronizeResource:](<mtlblitcommandencoder/synchronize(resource_).md>) 命令。此命令更新整个纹理并保持同步。要更新特定的纹理切片或 mipmap 层级，请改用 [- synchronizeTexture:slice:level:](<mtlblitcommandencoder/synchronize(texture_slice_level_).md>) 命令。在执行此命令之前，CPU 上修改后的纹理数据处于未定义状态。

**Swift**

```swift
// 为 GPU 工作创建命令缓冲区。
if let commandBuffer = commandQueue.makeCommandBuffer() {
    // 创建一个计算命令编码器。
    guard let computeCommandEncoder =
            commandBuffer.makeComputeCommandEncoder(dispatchType: MTLDispatchType.serial)
    else { return }
    
    // 编码一个计算 pass，使用 GPU 修改受管理纹理的数据。
    computeCommandEncoder.setComputePipelineState(computePipelineStateObject)
    computeCommandEncoder.setTexture(imageTexture, index: 0)
    computeCommandEncoder.dispatchThreads(gridSize, threadsPerThreadgroup: threadgroupSize)
    computeCommandEncoder.endEncoding()
    
    // 同步受管理纹理。
    guard let blitCommandEncoder = commandBuffer.makeBlitCommandEncoder() else { return }
    blitCommandEncoder.synchronize(resource: imageTexture)
    blitCommandEncoder.endEncoding()
    
    // 添加一个完成处理程序。
    commandBuffer.addCompletedHandler { commandBuffer in
        // 一旦完成处理程序被调用，就可以安全地在 CPU 上使用受管理资源。
    }

    // 提交命令缓冲区。
    commandBuffer.commit()
}
```

**Objective-C**

```objective-c
// 为 GPU 工作创建命令缓冲区。
id <MTLCommandBuffer> commandBuffer = [_commandQueue commandBuffer];

// 编码一个计算 pass，使用 GPU 修改受管理纹理的数据。
id <MTLComputeCommandEncoder> computeCommandEncoder = [commandBuffer computeCommandEncoderWithDispatchType:MTLDispatchTypeSerial];
[computeCommandEncoder setComputePipelineState:computePipelineStateObject];
[computeCommandEncoder setTexture:_imageTexture
                          atIndex:0];
[computeCommandEncoder dispatchThreads:gridSize
                 threadsPerThreadgroup:threadgroupSize];
[computeCommandEncoder endEncoding];

// 使用一条编码后的命令同步受管理纹理。
id <MTLBlitCommandEncoder> blitCommandEncoder = [commandBuffer blitCommandEncoder];
[blitCommandEncoder synchronizeResource:_imageTexture];
[blitCommandEncoder endEncoding];

// 添加一个完成处理程序并提交命令缓冲区。
[commandBuffer addCompletedHandler:^(id<MTLCommandBuffer> commandBuffer) {
    // 一旦完成处理程序被调用，就可以安全地在 CPU 上使用受管理资源。
}];
[commandBuffer commit];
```

## 另请参阅

### 资源管理

- [设置资源存储模式](setting-resource-storage-modes.md) — 设置用于定义资源内存位置和访问权限的存储模式。
- [为 Apple GPU 选择资源存储模式](choosing-a-resource-storage-mode-for-apple-gpus.md) — 在 Apple GPU 上为你的纹理和缓冲区选择适当的存储模式。
- [为 Intel 和 AMD GPU 选择资源存储模式](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md) — 在 AMD 和 Intel GPU 上为你的纹理和缓冲区选择适当的存储模式。
- [将数据复制到私有资源](copying-data-to-a-private-resource.md) — 使用 blit 命令编码器将缓冲区或纹理数据复制到私有资源。
- [在连接的 GPU 之间传输数据](transferring-data-between-connected-gpus.md) — 利用 GPU 之间的高速连接快速传输数据。
- [减少 Metal App 的内存占用空间](reducing-the-memory-footprint-of-metal-apps.md) — 了解在 iOS 和 tvOS 中高效使用内存的最佳实践。
