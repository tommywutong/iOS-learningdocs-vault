---
title: os_workgroup_leave
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_leave
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_leave'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_leave.json'
content_hash: 'sha256:d8b67010e0290c01'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_workgroup_leave

<sub>Function</sub>

Removes the current thread from the workgroup it previously joined.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void os_workgroup_leave(os_workgroup_t wg, os_workgroup_join_token_t token);
```

## Parameters

- `wg` — The workgroup to leave. This workgroup must be the same workgroup that the thread previously joined. If it isn’t, this function aborts the process.

- `token` — The token you received when the thread joined the workgroup. If the data in the token is invalid, if the token belongs to a different thread, or if the workgroup in the `wg` parameter doesn’t match the information in the token, this function aborts the process.

## Discussion

Always call this function using the same [os_workgroup_t](os_workgroup_t.md) and [os_workgroup_join_token_t](os_workgroup_join_token_t.md) structures you used at join time. If the workgroup or token information doesn’t match, this function aborts the current process. You may call this function safely from a real-time thread of your app.

> [!important] Important
> Always remove a thread from its workgroup before the thread exits. If a thread is still joined to a workgroup when it terminates, the system aborts the current process.

## See Also

### Thread Attachment

- [os_workgroup_join](os_workgroup_join.md) — Adds the current thread to the specified workgroup.
- [os_workgroup_join_token_t](os_workgroup_join_token_t.md) — An opaque token that represents a connection between a thread and a workgroup.
