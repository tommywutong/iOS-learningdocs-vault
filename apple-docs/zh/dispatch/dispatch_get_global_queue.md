---
title: dispatch_get_global_queue
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_get_global_queue
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_get_global_queue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_get_global_queue.json'
content_hash: 'sha256:dd85ec0b4a4a9495'
translated: true
---

> 导航：[技术](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_get_global_queue

<sub>函数</sub>

返回具有指定服务质量类的系统定义全局并发队列。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern dispatch_queue_global_tdispatch_get_global_queue(intptr_t identifier, uintptr_t flags);
```

## 参数

- `identifier` — 你希望赋予通过此队列执行的任务的服务质量。服务质量有助于决定队列执行任务时获得的优先级。你可以指定 `QOS_CLASS_USER_INTERACTIVE`、`QOS_CLASS_USER_INITIATED`、`QOS_CLASS_UTILITY` 或 `QOS_CLASS_BACKGROUND`。处理用户交互或用户发起任务的队列，其优先级高于旨在在后台运行的任务。在 OS X 10.9 或更早版本中，你可以指定 [dispatch_queue_priority_t](dispatch_queue_priority_t.md) 中的某个 dispatch queue 优先级值。这些值会映射到相应的服务质量类。

- `flags` — 保留供将来使用的标志。此参数始终指定为 `0`。

## 返回值

所请求的全局并发队列。

## 讨论

此函数返回一个适合以指定服务质量级别执行任务的队列。对 [dispatch_suspend](<dispatchobject/suspend().md>)、[dispatch_resume](<dispatchobject/resume().md>) 和 [dispatch_set_context](dispatch_set_context.md) 函数的调用，对返回的队列没有效果。

提交到返回队列的任务会相对于彼此并发调度。

## 另请参阅

### 队列与任务

- [dispatch_get_main_queue](dispatch_get_main_queue.md) — 返回与应用程序主线程关联的串行 dispatch queue。
- [Dispatch Queue](dispatch-queue.md) — 一个用于管理你的 App 主线程或后台线程上串行或并发执行任务的对象。
- [Dispatch Work Item](dispatch-work-item.md) — 你想要执行的工作，以一种可以为其附加完成处理程序或执行依赖关系的方式封装起来。
- [Dispatch Group](dispatch-group.md) — 一组作为单一整体来监控的任务。
- [Workloop](workloop.md) — 一个根据服务质量（QoS）级别对任务执行进行优先级排序的 dispatch 对象。
