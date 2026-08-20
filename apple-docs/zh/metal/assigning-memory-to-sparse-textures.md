---
title: 为稀疏纹理分配内存
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/assigning-memory-to-sparse-textures
source_url: 'https://developer.apple.com/documentation/metal/assigning-memory-to-sparse-textures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/assigning-memory-to-sparse-textures.json'
content_hash: 'sha256:dae9b112cb934a5d'
translated: true
---

> 导航：[技术](../technologies.md) · [Metal](../metal.md) · [纹理](textures.md)

# 为稀疏纹理分配内存

<sub>文章</sub>

使用资源状态编码器为稀疏纹理分配和释放稀疏 tile。

## 概述

稀疏纹理只有在你显式提供存储空间时才有存储。纹理中的每个 Mip 层级都被划分为 tile 大小的区域。每个区域可以是以下三种状态之一：

- _未映射 —_ 该区域没有内存存储。
- _未初始化 —_ 你已将一个稀疏 tile 映射到该区域，但未提供纹理数据。
- _已初始化 —_ 你已映射一个稀疏 tile 并提供了纹理数据。

最初，纹理的所有区域都处于未映射状态。要为某个区域提供数据，你需要让 GPU 将纹理中的区域映射到纹理堆上的稀疏 tile，然后将数据拷贝或渲染到这些区域。当某个区域不再需要内存时，你需要取消映射该区域以释放其内存，供未来请求使用。

### 映射或取消映射稀疏 tile

要映射或取消映射稀疏 tile，你可以使用资源状态命令编码器（[MTLResourceStateCommandEncoder](mtlresourcestatecommandencoder.md)）向 GPU 发出命令。为每次更新编码一条命令，指定纹理、该纹理中的 slice 和 Mip 层级，以及该 Mip 层级内的区域。用 tile 坐标指定区域。

**Swift**

```swift
if let encoder = commandBuffer.makeResourceStateCommandEncoder() {
    encoder.updateTextureMapping(texture, mode: .map, region: tileRegion, mipLevel: 0, slice: 0)
    encoder.endEncoding()
}
```

**Objective-C**

```objective-c
id<MTLResourceStateCommandEncoder> encoder = [commandBuffer resourceStateCommandEncoder];

[encoder updateTextureMapping:texture
                         mode:MTLSparseTextureMappingModeMap
                       region:tileRegion
                     mipLevel:0
                        slice:0];

[encoder endEncoding];
```

GPU 会在纹理的堆上寻找空闲的稀疏 tile，并将它们分配给该纹理。映射过程完成后，未来对该区域进行读取、写入或采样操作的请求将访问已分配的 tile。Metal 不会使用数据初始化这些 tile，因此为了确保有有效数据可用，请在从这些区域读取或采样之前，将数据拷贝或渲染到新映射的区域中。

GPU 按你编码命令的顺序处理映射请求。在每个命令内，GPU 以行优先顺序、按先到先得的原则映射 tile。如果堆空间不足，Metal 会跳过请求中任何剩余的 tile。

要释放 tile 并使更多内存可用于满足其他请求，请改用 [MTLSparseTextureMappingModeUnmap](mtlsparsetexturemappingmode/unmap.md) 模式编码命令。

> [!important] 重要
> 在释放稀疏纹理之前，请取消映射其所有稀疏 tile。否则，稀疏堆会继续将这些 tile 标记为已映射。但是，当你释放堆时，Metal 会释放所有已映射的 tile 内存。

### 在创建纹理后映射尾 Mip 层级

如果你为纹理创建了完整的 Mip 链，许多较低级别的 Mip 层级会小于稀疏 tile 的大小。为了节省内存，Metal 会将所有这些较小的 Mip 层级打包到一个内存分配中，通常是一个稀疏 tile。为了保证纹理始终有可采样的数据，通常需要在创建纹理后映射尾 Mip 层级，并保持其映射状态直到准备释放纹理。

要映射尾 Mip 层级，请向纹理请求尾部的第一个 Mip 层级，并映射其中的任何区域。所有尾 Mip 层级都会被映射。

**Swift**

```swift
let tailRegion = MTLRegionMake2D(0, 0, 1, 1)

encoder.updateTextureMapping(texture, mode: .map, region: tailRegion, mipLevel: texture.firstMipmapInTail, slice: 0)
```

**Objective-C**

```objective-c
MTLRegion tailRegion = MTLRegionMake2D(0, 0, 1, 1);

[encoder updateTextureMapping:texture
                         mode:MTLSparseTextureMappingModeMap
                       region:tailRegion
                     mipLevel:texture.firstMipmapInTail
                        slice:0];
```

类似地，如果你取消映射尾部的第一个 Mip 层级，所有尾 Mip 层级都会被取消映射。

### 同步对 tile 映射和取消映射的访问

Tile 映射由 GPU 执行，这意味着它会在你提交命令缓冲区后的某个未来时间点异步发生。当纹理的内容正在被读取或写入时，不要更改分配给该纹理的内存。使用围栏（fence）或事件（event）来确保这些操作不会重叠。

> [!important] 重要
> 如果使用多个资源状态编码器来编码访问同一稀疏堆的命令，则需要按顺序执行它们，否则你的 App 可能会崩溃。例如，如果你的 App 中有两个不同的命令队列，并且两者都为同一个堆编码了资源状态命令，请使用共享事件同步访问，以便更新按顺序进行。

有关同步 Metal 命令的更多信息，请参阅[资源同步](resource-synchronization.md)。

## 另请参阅

### 稀疏纹理

- [管理稀疏纹理内存](managing-sparse-texture-memory.md) — 通过使用稀疏纹理，直接控制纹理数据的内存分配。
- [创建稀疏堆和稀疏纹理](creating-sparse-heaps-and-sparse-textures.md) — 通过创建稀疏堆为稀疏纹理分配内存。
- [在像素区域和稀疏 tile 区域之间转换](converting-between-pixel-regions-and-sparse-tile-regions.md) — 了解稀疏纹理的内容在内存中如何组织。
- [读取和写入稀疏纹理](reading-and-writing-to-sparse-textures.md) — 决定如何处理对未映射纹理区域的访问。
- [估算纹理区域的访问频率](estimating-how-often-a-texture-region-is-accessed.md) — 使用纹理访问模式来确定何时需要映射纹理区域。
- [MTLResourceStatePassDescriptor](mtlresourcestatepassdescriptor.md) — 资源状态通道的配置，用于创建资源状态命令编码器。
- [MTLResourceStatePassSampleBufferAttachmentDescriptor](mtlresourcestatepasssamplebufferattachmentdescriptor.md) — 在资源状态通道的开始和结束位置存储 GPU 计数器信息的描述。
- [MTLResourceStatePassSampleBufferAttachmentDescriptorArray](mtlresourcestatepasssamplebufferattachmentdescriptorarray.md) — 资源状态通道的采样缓冲区附件数组。
- [MTLResourceStateCommandEncoder](mtlresourcestatecommandencoder.md) — 一种编码器，用于编码修改资源配置的命令。
- [MTLMapIndirectArguments](mtlmapindirectarguments.md) — 在使用间接命令映射稀疏纹理区域时的数据布局。
