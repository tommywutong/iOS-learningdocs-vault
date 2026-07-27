---
title: GPU 设备与工作提交
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/gpu-devices-and-work-submission
source_url: 'https://developer.apple.com/documentation/metal/gpu-devices-and-work-submission'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/gpu-devices-and-work-submission.json'
content_hash: 'sha256:504be891e20f8c2d'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md)

# GPU 设备与工作提交

<sub>API 集合</sub>

查找任意可用的 GPU，使用命令缓冲区向其提交工作，挂起工作，并在多个 GPU 之间进行协调。

## 概述

除了 [MTLCreateSystemDefaultDevice](<mtlcreatesystemdefaultdevice().md>) 返回的默认实例外，你还可以使用任意可用 GPU 的 [MTLDevice](mtldevice.md) 实例。对于每个设备实例，获取其 [MTLCommandQueue](mtlcommandqueue.md) 实例，并创建一个或多个 [MTLCommandBuffer](mtlcommandbuffer.md) 实例，以便向 GPU 发送工作。

当系统挂起你的 App 时，使用命令队列来完成已在进行中的命令缓冲区。更多信息参见 [Preparing your Metal app to run in the background](preparing-your-metal-app-to-run-in-the-background.md)。

## 主题

### 定位并检查 GPU 设备

- [Getting the default GPU](getting-the-default-gpu.md) — 选择系统的默认 GPU 设备，用于运行你的 Metal 代码。
- [Detecting GPU features and Metal software versions](detecting-gpu-features-and-metal-software-versions.md) — 使用设备对象的属性来决定你在 Metal 中如何执行任务。
- [MTLCreateSystemDefaultDevice](<mtlcreatesystemdefaultdevice().md>) — 返回 Metal 选定为默认值的设备实例。
- [MTLDevice](mtldevice.md) — App 用于绘制图形并并行运行计算的主要 Metal GPU 接口。
- [Multi-GPU systems](multi-gpu-systems.md) — 定位并使用内部和外部 GPU 及其显示器、显存以及性能权衡。

### 使用 Metal 4 向 GPU 提交工作

- [MTL4CommandQueue](mtl4commandqueue.md) — 表示命令队列的抽象，你用它来提交并同步命令缓冲区，以及执行其他 GPU 操作。
- [MTL4CommandQueueDescriptor](mtl4commandqueuedescriptor.md) — 将创建新命令队列所需的参数组合在一起。
- [MTL4CommandQueueError](mtl4commandqueueerror-swift.struct.md)
- [Code](mtl4commandqueueerror-swift.struct/code.md) — 提交一个命令缓冲区实例数组可能产生的错误种类的枚举。
- [MTL4CommandQueueErrorDomain](mtl4commandqueueerrordomain.md)
- [MTL4CommandBuffer](mtl4commandbuffer.md) — 记录一系列 GPU 命令。
- [MTL4CommandBufferOptions](mtl4commandbufferoptions.md) — 在向命令缓冲区编码工作之前用于配置该命令缓冲区的选项。
- [MTL4CommandEncoder](mtl4commandencoder.md) — 将 GPU 命令写入命令缓冲区的编码器。
- [MTL4RenderEncoderOptions](mtl4renderencoderoptions.md) — 在创建编码器时指定的自定义渲染流程选项。
- [MTL4ArgumentTable](mtl4argumenttable.md) — 提供一种机制，用于管理和提供缓冲区、纹理、采样器状态以及其他 Metal 资源的资源绑定。
- [MTL4ArgumentTableDescriptor](mtl4argumenttabledescriptor.md) — 将创建 Metal 参数表所需的参数组合在一起。
- [MTL4CommandAllocator](mtl4commandallocator.md) — 管理将 GPU 命令编码到命令缓冲区所依赖的内存。
- [MTL4CommandAllocatorDescriptor](mtl4commandallocatordescriptor.md) — 将创建命令分配器所需的参数组合在一起。
- [MTL4CommitOptions](mtl4commitoptions.md) — 表示用于配置命令队列上的提交操作的选项。
- [MTL4CommitFeedback](mtl4commitfeedback.md) — 描述一个对象，在完成工作负载后由 Metal 向你的 App 提供调试信息。
- [MTL4CommitFeedbackHandler](mtl4commitfeedbackhandler.md) — 定义 Metal 在完成工作负载后调用以向你的 App 提供反馈的回调的代码块签名。
- [MTL4CounterHeap](mtl4counterheap.md) — 表示一段不透明的、由驱动程序控制的内存区域，可用于存储 GPU 计数器数据。
- [MTL4CounterHeapDescriptor](mtl4counterheapdescriptor.md) — 将在创建时用于配置计数器堆对象的参数组合在一起。
- [MTL4CounterHeapType](mtl4counterheaptype.md) — 定义 [MTL4CounterHeap](mtl4counterheap.md) 的类型及其条目的内容。
- [MTL4TimestampHeapEntry](mtl4timestampheapentry.md) — 表示类型为 `MTL4CounterHeapTypeTimestamp` 的计数器堆中的一个时间戳数据条目。
- [MTL4TimestampGranularity](mtl4timestampgranularity.md) — 就写入 GPU 计数器时间戳时所需的精度向系统提供提示。

### 使用 Metal 向 GPU 提交工作

- [Setting up a command structure](setting-up-a-command-structure.md) — 了解 Metal 如何在 GPU 上执行命令。
- [MTLCommandQueue](mtlcommandqueue.md) — 用于创建、提交并调度命令缓冲区到特定 GPU 设备，以运行这些缓冲区中命令的实例。
- [MTLCommandQueueDescriptor](mtlcommandqueuedescriptor.md) — 用于自定义新命令队列行为的配置。
- [MTLCommandBuffer](mtlcommandbuffer.md) — 用于存储你编码到其中的一系列 GPU 命令的容器。
- [MTLCommandBufferDescriptor](mtlcommandbufferdescriptor.md) — 用于自定义新命令缓冲区行为的配置。
- [MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md) — 指示 GPU 为何未能完成执行某个命令缓冲区的命令缓冲区错误代码。
- [MTLCommandEncoder](mtlcommandencoder.md) — 将 GPU 命令写入命令缓冲区的编码器。

### 挂起 GPU 上的工作

- [Preparing your Metal app to run in the background](preparing-your-metal-app-to-run-in-the-background.md) — 通过暂停未来的 GPU 使用并确保之前的工作已被调度，为你的 App 转入后台做好准备。
