---
title: 内存管理函数
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/memory-management-functions
source_url: 'https://developer.apple.com/documentation/foundation/memory-management-functions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/memory-management-functions.json'
content_hash: 'sha256:399f8a1e228d5045'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [对象运行时](object-runtime.md)

# 内存管理函数

<sub>API 集合</sub>

执行底层内存管理任务。

## 主题

### Core Foundation ARC 集成

- [CFBridgingRetain](<cfbridgingretain(__).md>) — 将 Objective-C 指针转换为 Core Foundation 指针，同时把所有权转移给调用方。

### 内存管理

- [NSAllocateMemoryPages](<nsallocatememorypages(__).md>) — 分配新的内存 block。
- [NSCopyMemoryPages](<nscopymemorypages(______).md>) — 复制内存 block。
- [NSDeallocateMemoryPages](<nsdeallocatememorypages(____).md>) — 释放指定的内存 block。
- [NSLogPageSize](<nslogpagesize().md>) — 返回页面大小的二进制对数。
- [NSPageSize](<nspagesize().md>) — 返回一个页面中的字节数。
- [NSRealMemoryAvailable](<nsrealmemoryavailable().md>) — 返回有关用户系统的信息。 _(已废弃)_
- [NSRoundDownToMultipleOfPageSize](<nsrounddowntomultipleofpagesize(__).md>) — 返回指定字节数向下舍入到页面大小倍数后的值。
- [NSRoundUpToMultipleOfPageSize](<nsrounduptomultipleofpagesize(__).md>) — 返回指定字节数向上舍入到页面大小倍数后的值。

## 另请参阅

### 内存管理
