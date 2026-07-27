---
title: 内存分配选项
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/1539826-memory-allocation-options
source_url: 'https://developer.apple.com/documentation/foundation/1539826-memory-allocation-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/1539826-memory-allocation-options.json'
content_hash: 'sha256:7a1b692ce5f90c26'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [对象运行时](object-runtime.md) · [Objective-C 垃圾回收](objective-c-garbage-collection.md)

# 内存分配选项

<sub>API 集合</sub>

用于控制分配或重新分配可回收内存时行为的常量。

## 概述

这些常量作为位字段中的组成部分，用于指定 [NSAllocateCollectable](nsallocatecollectable.md) 和 [NSReallocateCollectable](nsreallocatecollectable.md) 的行为。

## 主题

### 常量

- [NSScannedOption](nsscannedoption.md) — 指定分配经过扫描的内存。
- [NSCollectorDisabledOption](nscollectordisabledoption.md) — 指定保留该 block，因而不能对其进行回收。指定此选项等同于调用 [disableCollectorForPointer:](nsgarbagecollector/disablecollectorforpointer_.md)，并将返回的 block 作为实参。

## 另请参阅

### 旧式
