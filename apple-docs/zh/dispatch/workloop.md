---
title: 工作循环
framework: Dispatch
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/workloop
source_url: 'https://developer.apple.com/documentation/dispatch/workloop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/workloop.json'
content_hash: 'sha256:3cd62d35d80b4b08'
translated: true
---

> 导航： [技术](../technologies.md) · [Dispatch](../dispatch.md)

# 工作循环（Workloop）

<sub>API 集合</sub>

一个根据服务质量（QoS）级别对任务执行进行优先级排序的 dispatch 对象。

## 概述

workloop 是一种按优先级排序的 dispatch queue，它使用 QoS 级别来确定任务的执行顺序。在开始执行每个新任务之前，该队列会评估当前已入队任务的 QoS 级别，并选出优先级最高的那个。QoS 级别为 `QOS_CLASS_USER_INTERACTIVE` 的任务优先级最高，其次是 QoS 级别为 `QOS_CLASS_USER_INITIATED` 的任务，依此类推。

workloop 是一种 [dispatch_queue_t](dispatch_queue_t.md) 对象，你使用相同的函数来将新任务加入队列。例如，使用 [dispatch_async](dispatch_async.md) 函数来异步地将一个任务加入队列。

## 主题

### 创建 Dispatch Workloop

- [dispatch_workloop_t](dispatch_workloop_t.md) — 一个根据服务质量级别对任务执行进行优先级排序的 dispatch queue。

### 同步执行任务

- [dispatch_sync](<dispatchqueue/sync(execute_)-3segw.md>) — 提交一个 block 对象以供执行，并在该 block 执行完毕后返回。
- [dispatch_async_and_wait](<dispatchqueue/asyncandwait(execute_)-1udeu.md>) — 提交一个工作项以供执行，并仅在其执行完毕后才返回。

### 管理队列特性

- [dispatch_set_target_queue](<dispatchobject/settarget(queue_).md>) — 指定用于执行与当前对象关联的工作的 dispatch queue。

## 另请参阅

### 队列与任务

- [DispatchQueue](dispatchqueue.md) — 一个用于管理你的 App 主线程或后台线程上串行或并发执行任务的对象。
- [DispatchWorkItem](dispatchworkitem.md) — 你想要执行的工作，以一种可以为其附加完成处理程序或执行依赖关系的方式封装起来。
- [DispatchGroup](dispatchgroup.md) — 一组作为单一整体来监控的任务。
- [Dispatch Queue](dispatch-queue.md) — 一个用于管理你的 App 主线程或后台线程上串行或并发执行任务的对象。
- [Dispatch Work Item](dispatch-work-item.md) — 你想要执行的工作，以一种可以为其附加完成处理程序或执行依赖关系的方式封装起来。
- [Dispatch Group](dispatch-group.md) — 一组作为单一整体来监控的任务。
