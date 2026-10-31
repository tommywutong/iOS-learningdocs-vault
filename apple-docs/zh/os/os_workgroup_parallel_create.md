---
title: os_workgroup_parallel_create
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_parallel_create
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_parallel_create'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_parallel_create.json'
content_hash: 'sha256:2c146ea5c7161f78'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_parallel_create

<sub>函数</sub>

创建一个新的工作组，用于管理并行处理单一任务的线程。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern os_workgroup_parallel_tos_workgroup_parallel_create(const char *name, os_workgroup_attr_t attr);
```

## 参数

- `name` — 工作组的可选名称。使用此名称标识你创建的工作组。此参数可以指定为 `NULL`。

- `attr` — 你应用于该工作组的属性。

## 返回值

跟踪并行工作负载的不透明工作组对象。

## 讨论

返回的工作组最初没有任何关联线程。请在线程自身上调用 `os_workgroup_join_self`，将该线程加入工作组。

## 另请参阅

### 并行

- [os_workgroup_parallel_t](os_workgroup_parallel_t.md) — 支持调度并行协作完成任务的线程的工作组对象。
