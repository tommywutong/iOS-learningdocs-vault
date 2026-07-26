---
title: Dispatch 信号量
framework: Dispatch
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch-semaphore
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch-semaphore'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch-semaphore.json'
content_hash: 'sha256:4935da2b1d3c629e'
translated: true
---

> 导航： [技术](../technologies.md) · [Dispatch](../dispatch.md)

# Dispatch 信号量

<sub>API 集合</sub>

一个通过传统计数信号量在多个执行上下文间控制对资源访问的对象。

## 概述

dispatch semaphore 是传统计数信号量的一种高效实现。dispatch semaphore 只有在调用线程需要被阻塞时才会向下调用内核。如果发起调用的 semaphore 不需要阻塞，就不会发起内核调用。

你可以通过调用 [signal()](<dispatchsemaphore/signal().md>) 方法来递增 semaphore 计数，通过调用 [dispatch_semaphore_wait](dispatch_semaphore_wait.md) 或其指定超时时间的某个变体来递减 semaphore 计数。

## 主题

### 创建信号量

- [dispatch_semaphore_create](<dispatchsemaphore/init(value_).md>) — 创建一个具有初始值的新计数信号量。
- [dispatch_semaphore_t](dispatch_semaphore_t.md) — 一个 dispatch 信号量对象。

## 另请参阅

### 任务同步

- [DispatchSemaphore](dispatchsemaphore.md) — 一个通过传统计数信号量在多个执行上下文间控制对资源访问的对象。
- [Dispatch Barrier](dispatch-barrier.md) — 并发 dispatch queue 中执行任务的一个同步点。
