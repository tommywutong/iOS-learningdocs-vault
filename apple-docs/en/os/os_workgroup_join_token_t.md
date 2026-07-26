---
title: os_workgroup_join_token_t
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_join_token_t
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_join_token_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_join_token_t.json'
content_hash: 'sha256:358661c0eb96f3f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_workgroup_join_token_t

<sub>Type Alias</sub>

An opaque token that represents a connection between a thread and a workgroup.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef struct os_workgroup_join_token_opaque_s * os_workgroup_join_token_t;
```

## Discussion

You provide an uninitialized token structure when calling the `os_workgroup_join_self` function, which initializes the structure and fills it with information. Use that token structure in a subsequent call to `os_workgroup_leave_self` to remove the thread from the workgroup.

> [!important] Important
> You must provide the original thread, workgroup, and token when removing a thread from its workgroup. If the values don’t match, the system aborts your process.

## See Also

### Thread Attachment

- [os_workgroup_join](os_workgroup_join.md) — Adds the current thread to the specified workgroup.
- [os_workgroup_leave](os_workgroup_leave.md) — Removes the current thread from the workgroup it previously joined.
