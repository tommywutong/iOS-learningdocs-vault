---
title: Dispatch 数据
framework: Dispatch
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch-data
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch-data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch-data.json'
content_hash: 'sha256:06db74460102edef'
translated: true
---

> 导航： [技术](../technologies.md) · [Dispatch](../dispatch.md)

# Dispatch 数据

<sub>API 集合</sub>

一个管理基于内存的数据缓冲区、并将其呈现为一整块连续内存的对象。

## 概述

该对象管理的内存缓冲区可以是单个连续的内存块，也可以由多个不连续的内存块组成。对于不连续的情况，dispatch data 对象会让这块内存看起来像是连续的。

## 主题

### 创建 Dispatch Data 对象

- [dispatch_data_t](dispatch_data_t.md) — 表示一块连续或稀疏内存区域的不可变对象。

## 另请参阅

### 系统事件监视

- [DispatchSource](dispatchsource.md) — 一个协调处理特定底层系统事件（例如文件系统事件、定时器和 UNIX 信号）的对象。
- [Dispatch Source](dispatch-source.md) — 一个协调处理特定底层系统事件（例如文件系统事件、定时器和 UNIX 信号）的对象。
- [DispatchIO](dispatchio.md) — 一个使用基于流或随机存取语义来管理文件描述符操作的对象。
- [DispatchData](dispatchdata.md) — 一个管理基于内存的数据缓冲区、并将其呈现为一整块连续内存的对象。
- [DispatchDataIterator](dispatchdataiterator.md) — 逐字节遍历某个 dispatch data 对象内容的迭代器。
- [Dispatch I/O](dispatch-i-o.md) — 一个使用基于流或随机存取语义来管理文件描述符操作的对象。
- [DispatchSourceProtocol](dispatchsourceprotocol.md) — 定义所有 dispatch source 类型共有的一组属性和方法。
