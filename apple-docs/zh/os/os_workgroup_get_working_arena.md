---
title: os_workgroup_get_working_arena
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_get_working_arena
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_get_working_arena'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_get_working_arena.json'
content_hash: 'sha256:5acbd342d1dbf3ca'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_get_working_arena

<sub>函数</sub>

检索工作组的共享数据，以及该数据中的线程专属索引。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void *os_workgroup_get_working_arena(os_workgroup_t wg, os_workgroup_index *index_out);
```

## 参数

- `wg` — 包含上下文数据的工作组。如果当前线程不是此工作组的成员，此函数会使 App 崩溃。

- `index_out` — 指向索引变量的指针。输出时，此参数包含该线程在指定工作组中的索引。如果不希望函数为该线程分配唯一索引，请指定 `NULL`。

## 返回值

指向工作组共享数据的指针；如果工作组没有共享数据，则为 `NULL`。

## 讨论

使用此函数检索工作组的共享数据。你第一次在某个线程上调用此函数并请求索引时，工作组会为该线程分配一个索引并返回它。随后从同一线程调用时，工作组会返回相同的索引值。

调用 [os_workgroup_set_working_arena](os_workgroup_set_working_arena.md) 函数时，你会指定最多可向工作组请求索引的唯一线程数。如果超出该上限，此函数会使你的 App 崩溃。

## 另请参阅

### 工作组配置

- [os_workgroup_max_parallel_threads](os_workgroup_max_parallel_threads.md) — 返回系统建议你向指定工作组添加的最大线程数。
- [os_workgroup_mpt_attr_t](os_workgroup_mpt_attr_t.md) — 包含与请求最大并行线程数相关属性的不透明结构。
- [os_workgroup_set_working_arena](os_workgroup_set_working_arena.md) — 向工作组的线程分发一块受管内存。
- [os_workgroup_index](os_workgroup_index.md) — 工作组为其已加入线程分配的唯一索引。
- [os_workgroup_working_arena_destructor_t](os_workgroup_working_arena_destructor_t.md) — 释放工作组当前已分配共享内存的函数。
