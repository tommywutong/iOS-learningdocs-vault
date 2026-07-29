---
title: 原子操作
framework: Kernel
symbol_kind: symbol
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/kernel/libkern/atomic_operations
source_url: 'https://developer.apple.com/documentation/kernel/libkern/atomic_operations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/kernel/libkern/atomic_operations.json'
content_hash: 'sha256:8857d31acdb48385'
translated: true
---

> 导航：[技术](../../technologies.md) · [Kernel](../../kernel.md) · [libkern](../libkern.md)

# 原子操作

<sub>API 集合</sub>

以原子方式递增和递减数字、执行比较并交换操作以及处理其他数据。

## 主题

### 测试操作

- [OSTestAndClear](../1576463-ostestandclear.md) — 位测试并清除操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSTestAndSet](../1576456-ostestandset.md) — 位测试并设置操作，相对于平台一致性架构中所有参与的设备原子地执行。

### 递增

- [OSIncrementAtomic](../1576460-osincrementatomic.md) — 32 位递增操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSIncrementAtomic8](../1576477-osincrementatomic8.md) — 8 位递增操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSIncrementAtomic16](../1576484-osincrementatomic16.md) — 16 位递增操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSIncrementAtomic64](../1576480-osincrementatomic64.md) — 64 位递增。

### 递减

- [OSDecrementAtomic](../1576455-osdecrementatomic.md) — 32 位递减操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSDecrementAtomic8](../1576458-osdecrementatomic8.md) — 8 位递减操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSDecrementAtomic16](../1576468-osdecrementatomic16.md) — 16 位递减操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSDecrementAtomic64](../1576449-osdecrementatomic64.md) — 64 位递减。

### 比较并交换

- [OSCompareAndSwap](../1576450-oscompareandswap.md) — 比较并交换操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSCompareAndSwap64](../1576485-oscompareandswap64.md) — 64 位比较并交换操作。
- [OSCompareAndSwapPtr](../1576461-oscompareandswapptr.md) — 比较并交换操作，相对于平台一致性架构中所有参与的设备原子地执行。

### 加法

- [OSAddAtomic](../1576452-osaddatomic.md) — 32 位加法操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSAddAtomic8](../1576483-osaddatomic8.md) — 8 位加法操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSAddAtomic16](../1576475-osaddatomic16.md) — 16 位加法操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSAddAtomic64](../1576451-osaddatomic64.md) — 64 位原子加法操作。

### 布尔运算

- [OSBitAndAtomic](../1576481-osbitandatomic.md) — 32 位逻辑与操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSBitAndAtomic8](../1576487-osbitandatomic8.md) — 8 位逻辑与操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSBitAndAtomic16](../1576453-osbitandatomic16.md) — 16 位逻辑与操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSBitOrAtomic](../1576467-osbitoratomic.md) — 32 位逻辑或操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSBitOrAtomic8](../1576478-osbitoratomic8.md) — 8 位逻辑或操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSBitOrAtomic16](../1576466-osbitoratomic16.md) — 16 位逻辑或操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSBitXorAtomic](../1576476-osbitxoratomic.md) — 32 位逻辑异或操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSBitXorAtomic8](../1576459-osbitxoratomic8.md) — 8 位逻辑异或操作，相对于平台一致性架构中所有参与的设备原子地执行。
- [OSBitXorAtomic16](../1576464-osbitxoratomic16.md) — 16 位逻辑异或操作，相对于平台一致性架构中所有参与的设备原子地执行。

## 另请参阅

### 基础知识

- [数据类型](data_types.md) — 创建驱动程序与内核扩展所使用的字符串、数字、集合、数据对象以及其他标准类型。
- [字节顺序工具](byte_order_utilities.md) — 在大端序与小端序格式之间转换值。
