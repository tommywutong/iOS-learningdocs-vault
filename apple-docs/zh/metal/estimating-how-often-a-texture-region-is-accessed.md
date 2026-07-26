---
title: 估算纹理区域被访问的频率
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/estimating-how-often-a-texture-region-is-accessed
source_url: 'https://developer.apple.com/documentation/metal/estimating-how-often-a-texture-region-is-accessed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/estimating-how-often-a-texture-region-is-accessed.json'
content_hash: 'sha256:9986dd2d96c5f3c3'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [Textures](textures.md)

# 估算纹理区域被访问的频率

<sub>文章</sub>

利用纹理访问模式来确定你何时需要映射某个纹理区域。

## 概述

使用稀疏纹理时，你需要决定何时映射或取消映射纹理区域。举例来说，一种做法是映射整个 mipmap，使用现有技巧来确定哪些 mipmap 被访问过。（更多信息请参阅[动态调整纹理细节层级](dynamically-adjusting-texture-level-of-detail.md)。）你可能还想更进一步，只映射单个 mipmap 内的子区域。为了帮助你做到这一点，Metal 提供了一种机制来估算你访问每个区域的频率。当你检测到对某个给定区域的请求数量足够多时，就可以为其映射一个稀疏图块。

当 GPU 尝试对纹理内存中的某个像素进行采样时：

1. 如果该像素已经存在于 GPU 的内存缓存中，它会将该缓存像素返回给你的着色器。否则，它会执行以下剩余步骤。
2. GPU 递增其访问计数器，并请求该纹理的像素数据。
3. 如果该稀疏图块已被映射，在请求完成后，GPU 会将像素数据放入缓存并返回给你的着色器。
4. 如果该稀疏图块未被映射，GPU 会将置零的数据加载到缓存中并返回给你的着色器。

纹理访问计数的估算来自缓存未命中的次数，并非对某个特定区域内存操作次数的精确计数。如果你的 App 频繁访问相同的区域，由于它们更有可能位于缓存中，你从 Metal 获得的计数可能会小于你实际执行的内存操作次数。

为了利用空间局部性，内存子系统会以更大的块（称为_缓存行_）检索内存。一个缓存行通常足以存储多个像素的数据，但具体的像素数量取决于像素格式。

为了对访问计数进行归一化处理，Metal 会像你访问了该缓存行中所有像素一样递增该计数。举例来说，如果一个缓存行是 `64` 字节，而一个像素是 `4` 字节，那么该计数器的值会增加 `16` `(64/4)`。这种抽象意味着你可以专注于记录下来的内存操作次数，而无需了解底层内存架构的细节。

请自行判断启发式规则，以决定需要多少次像素内存操作才足以开始为该区域映射一个稀疏图块。

### 请求估算的纹理访问计数

要获取某个稀疏纹理当前的访问计数，请创建一个 blit 命令编码器，并编码命令将 GPU 的内部计数器复制到一个 [MTLBuffer](mtlbuffer.md) 实例中。以下示例代码获取纹理顶层 mipmap 中的一个图块区域，创建一个足以容纳该区域所有图块的 [MTLBuffer](mtlbuffer.md) 实例，并编码一条复制这些计数器的命令。

**Swift**

```swift
let counterBufferSize = MemoryLayout<UInt32>.stride * tileRegion.size.height * tileRegion.size.width * tileRegion.size.depth
if let counters = device.makeBuffer(length: counterBufferSize, options: .storageModeShared) {
    if let blitEncoder = commandBuffer.makeBlitCommandEncoder() {
        blitEncoder.label = "Copy Texture Miss Counts"
        blitEncoder.getTextureAccessCounters(texture, region: tileRegion, mipLevel: 0, slice: 0,
                                             resetCounters: true, countersBuffer: counters, countersBufferOffset: 0)
    }
}
```

**Objective-C**

```objective-c
size_t counterBufferSize = sizeof(uint32_t) * tileRegion.size.height * tileRegion.size.width * tileRegion.size.depth;
id<MTLBuffer> counters = [_device newBufferWithLength:counterBufferSize
                                               options:MTLResourceStorageModeShared];

id<MTLBlitCommandEncoder> blitEncoder = [commandBuffer blitCommandEncoder];
blitEncoder.label = @"Copy Texture Miss Counts";
[blitEncoder getTextureAccessCounters:_sparseTexture
                               region:tileRegion
                             mipLevel:0
                                slice:0
                        resetCounters:YES
                       countersBuffer:counters
                 countersBufferOffset:0];
```

这些计数器被组织为一个按行优先顺序存储的 [uint32_t](../kernel/uint32_t.md) 值的三维数组。你可以告知 GPU 是否要重置这些访问计数器。

如果你想获取同一纹理中多个 mipmap 的信息，或者多张纹理的信息，请为每个 mipmap/纹理组合分别编码一条命令。不要为每次请求分配一个缓冲区；应分配更大的 [MTLBuffer](mtlbuffer.md) 实例，并为每次请求在这些缓冲区内指定偏移量。

## 另请参阅

### Sparse textures

- [管理稀疏纹理内存](managing-sparse-texture-memory.md) — 通过使用稀疏纹理直接控制纹理数据的内存分配。
- [创建稀疏堆和稀疏纹理](creating-sparse-heaps-and-sparse-textures.md) — 通过创建稀疏堆为稀疏纹理分配内存。
- [在像素区域和稀疏图块区域之间转换](converting-between-pixel-regions-and-sparse-tile-regions.md) — 了解稀疏纹理的内容在内存中是如何组织的。
- [为稀疏纹理分配内存](assigning-memory-to-sparse-textures.md) — 使用资源状态编码器为稀疏纹理分配和释放稀疏图块。
- [读写稀疏纹理](reading-and-writing-to-sparse-textures.md) — 决定如何处理对未映射纹理区域的访问。
- [MTLResourceStatePassDescriptor](mtlresourcestatepassdescriptor.md) — 用于资源状态流程的配置，用于创建资源状态命令编码器。
- [MTLResourceStatePassSampleBufferAttachmentDescriptor](mtlresourcestatepasssamplebufferattachmentdescriptor.md) — 描述在资源状态流程开始和结束时将 GPU 计数器信息存储在何处。
- [MTLResourceStatePassSampleBufferAttachmentDescriptorArray](mtlresourcestatepasssamplebufferattachmentdescriptorarray.md) — 资源状态流程的一组采样缓冲区附件数组。
- [MTLResourceStateCommandEncoder](mtlresourcestatecommandencoder.md) — 一个编码器，用于编码修改资源配置的命令。
- [MTLMapIndirectArguments](mtlmapindirectarguments.md) — 使用间接命令映射稀疏纹理区域时的数据布局。
