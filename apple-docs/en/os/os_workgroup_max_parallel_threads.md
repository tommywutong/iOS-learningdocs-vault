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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_workgroup_max_parallel_threads

<sub>Function</sub>

Returns the maximum number of threads that the system recommends you add to the specified workgroup.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern int os_workgroup_max_parallel_threads(os_workgroup_t wg, os_workgroup_mpt_attr_t attr);
```

## Parameters

- `wg` — The workgroup to examine.

- `attr` — Additional attributes. Specify `NULL` for this parameter.

## Discussion

This function returns the theoretical maximum number of threads for a workgroup, which doesn’t take into account the current system load or whether your app has any other workgroups. The actual number of effective threads may be lower.

## See Also

### Workgroup Configuration

- [os_workgroup_mpt_attr_t](os_workgroup_mpt_attr_t.md) — An opaque structure containing attributes related to a request for the maximum number of parallel threads.
- [os_workgroup_set_working_arena](os_workgroup_set_working_arena.md) — Distributes a block of managed memory to the threads of a workgroup.
- [os_workgroup_get_working_arena](os_workgroup_get_working_arena.md) — Retrieves the workgroup’s shared data, and the thread-specific index into that data.
- [os_workgroup_index](os_workgroup_index.md) — A unique index that the workgroup assigns to its joined threads.
- [os_workgroup_working_arena_destructor_t](os_workgroup_working_arena_destructor_t.md) — A function that deallocates a workgroup’s currently assigned shared memory.
