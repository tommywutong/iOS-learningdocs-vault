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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_workgroup_parallel_create

<sub>Function</sub>

Creates a new workgroup that manges threads working on a single task in parallel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern os_workgroup_parallel_tos_workgroup_parallel_create(const char *name, os_workgroup_attr_t attr);
```

## Parameters

- `name` — An optional name for the workgroup. Use this name to identify the workgroups you create. You may specify `NULL` for this parameter.

- `attr` — The attributes you apply to the workgroup.

## Return Value

An opaque workgroup object that tracks a parallel workload.

## Discussion

The returned workgroup doesn’t initially have any associated threads. Join individual threads to the workgroup by calling `os_workgroup_join_self` from the thread itself.

## See Also

### Parallel

- [os_workgroup_parallel_t](os_workgroup_parallel_t.md) — A workgroup object that supports the scheduling of threads that work in parallel to complete a task.
