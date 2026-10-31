---
title: os_workgroup_set_working_arena
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_set_working_arena
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_set_working_arena'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_set_working_arena.json'
content_hash: 'sha256:3ed19563b99489a1'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_set_working_arena

<sub>函数</sub>

向工作组的线程分发一块受管内存。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern int os_workgroup_set_working_arena(os_workgroup_t wg, void *arena, uint32_t max_workers, os_workgroup_working_arena_destructor_t destructor);
```

## 参数

- `wg` — 用于存储共享数据的工作组。该工作组不得有任何已加入的线程，且必须处于空闲状态。

- `arena` — 指向你要在工作组线程之间分发的数据的指针。指定 `NULL` 可从工作组中移除任何共享数据。

- `max_workers` — 可向工作组请求唯一索引的最大线程数。如果你的线程共享全部数据，而不是只操作其中一部分，请为此参数指定 `0`。

- `destructor` — 用于释放 `arena` 参数中内存的函数。

## 返回值

成功时返回 `0`；若函数遇到问题则返回错误码。例如，若无法分配管理 arena 数据所需的内存，函数返回 `ENOMEM`。

## 讨论

使用此函数把你创建的一块内存分发给工作组的线程。用你希望这些线程执行的工作来配置这块内存。在启动间隔或并行工作组之前，以及在将任何线程加入工作组之前，调用此函数。

将 arena 数据分配给工作组后，加入你的线程并启动任务。在每个线程中，调用 [os_workgroup_get_working_arena](os_workgroup_get_working_arena.md) 函数以检索共享的 `arena` 数据，以及（可选）该线程在该数据中的唯一索引。唯一索引让你能够在各线程之间均匀划分 `arena` 数据。每个线程使用其索引访问数据的相应部分。

如果你多次调用此函数，之后的每次调用都会使用 `destructor` 函数清理先前的 arena 数据。

## 另请参阅

### 工作组配置

- [os_workgroup_max_parallel_threads](os_workgroup_max_parallel_threads.md) — 返回系统建议你向指定工作组添加的最大线程数。
- [os_workgroup_mpt_attr_t](os_workgroup_mpt_attr_t.md) — 包含与请求最大并行线程数相关属性的不透明结构。
- [os_workgroup_get_working_arena](os_workgroup_get_working_arena.md) — 检索工作组的共享数据，以及该数据中的线程专属索引。
- [os_workgroup_index](os_workgroup_index.md) — 工作组为其已加入线程分配的唯一索引。
- [os_workgroup_working_arena_destructor_t](os_workgroup_working_arena_destructor_t.md) — 释放工作组当前已分配共享内存的函数。
