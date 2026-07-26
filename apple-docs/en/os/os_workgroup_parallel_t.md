---
title: os_workgroup_parallel_t
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_parallel_t
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_parallel_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_parallel_t.json'
content_hash: 'sha256:6836cb8e09681e53'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_workgroup_parallel_t

<sub>Type Alias</sub>

A workgroup object that supports the scheduling of threads that work in parallel to complete a task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef OS_os_workgroup<OS_os_workgroup_parallel> * os_workgroup_parallel_t;
```

## See Also

### Parallel

- [os_workgroup_parallel_create](os_workgroup_parallel_create.md) — Creates a new workgroup that manges threads working on a single task in parallel.
