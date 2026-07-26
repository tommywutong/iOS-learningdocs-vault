---
title: Dispatch 组
framework: Dispatch
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch-group
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch-group'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch-group.json'
content_hash: 'sha256:10eab6646dccba73'
translated: true
---

> 导航： [技术](../technologies.md) · [Dispatch](../dispatch.md)

# Dispatch 组

<sub>API 集合</sub>

一组作为单一整体来监控的任务。

## 概述

group 让你能够将一组任务聚合起来，并在该 group 上同步各种行为。你可以把多个 block 附加到一个 group 上，并将它们安排到同一队列或不同队列上异步执行。当所有 block 都执行完毕后，group 会执行其完成处理程序。你也可以同步等待 group 中所有 block 执行完毕。

## 主题

### 创建 Dispatch Group

- [dispatch_group_create](<dispatchgroup/init().md>) — 创建一个可以为其分配 block 对象的新 group。
- [dispatch_group_t](dispatch_group_t.md) — 提交到队列以进行异步调用的一组 block 对象。

### 手动更新 Group

- [dispatch_group_enter](<dispatchgroup/enter().md>) — 明确表示有一个 block 已进入该 group。
- [dispatch_group_leave](<dispatchgroup/leave().md>) — 明确表示 group 中的某个 block 已执行完毕。

## 另请参阅

### 队列与任务

- [DispatchQueue](dispatchqueue.md) — 一个用于管理你的 App 主线程或后台线程上串行或并发执行任务的对象。
- [DispatchWorkItem](dispatchworkitem.md) — 你想要执行的工作，以一种可以为其附加完成处理程序或执行依赖关系的方式封装起来。
- [DispatchGroup](dispatchgroup.md) — 一组作为单一整体来监控的任务。
- [Dispatch Queue](dispatch-queue.md) — 一个用于管理你的 App 主线程或后台线程上串行或并发执行任务的对象。
- [Dispatch Work Item](dispatch-work-item.md) — 你想要执行的工作，以一种可以为其附加完成处理程序或执行依赖关系的方式封装起来。
- [Workloop](workloop.md) — 一个根据服务质量（QoS）级别对任务执行进行优先级排序的 dispatch 对象。
