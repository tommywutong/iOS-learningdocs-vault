---
title: os_workgroup_max_parallel_threads
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_max_parallel_threads
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_max_parallel_threads'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_max_parallel_threads.json'
content_hash: 'sha256:1c788f3d73b01f6f'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_max_parallel_threads

<sub>函数</sub>

返回系统建议你向指定工作组添加的最大线程数。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern int os_workgroup_max_parallel_threads(os_workgroup_t wg, os_workgroup_mpt_attr_t attr);
```

## 参数

- `wg` — 要检查的工作组。

- `attr` — 附加属性。此参数请指定 `NULL`。

## 讨论

此函数返回工作组在理论上的最大线程数，不会考虑当前系统负载，也不会考虑你的 app 是否还有其他工作组。实际有效的线程数可能更少。

## 另请参阅

### 工作组配置

- [os_workgroup_mpt_attr_t](os_workgroup_mpt_attr_t.md) — 包含与请求最大并行线程数相关属性的不透明结构。
- [os_workgroup_set_working_arena](os_workgroup_set_working_arena.md) — 向工作组的线程分发一块受管内存。
- [os_workgroup_get_working_arena](os_workgroup_get_working_arena.md) — 检索工作组的共享数据，以及该数据中的线程专属索引。
- [os_workgroup_index](os_workgroup_index.md) — 工作组为其已加入线程分配的唯一索引。
- [os_workgroup_working_arena_destructor_t](os_workgroup_working_arena_destructor_t.md) — 释放工作组当前已分配共享内存的函数。
