---
title: 进程与线程
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processes-and-threads
source_url: 'https://developer.apple.com/documentation/foundation/processes-and-threads'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processes-and-threads.json'
content_hash: 'sha256:18e1924a0f494929'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# 进程与线程

<sub>API 集合</sub>

管理 App 与宿主操作系统及其他进程的交互，并实现底层并发功能。

## 主题

### 运行循环调度

- [RunLoop](runloop.md) — 管理运行循环（run loop）输入源的对象所提供的编程接口。
- [Timer](timer.md) — 经过特定时间间隔后触发，并向目标对象发送指定消息的定时器。

### 进程信息

- [ProcessInfo](processinfo.md) — 有关当前进程的信息集合。

### 线程与锁

- [Thread](thread.md) — 执行线程。
- [NSLocking](nslocking.md) — 定义锁对象的类所采纳的基本方法。
- [NSLock](nslock.md) — 协调同一 App 内多个执行线程操作的对象。
- [NSRecursiveLock](nsrecursivelock.md) — 同一线程可以多次获取而不会导致死锁的锁。
- [NSDistributedLock](nsdistributedlock.md) — 多个主机上的多个 App 可用于限制访问文件等共享资源的锁。
- [NSConditionLock](nsconditionlock.md) — 可与用户定义的特定条件关联的锁。
- [NSCondition](nscondition.md) — 语义遵循 POSIX 样式条件的条件变量。

### 操作

- [OperationQueue](operationqueue.md) — 调节操作执行的队列。
- [Operation](operation.md) — 表示与单个任务关联的代码和数据的抽象类。
- [BlockOperation](blockoperation.md) — 管理一个或多个 block 并发执行的操作。

### 脚本与外部任务

- [Process](process.md) — 表示当前进程的子进程的对象。
- [NSUserScriptTask](nsuserscripttask.md) — 执行脚本的对象。
- [NSUserAppleScriptTask](nsuserapplescripttask.md) — 执行 AppleScript 脚本的对象。
- [NSUserAutomatorTask](nsuserautomatortask.md) — 执行 Automator 工作流程的对象。
- [NSUserUnixTask](nsuserunixtask.md) — 执行 Unix App 的对象。

## 另请参阅

### 底层实用工具

- [XPC](xpc.md) — 管理安全的进程间通信。
- [对象运行时](object-runtime.md) — 获取对 Objective-C 基本功能、Cocoa 设计模式和 Swift 集成的底层支持。
- [流、套接字与端口](streams-sockets-and-ports.md) — 使用底层 Unix 功能管理文件、进程和网络之间的输入与输出。
