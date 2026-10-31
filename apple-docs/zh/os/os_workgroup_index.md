---
title: os_workgroup_index
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_index
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_index'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_index.json'
content_hash: 'sha256:c9ad12507ab2036e'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_index

<sub>类型别名</sub>

工作组为其已加入线程分配的唯一索引。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef uint32_t os_workgroup_index;
```

## 另请参阅

### 工作组配置

- [os_workgroup_max_parallel_threads](os_workgroup_max_parallel_threads.md) — 返回系统建议你向指定工作组添加的最大线程数。
- [os_workgroup_mpt_attr_t](os_workgroup_mpt_attr_t.md) — 包含与请求最大并行线程数相关属性的不透明结构。
- [os_workgroup_set_working_arena](os_workgroup_set_working_arena.md) — 向工作组的线程分发一块受管内存。
- [os_workgroup_get_working_arena](os_workgroup_get_working_arena.md) — 检索工作组的共享数据，以及该数据中的线程专属索引。
- [os_workgroup_working_arena_destructor_t](os_workgroup_working_arena_destructor_t.md) — 释放工作组当前已分配共享内存的函数。
