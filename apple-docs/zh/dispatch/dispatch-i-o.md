---
title: Dispatch 输入输出
framework: Dispatch
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch-i-o
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch-i-o'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch-i-o.json'
content_hash: 'sha256:9acf5faad4c5c934'
translated: true
---

> 导航： [技术](../technologies.md) · [Dispatch](../dispatch.md)

# Dispatch 输入输出（I/O）

<sub>API 集合</sub>

一个使用基于流或随机存取语义来管理文件描述符操作的对象。

## 主题

### 创建 Dispatch I/O 对象

- [dispatch_io_t](dispatch_io_t.md) — 一个 dispatch I/O 通道。

### 管理文件描述符

- [dispatch_io_get_descriptor](dispatchio/filedescriptor.md) — 返回与指定通道关联的文件描述符。
- [dispatch_io_set_low_water](<dispatchio/setlimit(lowwater_).md>) — 设置在将处理程序 block 加入队列之前要处理的最小字节数。
- [dispatch_io_set_high_water](<dispatchio/setlimit(highwater_).md>) — 设置在将处理程序 block 加入队列之前要处理的最大字节数。

### 同步文件操作

- [dispatch_io_barrier](<dispatchio/barrier(execute_).md>) — 在指定通道上安排一个 barrier 操作。

## 另请参阅

### 系统事件监视

- [DispatchSource](dispatchsource.md) — 一个协调处理特定底层系统事件（例如文件系统事件、定时器和 UNIX 信号）的对象。
- [Dispatch Source](dispatch-source.md) — 一个协调处理特定底层系统事件（例如文件系统事件、定时器和 UNIX 信号）的对象。
- [DispatchIO](dispatchio.md) — 一个使用基于流或随机存取语义来管理文件描述符操作的对象。
- [DispatchData](dispatchdata.md) — 一个管理基于内存的数据缓冲区、并将其呈现为一整块连续内存的对象。
- [DispatchDataIterator](dispatchdataiterator.md) — 逐字节遍历某个 dispatch data 对象内容的迭代器。
- [Dispatch Data](dispatch-data.md) — 一个管理基于内存的数据缓冲区、并将其呈现为一整块连续内存的对象。
- [DispatchSourceProtocol](dispatchsourceprotocol.md) — 定义所有 dispatch source 类型共有的一组属性和方法。
