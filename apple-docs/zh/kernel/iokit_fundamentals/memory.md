---
title: 内存
framework: Kernel
symbol_kind: symbol
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/kernel/iokit_fundamentals/memory
source_url: 'https://developer.apple.com/documentation/kernel/iokit_fundamentals/memory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/kernel/iokit_fundamentals/memory.json'
content_hash: 'sha256:5e5b7cbad8ea75c6'
translated: true
---

> 导航：[技术](../../technologies.md) · [Kernel](../../kernel.md) · [IOKit 基础](../iokit_fundamentals.md)

# 内存

<sub>API 集合</sub>

在内核中分配、映射、释放和管理内存。

## 主题

### 描述符

- [IOBufferMemoryDescriptor](../iobuffermemorydescriptor.md) — 一个简单的内存描述符，用于分配其自身的缓冲区内存。
- [IODeviceMemory](../iodevicememory.md) — 用于设备物理内存范围的 IOMemoryDescriptor。
- [IOGeneralMemoryDescriptor](../iogeneralmemorydescriptor.md)
- [IOInterleavedMemoryDescriptor](../iointerleavedmemorydescriptor.md) — IOInterleavedMemoryDescriptor 对象描述由多个其他 IOMemoryDescriptor 的部分组成的内存区域。
- [IOMultiMemoryDescriptor](../iomultimemorydescriptor.md) — IOMultiMemoryDescriptor 对象描述由多个其他 IOMemoryDescriptor 组成的内存区域。
- [IOSubMemoryDescriptor](../iosubmemorydescriptor.md) — IOSubMemoryDescriptor 对象描述由另一个 IOMemoryDescriptor 的一部分构成的内存区域。
- [IOMemoryDescriptor](../iomemorydescriptor.md) — 一个抽象基类，定义了描述物理或虚拟内存的通用方法。

### 直接内存访问（DMA）

- [IODMACommand](../iodmacommand.md) — 一个将内存引用转换为 I/O 总线地址的对象。
- [IODMAController](../iodmacontroller.md)
- [IODMAEventSource](../iodmaeventsource.md)

### 释放

- [IOFree](../1575290-iofree.md) — 释放通过 IOMalloc 分配的内存。
- [IOFreeAligned](../1575330-iofreealigned.md) — 释放通过 IOMallocAligned 分配的内存。
- [IOFreePageable](../1575300-iofreepageable.md) — 释放通过 IOMallocPageable 分配的内存。

### 分配

- [IOMalloc](../1575326-iomalloc.md) — 在内核映射中分配通用用途的固定内存。
- [IOMallocAligned](../1575291-iomallocaligned.md) — 在内核映射中分配具有对齐限制的固定内存。
- [IOMallocPageable](../1575327-iomallocpageable.md) — 在内核映射中分配可分页内存。
- [IOMallocZero](../3074962-iomalloczero.md)
- [IORangeAllocator](../iorangeallocator.md) — 一个用于管理从某个范围进行分配的实用工具类。

### 映射内存

- [IOMapper](../iomapper.md)
- [IOMemoryMap](../iomemorymap.md) — 一个定义内存映射通用方法的类。
- [IOMappedRead16](../1575322-iomappedread16.md) — 从指定的“物理”IOSpace 地址读取两个字节。
- [IOMappedRead32](../1575311-iomappedread32.md) — 从指定的“物理”IOSpace 地址读取四个字节。
- [IOMappedRead64](../1575301-iomappedread64.md) — 从指定的“物理”IOSpace 地址读取八个字节。
- [IOMappedRead8](../1575317-iomappedread8.md) — 从指定的“物理”IOSpace 地址读取一个字节。
- [IOMappedWrite16](../1575315-iomappedwrite16.md) — 向指定的“物理”IOSpace 地址写入两个字节。
- [IOMappedWrite32](../1575310-iomappedwrite32.md) — 向指定的“物理”IOSpace 地址写入四个字节。
- [IOMappedWrite64](../1575313-iomappedwrite64.md) — 向指定的“物理”IOSpace 地址写入八个字节。
- [IOMappedWrite8](../1575318-iomappedwrite8.md) — 向指定的“物理”IOSpace 地址写入一个字节。
- [IOMapperIOVMAlloc](../1532986-iomapperiovmalloc.md)
- [IOMapperIOVMFree](../1532978-iomapperiovmfree.md)
- [IOMapperInsertPage](../1532970-iomapperinsertpage.md)
- [IOFlushProcessorCache](../1575308-ioflushprocessorcache.md) — 刷新映射内存的处理器缓存。

### 游标

- [IOBigMemoryCursor](../iobigmemorycursor.md) — 一个 IOMemoryCursor 的子类，以大端字节序输出 PhysicalSegments 向量。
- [IOLittleMemoryCursor](../iolittlememorycursor.md) — 一个 IOMemoryCursor 的子类，以小端字节序输出 PhysicalSegments 向量。
- [IONaturalMemoryCursor](../ionaturalmemorycursor.md) — 一个 IOMemoryCursor 的子类，以 CPU 的自然字节序输出 PhysicalSegments 向量。
- [IOMemoryCursor](../iomemorycursor.md) — 一种将内存引用转换为物理地址的机制。

## 另请参阅

### 相关资源

- [工作流与控制](workflow_and_control.md)
- [锁](locks.md)
- [数据类型](../libkern/data_types.md) — 创建字符串、数字、集合、数据对象以及驱动和内核扩展使用的其他标准类型。
