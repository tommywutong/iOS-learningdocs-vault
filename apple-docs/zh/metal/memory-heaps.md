---
title: 内存堆
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/memory-heaps
source_url: 'https://developer.apple.com/documentation/metal/memory-heaps'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/memory-heaps.json'
content_hash: 'sha256:ec05edc03407b6bb'
translated: true
---

> 导航：[技术](../technologies.md) · [Metal](../metal.md)

# 内存堆

<sub>API 集合</sub>

通过为各种缓冲区、纹理和其他资源创建大型内存分配，掌控你的 App 的 GPU 内存管理。

## 概述

使用 [MTLHeap](mtlheap.md) 快速创建和销毁 GPU 资源。内存堆（memory heap）还可以通过别名化（aliasing）其不同部分，帮助你的 App 节省内存。

调用 [MTLDevice](mtldevice.md) 实例的 [- newHeapWithDescriptor:](<mtldevice/makeheap(descriptor_).md>) 方法来创建一个堆。

> [!note] 注意
> Metal 仅同步你从 Metal 堆所创建且其 [hazardTrackingMode](mtlheap/hazardtrackingmode.md) 属性设为 [MTLHazardTrackingModeTracked](mtlhazardtrackingmode/tracked.md) 的资源。

## 主题

### 资源内存分配与管理

- [将参数缓冲区（argument buffer）与资源堆（resource heap）结合使用](using-argument-buffers-with-resource-heaps.md) — 通过在参数缓冲区中使用数组并将其与资源堆结合，降低 CPU 开销。
- [使用堆和事件（event）实现多阶段图像滤镜](implementing-a-multistage-image-filter-using-heaps-and-events.md) — 使用事件同步对堆上分配资源的访问。
- [使用堆和围栏（fence）实现多阶段图像滤镜](implementing-a-multistage-image-filter-using-heaps-and-fences.md) — 使用围栏同步对堆上分配资源的访问。
- [MTLHeap](mtlheap.md) — 一种内存池，你可以从其中对资源进行子分配（suballocate）。
- [MTLHeapDescriptor](mtlheapdescriptor.md) — 一种用于定制 Metal 内存堆行为的配置。
- [MTLHeapType](mtlheaptype.md) — 用于选择堆类型的选项。
- [MTLSizeAndAlign](mtlsizeandalign.md) — 资源的大小和对齐方式（以字节为单位）。

## 另请参阅

### 相关资源

- [资源基础](resource-fundamentals.md) — 控制所有 Metal 内存资源（包括缓冲区和纹理）的通用属性，以及如何配置其底层内存。
- [缓冲区](buffers.md) — 创建和管理你的 App 用于与其着色器函数交换信息的无类型数据。
- [纹理](textures.md) — 创建和管理你的 App 用于与其着色器函数交换信息的类型化数据。
- [资源加载](resource-loading.md) — 通过在你的 GPU 任务旁运行专用输入/输出队列，快速加载游戏和 App 中的资源。
- [资源同步](resource-synchronization.md) — 通过使用障碍（barrier）、围栏或事件协调读写操作，防止多个命令同时访问同一资源。
