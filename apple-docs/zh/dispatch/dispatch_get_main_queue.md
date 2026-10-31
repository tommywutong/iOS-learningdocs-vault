---
title: dispatch_get_main_queue
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_get_main_queue
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_get_main_queue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_get_main_queue.json'
content_hash: 'sha256:d03db9874685b061'
translated: true
---

> 导航：[技术](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_get_main_queue

<sub>函数</sub>

返回与应用程序主线程关联的串行 dispatch queue。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
static dispatch_queue_main_tdispatch_get_main_queue();
```

## 返回值

返回主队列。该队列会在调用 `main` 之前，代表主线程自动创建。

## 讨论

系统会自动创建主队列，并将其与你的应用程序主线程关联。你的 App 会采用以下三种方式之一（且仅采用一种）来调用提交到主队列的 block：

- 调用 [dispatch_main](<dispatchmain().md>)
- 调用 [UIApplicationMain(_:_:_:_:)](<../uikit/uiapplicationmain(________)-1yub7.md>)（iOS）或 [NSApplicationMain(_:_:)](<../appkit/nsapplicationmain(____).md>)（macOS）
- 在主线程上使用 [CFRunLoop](../corefoundation/cfrunloop.md)

与全局并发队列一样，对 [dispatch_suspend](<dispatchobject/suspend().md>)、[dispatch_resume](<dispatchobject/resume().md>)、[dispatch_set_context](dispatch_set_context.md) 等的调用，在用于此函数返回的队列时没有效果。

## 另请参阅

### 相关文档

- [并发编程指南](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091)

### 队列与任务

- [dispatch_get_global_queue](dispatch_get_global_queue.md) — 返回具有指定服务质量类的系统定义全局并发队列。
- [Dispatch Queue](dispatch-queue.md) — 一个用于管理你的 App 主线程或后台线程上串行或并发执行任务的对象。
- [Dispatch Work Item](dispatch-work-item.md) — 你想要执行的工作，以一种可以为其附加完成处理程序或执行依赖关系的方式封装起来。
- [Dispatch Group](dispatch-group.md) — 一组作为单一整体来监控的任务。
- [Workloop](workloop.md) — 一个根据服务质量（QoS）级别对任务执行进行优先级排序的 dispatch 对象。
