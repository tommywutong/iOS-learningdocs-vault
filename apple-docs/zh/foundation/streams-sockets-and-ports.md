---
title: 流、Socket 与端口
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/streams-sockets-and-ports
source_url: 'https://developer.apple.com/documentation/foundation/streams-sockets-and-ports'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/streams-sockets-and-ports.json'
content_hash: 'sha256:8ff84a694431e380'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# 流、Socket 与端口

<sub>API 集合</sub>

使用底层 Unix 特性来管理文件、进程和网络之间的输入与输出。

## 主题

### 流

- [Stream](stream.md) — 一个表示流的抽象类。
- [InputStream](inputstream.md) — 一个提供只读流功能的流。
- [OutputStream](outputstream.md) — 一个提供只写流功能的流。
- [StreamDelegate](streamdelegate.md) — 流实例的委托用来处理流上事件的接口。

### 任务与管道

- [Process](process.md) — 一个代表当前进程子进程的对象。
- [Pipe](pipe.md) — 相关进程之间的单向通信通道。

### Socket

- [Host](host.md) — 网络上单个主机的表示。_(已废弃)_
- [Port](port.md) — 一个表示通信信道的抽象类。
- [SocketPort](socketport.md) — 一个代表 BSD socket 的端口。

### 字节排序

- [字节排序工具](byte-order-utilities.md) — 检查和管理通过网络通道传输的数字的字节顺序。

## 另请参阅

### 底层工具

- [XPC](xpc.md) — 管理安全的进程间通信。
- [对象运行时](object-runtime.md) — 为基础 Objective-C 特性、Cocoa 设计模式以及 Swift 集成获取底层支持。
- [进程与线程](processes-and-threads.md) — 管理你的 App 与宿主操作系统及其他进程的交互，并实现底层并发（concurrency）特性。
