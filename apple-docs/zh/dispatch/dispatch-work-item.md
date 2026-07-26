---
title: Dispatch 工作项
framework: Dispatch
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch-work-item
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch-work-item'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch-work-item.json'
content_hash: 'sha256:6366868a6a3260d1'
translated: true
---

> 导航： [技术](../technologies.md) · [Dispatch](../dispatch.md)

# Dispatch 工作项

<sub>API 集合</sub>

你想要执行的工作，以一种可以为其附加完成处理程序或执行依赖关系的方式封装起来。

## 概述

一个 dispatch work item 封装了要在某个 dispatch queue 上或某个 dispatch group 内执行的工作。你也可以把一个工作项用作 dispatch source 的事件、注册或取消处理程序。

## 另请参阅

### 队列与任务

- [DispatchQueue](dispatchqueue.md) — 一个用于管理你的 App 主线程或后台线程上串行或并发执行任务的对象。
- [DispatchWorkItem](dispatchworkitem.md) — 你想要执行的工作，以一种可以为其附加完成处理程序或执行依赖关系的方式封装起来。
- [DispatchGroup](dispatchgroup.md) — 一组作为单一整体来监控的任务。
- [Dispatch Queue](dispatch-queue.md) — 一个用于管理你的 App 主线程或后台线程上串行或并发执行任务的对象。
- [Dispatch Group](dispatch-group.md) — 一组作为单一整体来监控的任务。
- [Workloop](workloop.md) — 一个根据服务质量（QoS）级别对任务执行进行优先级排序的 dispatch 对象。
