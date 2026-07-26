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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_workgroup_index

<sub>Type Alias</sub>

A unique index that the workgroup assigns to its joined threads.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef uint32_t os_workgroup_index;
```

## See Also

### Workgroup Configuration

- [os_workgroup_max_parallel_threads](os_workgroup_max_parallel_threads.md) — Returns the maximum number of threads that the system recommends you add to the specified workgroup.
- [os_workgroup_mpt_attr_t](os_workgroup_mpt_attr_t.md) — An opaque structure containing attributes related to a request for the maximum number of parallel threads.
- [os_workgroup_set_working_arena](os_workgroup_set_working_arena.md) — Distributes a block of managed memory to the threads of a workgroup.
- [os_workgroup_get_working_arena](os_workgroup_get_working_arena.md) — Retrieves the workgroup’s shared data, and the thread-specific index into that data.
- [os_workgroup_working_arena_destructor_t](os_workgroup_working_arena_destructor_t.md) — A function that deallocates a workgroup’s currently assigned shared memory.
