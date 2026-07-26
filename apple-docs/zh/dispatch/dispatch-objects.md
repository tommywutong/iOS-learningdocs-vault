---
title: Dispatch 对象
framework: Dispatch
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch-objects
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch-objects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch-objects.json'
content_hash: 'sha256:c3b19c5771a6861b'
translated: true
---

> 导航： [技术](../technologies.md) · [Dispatch](../dispatch.md)

# Dispatch 对象

<sub>API 集合</sub>

所有 dispatch 类型都支持的基本行为。

## 概述

dispatch 对象有很多种类型，包括 [dispatch_queue_t](dispatch_queue_t.md)、[dispatch_group_t](dispatch_group_t.md) 和 [dispatch_source_t](dispatch_source_t.md)。基础 dispatch 对象接口让你能够管理内存、暂停和恢复执行、定义对象上下文、记录任务数据等等。

默认情况下，当你用 Objective-C 编译器构建 dispatch 对象时，它们会被声明为 Objective-C 类型。这一行为让你能够采用 ARC，并让静态分析器启用内存泄漏检查；也让你能够把这些对象加入 Cocoa 集合中。

## 主题

### 激活、暂停和恢复对象

- [dispatch_activate](<dispatchobject/activate().md>) — 激活该 dispatch 对象。
- [dispatch_suspend](<dispatchobject/suspend().md>) — 暂停某个 dispatch 对象上 block 对象的调用。
- [dispatch_resume](<dispatchobject/resume().md>) — 恢复某个 dispatch 对象上 block 对象的调用。
- [dispatch_object_t](dispatch_object_t.md) — 一个 dispatch 对象。

### 更改分配的目标队列

- [dispatch_set_target_queue](<dispatchobject/settarget(queue_).md>) — 指定用于执行与当前对象关联的工作的 dispatch queue。

## 另请参阅

### Dispatch 对象

- [DispatchObject](dispatchobject.md) — 大多数 dispatch 类型的基类。
- [DispatchPredicate](dispatchpredicate.md) — 要在给定执行上下文中求值的逻辑条件。
- [dispatchPrecondition(condition:)](<dispatchprecondition(condition_).md>) — 检查进一步执行所必需的某个 dispatch 条件。
