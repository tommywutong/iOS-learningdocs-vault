---
title: Dispatch 屏障
framework: Dispatch
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch-barrier
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch-barrier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch-barrier.json'
content_hash: 'sha256:1c7f1f74c00ba4e6'
translated: true
---

> 导航： [技术](../technologies.md) · [Dispatch](../dispatch.md)

# Dispatch 屏障

<sub>API 集合</sub>

并发 dispatch queue 中执行任务的一个同步点。

## 概述

使用 barrier 来同步 dispatch queue 中一个或多个任务的执行。当你向并发 dispatch queue 添加一个 barrier 时，该队列会延迟执行 barrier block（以及在 barrier 之后提交的任何任务），直到所有先前提交的任务执行完毕。等先前的任务执行完毕后，队列会单独执行该 barrier block。一旦 barrier block 执行完毕，队列就会恢复其正常的执行行为。

## 另请参阅

### 任务同步

- [DispatchSemaphore](dispatchsemaphore.md) — 一个通过传统计数信号量在多个执行上下文间控制对资源访问的对象。
- [Dispatch Semaphore](dispatch-semaphore.md) — 一个通过传统计数信号量在多个执行上下文间控制对资源访问的对象。
