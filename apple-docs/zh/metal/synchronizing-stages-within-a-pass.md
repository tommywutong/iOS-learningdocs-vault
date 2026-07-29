---
title: 同步 pass 内的阶段
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/synchronizing-stages-within-a-pass
source_url: 'https://developer.apple.com/documentation/metal/synchronizing-stages-within-a-pass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/synchronizing-stages-within-a-pass.json'
content_hash: 'sha256:db5e86c58101b762'
translated: true
---

> 导航：[技术](../technologies.md) · [Metal](../metal.md) · [资源同步](resource-synchronization.md)

# 同步 pass 内的阶段

<sub>文章</sub>

阻止同一个 pass 内的 GPU 阶段运行，直到同一 pass 内的其他阶段执行完毕。

## 概述

pass 内屏障（intrapass barrier）可解决同一 pass 内命令之间的访问冲突，且不影响任何其他 pass。当你的 App 编码的命令从不同 pass 访问某个资源，或者从同一个 pass 内的不同阶段访问该资源时，如果至少有一条命令修改了该资源，就会产生访问冲突。之所以会发生这种冲突，是因为 GPU 可能同时运行多条命令，包括来自以下各项的命令：

- 多个 pass
- pass 的不同阶段，例如计算 pass 的 [MTLStageBlit](mtlstages/blit.md) 和 [MTLStageDispatch](mtlstages/dispatch.md) 阶段
- pass 中某个阶段的多个实例，例如计算 pass 中的两条或更多条调度命令

有关资源访问冲突和 GPU 阶段的更多信息，请分别参阅[资源同步](resource-synchronization.md)和 [MTLStages](mtlstages.md)。

首先，找出同一个 pass 内不同阶段中哪些内存操作会引发冲突。然后，通过添加一个 pass 内屏障来解决冲突，让 GPU 在运行消费阶段之前暂停，直到生产阶段执行完毕。

> [!note] 注意
> pass 内屏障不会影响任何其他 pass。GPU 可能仍在运行之前的 pass，也可能开始运行下一个 pass，或者两者同时进行。

### 识别单个 pass 内的访问冲突

以下代码示例对一个计算 pass 进行了编码，该 pass 的复制命令和调度命令之间存在访问冲突。

**Swift**

```swift
func encodeComputeWorkWithIntrapassBarrier(computeEncoder: MTL4ComputeCommandEncoder,
                                           argumentTable: MTL4ArgumentTable,
                                           buffers: [MTLBuffer])
{
    // 将参数表分配给计算编码器。
    computeEncoder.setArgumentTable(argumentTable)

    // 将缓冲区添加到参数表。
    let bufferA = buffers[0]
    let bufferB = buffers[1]

    argumentTable.setAddress(bufferA.gpuAddress, index: 0)
    argumentTable.setAddress(bufferB.gpuAddress, index: 1)

    // 编码一条复制命令，该命令在 blit 阶段由 GPU 运行。
    computeEncoder.copy(sourceBuffer: bufferA, sourceOffset: 0,
                        destinationBuffer: bufferB, destinationOffset: 0,
                        size: copySize)

    // 此方法在此处需要一个屏障。

    // 运行一条处理 `bufferB` 的调度命令，
    // 该命令在调度阶段由 GPU 运行。
    computeEncoder.setComputePipelineState(modifyBufferIndex1ComputePipeline)
    computeEncoder.dispatchThreadgroups(threadgroupsPerGrid: threadgroupCount,
                                        threadsPerThreadgroup: threadsPerThreadgroup)
}
```

**Objective-C**

```objective-c
- (void)encodeComputeWorkWithIntrapassBarrier:(id<MTL4ComputeCommandEncoder>)computeEncoder
                                argumentTable:(id<MTL4ArgumentTable>)argumentTable
                                      buffers:(id<MTLBuffer> *)buffers
{
    // 将参数表分配给计算编码器。
    [computeEncoder setArgumentTable:argumentTable];

    // 将缓冲区添加到参数表。
    id<MTLBuffer> bufferA = buffers[0];
    id<MTLBuffer> bufferB = buffers[1];

    [argumentTable setAddress:bufferA.gpuAddress atIndex:0];
    [argumentTable setAddress:bufferB.gpuAddress atIndex:1];

    // 编码一条复制命令，该命令在 blit 阶段由 GPU 运行。
    [computeEncoder copyFromBuffer:bufferA sourceOffset:0
                          toBuffer:bufferB destinationOffset:0
                              size:copySize];

    // 此方法在此处需要一个屏障。

    // 运行一条处理 `bufferB` 的调度命令，
    // 该命令在调度阶段由 GPU 运行。
    [computeEncoder setComputePipelineState:modifyBufferIndex1ComputePipeline];
    [computeEncoder dispatchThreadgroups:threadgroupCount
                   threadsPerThreadgroup:threadsPerThreadgroup];
}
```

该示例至少存在一个访问冲突，因为该 pass 从不同阶段访问了两个共享资源——`bufferA` 和 `bufferB`——并且至少有一条命令修改了其中一个或多个资源。

复制命令和调度命令分别在 blit 阶段和调度阶段运行；两条命令都修改了 `bufferB`。

![](../../../attachments/c561aebb95e82f882e2699eec5fa477c/synchronizing-stages-within-a-pass-1@2x.png)

<sub>图表显示了一个包含复制和调度命令的单个计算 pass，两者都访问 buffer B，其中复制命令在 blit 阶段运行并存储到 buffer B，而调度命令在调度阶段运行并修改 buffer B。</sub>

如果没有屏障，GPU 可以随时以任意相对顺序运行这些命令，甚至同时运行，这可能导致存在访问冲突的资源产生不一致的结果。

![](../../../attachments/d51f338f01e9acac15e205d1ba45ebed/synchronizing-stages-within-a-pass-2@2x.png)

<sub>图表显示了 blit 和调度阶段在没有同步的情况下并行运行，当两者都访问 buffer B 时可能导致不一致的结果。</sub>

### 使用屏障解决 pass 内冲突

通过使用编码器的 [barrier(afterEncoderStages:beforeEncoderStages:visibilityOptions:)](<mtl4commandencoder/barrier(afterencoderstages_beforeencoderstages_visibilityoptions_).md>) 方法添加一个 pass 内屏障，来解决同一 pass 内命令之间的访问冲突。

以下代码示例修改了上一个示例，在 pass 内的 blit 和调度阶段之间添加了一个 pass 内屏障。

**Swift**

```swift
    // 编码一条复制命令，该命令在 blit 阶段由 GPU 运行。
    computeEncoder.copy(sourceBuffer: bufferA, sourceOffset: 0,
                        destinationBuffer: bufferB, destinationOffset: 0,
                        size: copySize)

    // 在上面的复制和下面的调度之间添加一个屏障。
    computeEncoder.barrier(afterEncoderStages: .blit,
                           beforeEncoderStages: .dispatch,
                           visibilityOptions: .device)

    // 运行一条处理 `bufferB` 的调度命令，
    // 该命令在调度阶段由 GPU 运行。
    computeEncoder.setComputePipelineState(modifyBufferIndex1ComputePipeline)
    computeEncoder.dispatchThreadgroups(threadgroupsPerGrid: threadgroupCount,
                                        threadsPerThreadgroup: threadsPerThreadgroup)
```

**Objective-C**

```objective-c
    // 编码一条复制命令，该命令在 blit 阶段由 GPU 运行。
    [computeEncoder copyFromBuffer:bufferA sourceOffset:0
                          toBuffer:bufferB destinationOffset:0
                              size:copySize];

    // 在上面的复制和下面的调度之间添加一个屏障。
    [computeEncoder barrierAfterEncoderStages:MTLStageBlit
                          beforeEncoderStages:MTLStageDispatch
                            visibilityOptions:MTL4VisibilityOptionDevice];

    // 运行一条处理 `bufferB` 的调度命令，
    // 该命令在调度阶段由 GPU 运行。
    [computeEncoder setComputePipelineState:modifyBufferIndex1ComputePipeline];
    [computeEncoder dispatchThreadgroups:threadgroupCount
                   threadsPerThreadgroup:threadsPerThreadgroup];
```

上述代码示例在 blit 阶段和调度阶段之间添加了一个屏障，因为它们都通过加载或存储操作访问 `bufferB`。该屏障强制 GPU 等到 blit 命令完成后才开始调度阶段。

![](../../../attachments/5730800e64956f5a9090f6ea4451e8c8/synchronizing-stages-within-a-pass-3@2x.png)

<sub>图表显示了 pass 内屏障同步，GPU 等待 blit 阶段完成后才开始调度阶段。</sub>

该屏障确保了 blit 阶段命令的存储操作完全完成后，调度阶段命令才从同一内存加载。

### 编码依赖于片段或图块阶段输出的命令

对于采用基于图块的延迟渲染（TBDR）架构的设备（例如 Apple 芯片 GPU），Metal 不支持等待 [MTLStageTile](mtlstages/tile.md) 或 [MTLStageFragment](mtlstages/fragment.md) 阶段的 pass 内屏障。

> [!note] 注意
> 有关 TBDR 架构的更多信息，请参阅[针对 Apple GPU 和基于图块的延迟渲染调整你的 App](tailor-your-apps-for-apple-gpus-and-tile-based-deferred-rendering.md)。

你可以编码一个依赖于前一个图块调度结果的图块调度，因为图块计算调度可以访问同一图块中任何位置的数据。类似地，你可以编码一个依赖于前一个绘制命令片段阶段结果的绘制命令，因为片段着色器只能访问其特定像素位置的数据。但是，如果某个图块调度需要另一个图块的结果，或者某个片段着色器需要另一个片段的结果，则需要启动一个新的渲染 pass 并使用屏障进行同步。

例如，要通过在新 pass 中添加基于消费者的队列屏障来同步两个 pass：

1. 调用编码器的 [- endEncoding](<mtl4commandencoder/endencoding().md>) 方法来结束当前渲染 pass。
2. 通过从命令缓冲区或队列的其他绑定创建新的渲染编码器，来启动一个新的渲染 pass。
3. 调用新编码器的 [barrier(afterQueueStages:beforeStages:visibilityOptions:)](<mtl4commandencoder/barrier(afterqueuestages_beforestages_visibilityoptions_).md>) 方法来添加一个消费者屏障，从而同步前一个渲染 pass 的结果。

类似地，要在 pass 中创建基于生产者的队列屏障：

1. 调用编码器的 [barrier(afterStages:beforeQueueStages:visibilityOptions:)](<mtl4commandencoder/barrier(afterstages_beforequeuestages_visibilityoptions_).md>) 方法来添加一个生产者屏障，从而同步当前渲染 pass 的结果。
2. 调用编码器的 [- endEncoding](<mtl4commandencoder/endencoding().md>) 方法来结束当前渲染 pass。
3. 通过从命令缓冲区或队列的其他绑定创建新的编码器，来启动一个新的渲染 pass。

或者，使用 [MTLFence](mtlfence.md)：

1. 调用编码器的 [- updateFence:afterEncoderStages:](<mtl4commandencoder/updatefence(__afterencoderstages_).md>) 方法来更新当前渲染 pass 中的一个 fence。
2. 调用编码器的 [- endEncoding](<mtl4commandencoder/endencoding().md>) 方法来结束当前渲染 pass。
3. 通过从同一个命令缓冲区创建新的编码器，来启动一个新的渲染 pass。
4. 调用新编码器的 [- waitForFence:beforeEncoderStages:](<mtl4commandencoder/waitforfence(__beforeencoderstages_).md>) 方法来等待新渲染 pass 中的同一个 fence 实例。

有关其他同步机制的更多信息，请参阅本系列的以下文章：

- [使用 fence 同步 pass](synchronizing-passes-with-a-fence.md)
- [使用消费者屏障同步 pass](synchronizing-passes-with-consumer-barriers.md)
- [使用生产者屏障同步 pass](synchronizing-passes-with-producer-barriers.md)

## 另请参阅

### 使用屏障和 fence 进行同步

- [使用 fence 同步 pass](synchronizing-passes-with-a-fence.md) — 阻止 pass 中的 GPU 阶段运行，直到另一个 pass 通过发出 fence 信号来解除阻塞。
- [使用消费者屏障同步 pass](synchronizing-passes-with-consumer-barriers.md) — 阻止一个 pass 及其所有后续 pass 中的 GPU 阶段运行，直到之前各 pass 的阶段执行完毕。
- [使用生产者屏障同步 pass](synchronizing-passes-with-producer-barriers.md) — 阻止后续 pass 中的 GPU 阶段运行，直到当前 pass 及之前各 pass 的阶段执行完毕。
- [同步 CPU 和 GPU 工作](synchronizing-cpu-and-gpu-work.md) — 通过使用资源的多个实例来避免 CPU 和 GPU 工作之间的停滞。
- [使用堆和 fence 实现多阶段图像滤镜](implementing-a-multistage-image-filter-using-heaps-and-fences.md) — 使用 fence 来同步对堆上分配的资源的访问。
- [MTLStages](mtlstages.md) — Metal pass 类型中命令执行的各个阶段。
- [MTLFence](mtlfence.md) — 一种同步机制，用于对 GPU pass 之间的内存操作进行排序。
- [MTLRenderStages](mtlrenderstages.md) — 渲染 pass 中触发同步命令的阶段。
- [MTLBarrierScope](mtlbarrierscope.md) — 描述屏障操作的资源类型。
- [MTL4VisibilityOptions](mtl4visibilityoptions.md) — 同步命令的内存一致性选项。
