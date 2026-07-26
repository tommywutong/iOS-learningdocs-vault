---
title: os_workgroup_join
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_join
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_join'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_join.json'
content_hash: 'sha256:316c79b43e03ffd1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_workgroup_join

<sub>Function</sub>

Adds the current thread to the specified workgroup.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern int os_workgroup_join(os_workgroup_t wg, os_workgroup_join_token_t token_out);
```

## Parameters

- `wg` — The workgroup to join.

- `token_out` — An empty token structure. This function fills the provided structure with information about the workgroup relationship. Save this structure so you can remove the thread from the workgroup later.

## Return Value

A value of `0` on success, or a nonzero error code that indicates why the function failed. Common error codes include `EINVAL` or `EALREADY`. For example, this method returns `EALREADY` if the thread already belongs to a workgroup. It returns `EINVAL` if the workgroup is already canceled.

## Discussion

When you call this function, the current thread must not belong to any workgroup. This function adds the thread to the specified workgroup and updates the `token_out` parameter. You may call this function safely from a real-time thread of your app.

> [!important] Important
> Save the `token_out` parameter so that you can remove the thread from the workgroup later. When removing a thread, the thread, workgroup, and token data must match the original values you specify for this function; if they don’t, the system aborts your process.

## See Also

### Thread Attachment

- [os_workgroup_leave](os_workgroup_leave.md) — Removes the current thread from the workgroup it previously joined.
- [os_workgroup_join_token_t](os_workgroup_join_token_t.md) — An opaque token that represents a connection between a thread and a workgroup.
