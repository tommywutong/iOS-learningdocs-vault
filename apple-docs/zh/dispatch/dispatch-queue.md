---
title: Dispatch 队列
framework: Dispatch
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch-queue
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch-queue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch-queue.json'
content_hash: 'sha256:deb7580485b1dd9c'
translated: true
---

> 导航： [技术](../technologies.md) · [Dispatch](../dispatch.md)

# Dispatch 队列

<sub>API 集合</sub>

一个用于管理你的 App 主线程或后台线程上串行或并发执行任务的对象。

## 概述

dispatch queue 是先进先出（FIFO）队列，你的 App 可以以 block 对象的形式向其提交任务。dispatch queue 会串行或并发地执行任务。提交给 dispatch queue 的工作会在系统管理的一个线程池上执行。除了代表你的 App 主线程的那个 dispatch queue 之外，系统不会对使用哪个线程来执行某个任务做出任何保证。

你可以同步或异步地调度工作项。当你同步调度一个工作项时，你的代码会一直等待，直到该工作项执行完毕。当你异步调度一个工作项时，你的代码会继续执行，而该工作项会在别处运行。

> [!important] 重要
> 试图在主队列上同步执行一个工作项会导致死锁。

dispatch queue 默认对自动释放对象提供最基本的支持。系统 API 可能会向你的代码返回自动释放对象。例如，[NSError](../foundation/nserror.md) 对象通常是自动释放的。如果你发现由于 block 中创建的自动释放对象而导致内存压力增大，可以考虑向这些 block 添加自动释放池来缓解压力。你也可以在创建自定义 dispatch queue 时，使用 [dispatch_queue_attr_make_with_autorelease_frequency](dispatch_queue_attr_make_with_autorelease_frequency.md) 函数来配置其默认的自动释放行为。

### 避免过度创建线程

在为并发执行设计任务时，不要调用会阻塞当前执行线程的方法。当某个并发 dispatch queue 调度的任务阻塞了一个线程时，系统会创建额外的线程来运行其他已排队的并发任务。如果太多任务发生阻塞，系统可能会为你的 App 耗尽可用线程。

App 消耗过多线程的另一种方式，是创建了过多的私有并发 dispatch queue。因为每个 dispatch queue 都会消耗线程资源，创建更多的并发 dispatch queue 会加剧线程消耗问题。与其创建私有并发队列，不如把任务提交给某个全局并发 dispatch queue。对于串行任务，可以把你的串行队列的目标设为某个全局并发队列。这样一来，你既能保持该队列的串行行为，又能最大限度减少各自创建线程的独立队列数量。

## 主题

### 创建 Dispatch Queue

- [dispatch_queue_t](dispatch_queue_t.md) — 你的 App 用来提交 block 以供后续执行的一个轻量对象。
- [dispatch_queue_main_t](dispatch_queue_main_t.md) — 一个绑定到 App 主线程、并在该线程上串行执行任务的 dispatch queue。
- [dispatch_queue_global_t](dispatch_queue_global_t.md) — 一个使用全局线程池中的线程并发执行任务的 dispatch queue。
- [dispatch_queue_serial_t](dispatch_queue_serial_t.md) — 一个以先进先出（FIFO）顺序串行执行任务的 dispatch queue。
- [dispatch_queue_concurrent_t](dispatch_queue_concurrent_t.md) — 一个并发地、以任意顺序执行任务（同时遵守任何已设置的 barrier）的 dispatch queue。

### 配置队列执行参数

- [dispatch_queue_attr_t](dispatch_queue_attr_t.md) — 描述某个 dispatch queue 行为的一组特性。

### 同步执行任务

- [dispatch_sync](<dispatchqueue/sync(execute_)-3segw.md>) — 提交一个 block 对象以供执行，并在该 block 执行完毕后返回。
- [dispatch_async_and_wait](<dispatchqueue/asyncandwait(execute_)-1udeu.md>) — 提交一个工作项以供执行，并仅在其执行完毕后才返回。

### 管理队列特性

- [dispatch_set_target_queue](<dispatchobject/settarget(queue_).md>) — 指定用于执行与当前对象关联的工作的 dispatch queue。

### 管理主 Dispatch Queue

- [dispatch_main](<dispatchmain().md>) — 执行提交到主队列的 block。

## 另请参阅

### 队列与任务

- [DispatchQueue](dispatchqueue.md) — 一个用于管理你的 App 主线程或后台线程上串行或并发执行任务的对象。
- [DispatchWorkItem](dispatchworkitem.md) — 你想要执行的工作，以一种可以为其附加完成处理程序或执行依赖关系的方式封装起来。
- [DispatchGroup](dispatchgroup.md) — 一组作为单一整体来监控的任务。
- [Dispatch Work Item](dispatch-work-item.md) — 你想要执行的工作，以一种可以为其附加完成处理程序或执行依赖关系的方式封装起来。
- [Dispatch Group](dispatch-group.md) — 一组作为单一整体来监控的任务。
- [Workloop](workloop.md) — 一个根据服务质量（QoS）级别对任务执行进行优先级排序的 dispatch 对象。
