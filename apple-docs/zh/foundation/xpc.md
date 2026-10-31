---
title: XPC
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xpc
source_url: 'https://developer.apple.com/documentation/foundation/xpc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xpc.json'
content_hash: 'sha256:6a201de82ec4d6c5'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# XPC

<sub>API 集合</sub>

管理安全的进程间通信。

## 主题

### XPC 客户端

- [NSXPCProxyCreating](nsxpcproxycreating.md) — 用于创建新代理对象的方法。
- [NSXPCConnection](nsxpcconnection.md) — 两个进程之间的双向通信通道。
- [NSXPCInterface](nsxpcinterface.md) — 一种可发送到导出对象或远程对象代理的接口。
- [NSXPCCoder](nsxpccoder.md) — 一个编码解码器，对你的 App 通过 XPC 连接发送的对象进行编码和解码。

### XPC 服务

- [NSXPCListener](nsxpclistener.md) — 一种监听器，等待新的传入连接、对其进行配置，并接受或拒绝它们。
- [NSXPCListenerDelegate](nsxpclistenerdelegate.md) — XPC 监听器的委托用于接受或拒绝新连接的协议。
- [NSXPCListenerEndpoint](nsxpclistenerendpoint.md) — 为特定 XPC 监听器命名的对象。

## 另请参阅

### 低层实用工具

- [Object Runtime](object-runtime.md) — 获取对 Objective-C 基本功能、Cocoa 设计模式和 Swift 集成的底层支持。
- [Processes and Threads](processes-and-threads.md) — 管理 App 与宿主操作系统及其他进程的交互，并实现底层并发功能。
- [Streams, Sockets, and Ports](streams-sockets-and-ports.md) — 使用底层 Unix 功能管理文件、进程和网络之间的输入与输出。
